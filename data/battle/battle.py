from colorama import Fore, Style

import random

import data.monsters.monsters as monsters


class Field:
    """@staticmethod
    def reset_color(func):
        func()
        print(Style.RESET_ALL, end='') """

    def __init__(self, player, creeps, ses):
        self.height = 14
        self.width = 50
        self.fill = '。'
        self.field = [self.fill * self.width for _ in range(self.height)]
        self.player = player
        self.monsters = creeps
        self.creatures = creeps[:] + [player]
        self.game = ses

    def start_pos(self):
        unique = set()
        self.player.parameter.set_random_pos(self.height, self.width, unique)
        for monster in self.monsters:
            monster.parameter.set_random_pos(self.height, self.width, unique)

    def display(self):
        print(Fore.GREEN, end='')
        for i in range(self.height):
            for j in range(self.width):
                for creep in self.creatures:
                    if creep.parameter.x == i and creep.parameter.y == j:
                        print(creep.parameter.sign['value'], end='')
                        break
                else:
                    print(self.field[i][j], end='')
            print()

    @staticmethod
    def is_neighbour(target1, target2):
        x = abs(target1.parameter.x - target2.parameter.x) <= 1
        y = abs(target1.parameter.y - target2.parameter.y) <= 1
        return x and y

    def display_enemies_parameter(self):
        for enemy in self.monsters:
            if self.is_neighbour(self.player, enemy):
                enemy.parameter.display()

    @staticmethod
    def creatures_in_cell(creatures, x, y):
        flag = False
        for creep in creatures:
            if creep.parameter.x == x and creep.parameter.y == y:
                flag = creep
        return flag

    @staticmethod
    def creatures_in_side(attacker, targets: list, side):
        bias = {'w': (-1, 0), 'd': (0, 1), 'x': (1, 0), 'a': (-1, 0), 'e': (-1, 1), 'c': (1, 1), 'z': (1, -1),
                'q': (-1, -1)}
        x, y = bias[side]
        for enemy in targets:
            right_x = enemy.parameter.x == attacker.parameter.x + x
            right_y = enemy.parameter.y == attacker.parameter.y + y
            if right_x and right_y:
                return enemy
        else:
            return False

    def detection_target(self, tester, target):
        flag = False
        x, y = tester.parameter.x, tester.parameter.y
        for i in range(-tester.parameter.vision, tester.parameter.vision + 1):
            for j in range(-tester.parameter.vision, tester.parameter.vision + 1):
                x_correct = 0 <= x+i <= self.height
                y_correct = 0 <= y+j <= self.width
                target_in_cell = self.creatures_in_cell([target], x+i, y+j)
                if x_correct and y_correct and target_in_cell:
                    flag = True
        return flag

    @staticmethod
    def start_battle_message():
        """Стартовое сообщение перед началом боя"""
        print('─' * 50)
        print(Fore.RED + ' ' * 10 + 'Начинается бой')
        print('─' * 50)

    def escape(self, creature, targets_around):
        """Побег от монстра, вункция возвращает 1 если побег удался и 0 если не удался"""
        print(creature.parameter.target['value'] + "пытается сбежать")
        self.game.pause()
        res = random.randint(1, 20)
        if res > 6:
            print(creature.parameter.target['value'] + 'сбежал')
            creature.parameter.recovery_parameter()
            self.game.pause()
            return 1
        else:
            print(creature.parameter.target['value'] + 'не удалось сбежать')
            if targets_around:
                for monster in targets_around:
                    monster.hit(creature)
            self.game.pause()
            return 0

    def attack(self, attacker, side):
        monster = self.creatures_in_side(attacker, self.creatures, side)
        if monster and attacker.time_attack['value'] > 0:
            attacker.hit(monster)
            if monster.parameter.heart['value'] <= 0:
                self.player.parameter.reward(monster)
                self.monsters.remove(monster)
        else:
            print('Атаковать не возможно')

    def progress_player(self):
        self.player.parameter.increase('points', self.player.parameter.dexterity['value'] // 5, flag=False)
        while self.player.parameter.dexterity['value']:
            points = self.player.parameter.points['value']
            print('Ваш ход')
            self.display()
            self.player.parameter.display()
            self.display_enemies_parameter()
            print('\n⚔  ➔ 1 и направление\n'
                  '🥾  ➔ 2 и направление\n'
                  '🏃  ➔ 3\n'
                  '❌  ➔ 4')
            command = input()
            if command[0] == '1':
                try:
                    self.attack(self.player, command[1])
                except IOError:
                    print('Вы ввели неправильно, попробуйте 1d1')
            elif command[0] == '2':
                try:
                    if points > 0:
                        self.player.parameter.moving(command[1], int(command[2:]), self.height, self.width)
                    else:
                        print('Вы не можете больше ходить')
                except IOError:
                    print('Вы ввели неправильно, пропробуйте 2d1')
            elif command[0] == '3':
                creeps_around = []
                for pos in 'qwedcxza':
                    creeps_around.append(self.creatures_in_side(self.player, self.monsters, pos))
                if self.escape(self.player, creeps_around):
                    return True
            elif command[0] == '4':
                return False
            self.game.pause()

    def progress_monster(self, monster):
        while monster.parameter.points['value']:
            points = monster.parameter.dexterity['value'] // 5
            time_attack = monster.parameter.time_attack['value']
            if self.is_neighbour(self.player, monster):
                if time_attack > 0:
                    monster.attack(self.player)
                    self.game.pause()
            elif self.detection_target(monster, self.player):
                monster.parameter.monster_move(self.player, monster, points, 'x')
                monster.parameter.monster_move(self.player, monster, points, 'y')
            else:
                if random.randint(0, 1):
                    monster.parameter.random_move('x', self.height)
                    monster.parameter.random_move('y', self.width)
                    break

    def fighting(self):
        """на вход подается новый экземпляр монстра"""
        # monster.bonus()
        self.start_battle_message()
        self.player.stats.battles(1)
        self.start_pos()
        while self.player.parameter.alive() and any(enemy.parameter.alive() for enemy in self.monsters):
            self.progress_player()
            for monster in self.monsters:
                self.progress_monster(monster)


class Location:
    def __init__(self, name):
        pass


class Dungeon:
    def __init__(self, event=1, ses=None):
        self.event = event
        self.game = ses

    def dungeon(self, player):
        """Запускается при заходе в лес, показывает куда можно пойти, пока сделана только первая локация."""
        while True:
            choice_location = input(Fore.GREEN + 'Куда вы поёдете?:\n'
                                    'Лес Смерти => 1\n'
                                    'Вернуться => 2\n' + Style.RESET_ALL)
            if choice_location == '1':
                print("Вы попадаете в лес Смерти")
                choice_monster = player.parameter.lvl['value'] * 3
                if choice_monster > 6:
                    choice_monster = 6
                creeps = []
                for i in range(random.randint(4, 8)):
                    what_monster = random.randint(1, choice_monster) - 1
                    name_monster = monsters.forest[what_monster]
                    creeps.append(name_monster(self.game, self.event*random.randint(8, 14) / 10))
                battle = Field(player, creeps, self.game)
                battle.fighting()
                break
            else:
                break


if __name__ == '__main__':
    pass
