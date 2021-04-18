from colorama import Fore, Style
from progress.bar import FillingCirclesBar, FillingSquaresBar

import information


class Creature:
    """живое создание"""

    def __init__(self):
        self.exp_to_lvl = None
        self.full_heart = 0
        self.heart = 0
        self.full_attack = 0
        self.attack = 0
        self.full_force = 0
        self.force = 0
        self.full_defence = 0
        self.defence = 0
        self.full_dexterity = 0
        self.dexterity = 0
        self.full_wisdom = 0
        self.wisdom = 0
        self.lvl = 0
        self.exp = 0
        self.gold = 0
        self.target = ''
        self.sign = ''

    def recovery_parameter(self):
        """Восстанавливает все параметры, которые изменились по ходу битвы"""
        self.heart = self.full_heart
        self.attack = self.full_attack
        self.force = self.full_force
        self.defence = self.full_defence
        self.dexterity = self.full_dexterity
        self.wisdom = self.full_wisdom

    def alive(self):
        return self.heart > 0

    def progress_exp(self):
        """отображает количество здоровья в виде прогресс-бара"""
        s = '{}{}'.format(Fore.BLUE, '📖')
        lvl = self.lvl
        exp_for_next = self.exp_to_lvl[lvl] - self.exp_to_lvl[lvl-1]
        bar = FillingCirclesBar(s, max=exp_for_next)
        bar.index = self.exp - self.exp_to_lvl[lvl-1]
        bar.update()
        print()

    def progress_hp(self):
        """отображает количество здоровья в виде прогресс-бара"""
        s = '{}{}'.format(Fore.RED, '❤ ')
        bar = FillingSquaresBar(s, max=self.full_heart)
        bar.index = self.heart
        bar.update()
        print()

    def parameters(self):
        """Отражение параметров героя в зависимости от выбранного класса героя"""
        print(Style.RESET_ALL + '─' * 40)
        print(Fore.WHITE + Style.BRIGHT + "Уровень {}".format(self.lvl), end='  ')
        print(Fore.MAGENTA + self.sign)
        self.progress_hp()
        self.progress_exp()
        print(Fore.YELLOW + '🪙 {}'.format(self.gold), end='  ')
        print(Fore.BLUE + "⚔ {}".format(self.attack), end='  ')
        print(Fore.LIGHTBLUE_EX + Style.DIM + '👊 {}'.format(self.force), end='  ')
        print(Fore.LIGHTMAGENTA_EX + '🛡 {}'.format(self.defence), end='  ')
        print(Fore.GREEN + '🥾 {}'.format(self.dexterity), end='  ')
        print(Fore.LIGHTBLUE_EX + Style.DIM + '🧠 {}'.format(self.wisdom))
        print('─' * 40 + '\n')

    def gold_spending(self, gold):
        """В фукнцию передаем значение золота, которое тратит игрок, возвращает, получится потратить или нет"""
        # если золота достаточно
        if self.gold >= gold:
            print(Fore.YELLOW + self.target + ' -{}🪙'.format(gold))
            self.gold -= gold
            return 1
        else:
            print(self.target + ' Недостаточно золота')
            return 0

    def gold_receive(self, gold):
        """В функцию подаём значение золота, которое игрок получает"""
        print(self.target + ' +{}🪙'.format(gold))
        self.gold += gold

    def attack_new(self, attack):
        """Новое значение атаки"""
        ans = self.attack - attack
        if ans >= 0:
            print(self.target + ' +{}⚔'.format(ans))
        else:
            print(self.target + ' -{}⚔'.format(-ans))
        self.attack = attack

    def defence_new(self, defence):
        """Герой получает данное количество брони, предыдущее значение нигде не сохраняется"""
        """Новое значение атаки"""
        ans = self.defence - defence
        if ans >= 0:
            print(self.target + ' +{}🛡'.format(ans))
        else:
            print(self.target + ' -{}🛡'.format(-ans))
        self.defence = defence

    def heart_new(self, heart):
        """В функцию подаём значение здоровья, которое становится у игрока. Отображает разницу между прошлым и будующим
        здоровьем"""
        ans = self.heart - heart
        if ans >= 0:
            print(self.target + ' +{}♥'.format(ans))
        else:
            print(self.target + ' -{}♥'.format(-ans))
        self.defence = heart

    def exp_receive(self, exp):
        """В функцию подаём значение опыта, которое игрок получает"""
        self.exp += exp
        print(Fore.BLUE + self.target + ' +{} 📖'.format(exp))

    def heart_upgrade(self, heart):
        """Увеличивает количество максимального здоровья на данную велечину"""
        self.full_heart += heart
        print(self.target + ' +{}💙'.format(heart))
        information.pause()

    def force_upgrade(self, force):
        """Увеличивает количество силы игрока на данную велечину"""
        self.full_force += force
        print(self.target + ' +{}👊'.format(force))
        information.pause()

    def dexterity_upgrade(self, dexterity):
        """Увеличивает количество ловкости игрока на данную велечину"""
        self.full_dexterity += dexterity
        print(self.target + ' +{}🥾'.format(dexterity))
        information.pause()

    def wisdom_upgrade(self, wisdom):
        """Увеличивает количество мудрости игрока на данную велечину"""
        self.full_wisdom += wisdom
        print(self.target + ' +{}🧠'.format(wisdom))
        information.pause()
