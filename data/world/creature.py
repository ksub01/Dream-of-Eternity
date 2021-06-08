# sys.path.append('/home/dreamer/projects/DreamOfEternity')
import random
import time

from colorama import Fore, Style
from progress.bar import FillingCirclesBar, FillingSquaresBar
from progress.spinner import Spinner

import data.items.items as items


INVENTORY_MESSAGE = Fore.GREEN + Style.BRIGHT
DIE_MASSAGE = Fore.RED + Style.BRIGHT
HELP_MESSAGE = Fore.CYAN + Style.DIM
TOWN_MESSAGE = Style.DIM + Fore.LIGHTYELLOW_EX
MENU_TOWN_MASSAGE = Fore.LIGHTBLUE_EX
STORY_MESSAGE = Fore.YELLOW + Style.DIM
MESSAGE_DIALOGUE = Fore.GREEN
LVL_UP_MESSAGE = Fore.YELLOW + Style.BRIGHT
MESSAGE_DAMAGE = Fore.GREEN + Style.DIM
MESSAGE_HEAL = Fore.MAGENTA + Style.BRIGHT


class Parameter:
    def __init__(self, player, session, factor=1, heart=0, attack=0, force=0, defence=0, dexterity=0, wisdom=0,
                 lvl=0, exp=0, gold=0, sign='🔥', target='', monster=False, vision=3, cls='Монстр', skills=None,
                 feature=None):
        """Начальные параметры"""
        self.player = player
        self.session = session
        self.exp_to_lvl = [0, 25, 50, 100, 500, 2500, 7500, 17000, 26000, 52000, 104000, 208000, 512000,
                           1024000]



        self.full_heart = dict(value=heart*factor, sign='💙', name='Здоровье ', front=Fore.RED)
        self.full_attack = dict(value=attack*factor, sign='🗡', name='Атака ', front=Fore.LIGHTGREEN_EX)
        self.full_force = dict(value=force*factor, sign='👊', name='Сила ', front=Fore.LIGHTBLUE_EX + Style.DIM)
        self.full_defence = dict(value=defence*factor, sign='🛡', name='Защита ', front=Fore.LIGHTMAGENTA_EX)
        self.full_dexterity = dict(value=dexterity*factor, sign='🥾', name='Ловкость ', front=Fore.GREEN)
        self.full_wisdom = dict(value=wisdom*factor, sign='🧠', front=Fore.LIGHTBLUE_EX + Style.DIM,
                                name='Мудрость ')
        self.lvl = dict(value=lvl, sign='🕮', name='Уровень ', front=Fore.RED)
        self.exp = dict(value=exp*factor, sign='🌟', name='Опыт ', front=Fore.WHITE + Style.BRIGHT)
        self.gold = dict(value=gold*factor, sign='🪙', name='Золото ', front=Fore.YELLOW)
        # имя по которому происходит обращение во всех событиях
        self.target = dict(value=target, name='Имя ', front=Fore.GREEN)
        # значок в игре
        self.sign = dict(value=sign, front=Fore.CYAN)
        self.attack = self.full_attack.copy()
        self.force = self.full_force.copy()
        self.defence = self.full_defence.copy()
        self.dexterity = self.full_dexterity.copy()
        self.wisdom = self.full_wisdom.copy()




        self.name_demon(factor)

        # название класса
        self.cls = dict(value=sign, front=Fore.WHITE)
        self.name_class = dict(value=cls, front=Fore.WHITE)
        self.heart = self.full_heart.copy()
        self.heart['sign'] = '♥'
        self.skills = skills
        self.feature = feature

        self.monster = monster
        self.factor = factor
        self.time_attack = dict(value=1, front=Fore.WHITE)
        self.vision = vision
        self.points = dict(value=0, front=Fore.WHITE)
        self.x = 0
        self.y = 0

    def name_demon(self, factor):
        if factor == 2:
            lower_name = self.target['value'][0].lower() + self.target['value'][1:].lower()
            self.target['value'] = 'Демонический ' + lower_name

    def _display_parameter(self, par='', value=True, sign=False, name=False, end='\n'):
        """Передаем имя параметра - выводим цвет и значение"""
        result = str(getattr(self, par)['front'])
        if name:
            result += str(getattr(self, par)['name'])
        if sign:
            result += str(getattr(self, par)['sign']) + ' '
        if value:
            result += str(getattr(self, par)['value'])
        result += Style.RESET_ALL
        print(result, end=end)

    def progress_exp(self):
        """отображает количество здоровья в виде прогресс-бара"""
        s = '{}{}'.format(Fore.BLUE, '📖')
        lvl = self.lvl['value']
        exp_for_next = self.exp_to_lvl[lvl] - self.exp_to_lvl[lvl - 1]
        bar = FillingCirclesBar(s, max=exp_for_next)
        bar.index = self.exp['value'] - self.exp_to_lvl[lvl - 1]
        bar.update()
        print()

    def progress_hp(self):
        """отображает количество здоровья в виде прогресс-бара"""
        s = '{}{}'.format(Fore.RED, '❤ ')
        bar = FillingSquaresBar(s, max=self.full_heart['value'])
        bar.index = self.heart['value']
        bar.update()
        print()

    def _gather_attrs(self):
        attrs = []
        for key in sorted(self.__dict__):
            attrs.append('%s=%s' % (key, getattr(self, key)))
        return ', '.join(attrs)

    @staticmethod
    def _reset_front(end='\n'):
        """Сброс цвета шрифта"""
        print(Style.RESET_ALL, end=end)

    def __repr__(self):
        """Отображение информации о классах"""
        return '[%s: %s]' % (self.__class__.__name__, self._gather_attrs())

    def display(self):
        """Отражение параметров героя в зависимости от выбранного класса героя"""
        # сделано очень костыльно
        print(Fore.YELLOW + '─' * 40)
        self._display_parameter('target', end=' ')
        self._display_parameter('lvl', name=True, end=' ')
        self._display_parameter('sign', end='\n')
        self.progress_hp()
        if self.monster:
            pass
        else:
            self.progress_exp()
            for atr in ('gold', 'attack', 'force', 'defence', 'dexterity', 'wisdom'):
                self._display_parameter(atr, sign=True, end='   ')
            print()
        self._reset_front(end='')
        print(Fore.YELLOW + '─' * 40 + Style.RESET_ALL)

    @staticmethod
    def two_choice():
        print('Да -> 1')
        print('Нет -> 2')

    def set_name(self, name=''):
        """Дает новое имя объекту"""
        # стандартное значение
        if name:
            self.target['value'] = name + ' '
            return
        while True:
            print(MESSAGE_DIALOGUE + 'Введите ваше имя' + Style.RESET_ALL)
            name = input() + ' '
            print()
            print(MENU_TOWN_MASSAGE + 'Уверены?', name)
            print()
            self.two_choice()
            print(Style.RESET_ALL, end='')
            ch = input()
            if ch == '1':
                self.target['value'] = Fore.GREEN + name + Style.RESET_ALL
                break

    def recovery_parameter(self):
        """Восстанавливает все параметры, которые могли измениться"""
        self.attack = self.full_attack.copy()
        self.force = self.full_force.copy()
        self.defence = self.full_defence.copy()
        self.dexterity = self.full_dexterity.copy()
        self.wisdom = self.full_wisdom.copy()

    def alive(self):
        """Возвращает истину, если объект жив"""
        return self.heart['value'] > 0

    def gold_spending(self, gold):
        """В фукнцию передаем значение золота, которое тратит игрок, возвращает, получится потратить или нет"""
        # если золота достаточно
        if self.gold['value'] >= gold:
            self._display_parameter('target', end='')
            print(getattr(self, 'gold')['front'] + '-> ' + '-{}'.format(gold), end='')
            self._display_parameter('gold', value=False, sign=True, end='')
            self.gold['value'] -= gold
            self._reset_front()
            return 1
        else:
            self._display_parameter('target', end='')
            print(getattr(self, 'gold')['front'] + '-> ' + 'Недостаточно золота', end='')
            self._reset_front()
            return 0

    def new_value(self, name, value):
        """новое значение для характеристики"""
        ans = getattr(self, name)['value'] - value
        atr = getattr(self, name)
        self._display_parameter('target', end='')
        if ans >= 0:
            print(atr['front'] + ' -> ' + '-{}'.format(ans), end=' ')
        else:
            print(atr['front'] + ' -> ' + '+{}'.format(-ans), end=' ')
        self._display_parameter(name, value=False, sign=True, end='\n')
        atr['value'] = value
        setattr(self, name, atr)

    def increase(self, name, value, flag=True):
        """увеличение данной характеристики"""
        atr = getattr(self, name)
        atr['value'] += value
        if flag:
            self._display_parameter('target', end='')
            print(atr['front'] + ' -> ' + '+{}'.format(value), end=' ')
            self._display_parameter(name, sign=True, value=False, end='\n')
        setattr(self, name, atr)

    def spend(self, name, value, flag=True):
        """увеличение данной характеристики"""
        atr = getattr(self, name)
        atr['value'] -= value
        if flag:
            self._display_parameter('target', end='')
            print(atr['front'] + ' -> ' + '-{}'.format(value), end=' ')
            self._display_parameter(name, sign=True, value=False, end='\n')
        setattr(self, name, atr)

    @staticmethod
    def effect_hit(creature):
        s = '{} {}{} '.format(creature.parameter.sign['value'], Fore.GREEN, '')
        spinner = Spinner(s)
        for i in range(3):
            time.sleep(0.1)
            spinner.next()
        print(end=' ')

    def up_parameter(self):
        while True:
            coefficient = self.lvl['value'] - 1
            print(LVL_UP_MESSAGE + 'Здоровье + {} -> 1'.format(14 * coefficient))
            print(LVL_UP_MESSAGE + 'Сила + {} -> 2'.format(3 * coefficient))
            print(LVL_UP_MESSAGE + 'Ловкость + {} -> 3'.format(3 * coefficient))
            print(LVL_UP_MESSAGE + 'Мудрость + {} -> 4'.format(4 * coefficient) + Style.RESET_ALL)
            number_characteristic = input()
            if number_characteristic == '1':
                self.increase('full_heart', 14 * coefficient)
                break
            elif number_characteristic == '2':
                self.increase('full_force', 3 * coefficient)
                break
            elif number_characteristic == '3':
                self.increase('full_dexterity', 3 * coefficient)
                break
            elif number_characteristic == '4':
                self.increase('full_wisdom', 4 * coefficient)
                break

    def get_lvl(self, num):
        """Повышает параметр уровня героя на num и добавляет сундк в инвентарь уровня, которыё равен полученному уровню
        Передаётся: количество уровней, которые получает игрок"""
        self.lvl['value'] += num
        print("Ваш уровень повышен {} => {}".format(self.lvl['value'] - num, self.lvl['value']))
        self.session.pause()

    def lvl_up(self):
        self.get_lvl(1)
        print(HELP_MESSAGE + "Выберите две характеристики для повышения")
        print(HELP_MESSAGE + 'Введите первую')
        self.up_parameter()
        self.session.pause()
        print(HELP_MESSAGE + 'Введите вторую')
        self.up_parameter()
        self.session.pause()
        self.player.inventory.give_chest(100, 100, self.lvl['value'] - 1, 0)
        print('Получено очко особого умения')
        self.player.skills.update()

    def test_lvl_up(self):
        return self.exp['value'] >= self.exp_to_lvl[self.lvl['value']]

    def moving(self, side, val, height, width):
        if 0 <= self.x < width and 0 <= self.y < height and self.points['value'] - val >= 0:
            sides = dict(d=(0, 1), w=(1, 0), s=(-1, 0), a=(0, -1))
            new_x, new_y = sides[side]
            new_x *= val
            new_y *= val
            self.x += new_x
            self.y += new_y
            self.spend('points', val, flag=False)
        else:
            print('Движение не возможно')

    @staticmethod
    def monster_move(player, creep, val, side):
        player_res = getattr(player.parameter, side)
        creep_res = getattr(creep.parameter, side)
        if creep_res > player_res:
            cou = 1
        elif creep_res == player_res:
            cou = 0
        else:
            cou = -1
        if val >= abs(creep_res - player_res - cou):
            past = getattr(creep.parameter, side)
            setattr(creep.parameter, side, player_res + cou)
            deference = past - getattr(creep.parameter, side)
            creep.points['value'] -= abs(deference)
        else:
            past = getattr(creep.parameter, side)
            if cou == 1:
                setattr(creep.parameter, side, past - val)
            elif cou == -1:
                setattr(creep.parameter, side, past + val)
            creep.points['value'] -= val

    @staticmethod
    def payment_attack(attacking_par, target):
        value = attacking_par.attack['value'] + attacking_par.force['value']
        if value - target.parameter.defence['value'] <= int(value * 0.4):
            damage = int((attacking_par.attack['value'] + attacking_par.force['value']) * 0.4)
        else:
            damage = (attacking_par.attack['value'] + attacking_par.force['value']
                      - target.parameter.defence['value'])
        damage = min(damage, 1)
        return damage

    def set_random_pos(self, height, width, kit: set):
        x, y = 0, 0
        while (x, y) in kit:
            x, y = random.randint(0, height - 1), random.randint(0, width - 1)
        self.x = x
        self.y = y
        kit.add((x, y))

    def random_move(self, name, border):
        s = random.randint(-1, 1)
        while not (0 <= getattr(self, name) + s < border):
            s = random.randint(-1, 1)
        self.x += s

    def hit(self, target):
        """То как расчитывается урон героя. после чего включаются соответствующие эффекты. в будующем удар героя,
         как и монста будет проходить обработку, передаётся словарь монстра"""
        # разброс урона 0.8 - 1.2
        self.effect_hit()
        damage = int(self.payment_attack(self, target) * random.randint(8, 12) / 10)
        self.time_attack['value'] -= 1
        target.parameter.spend('heart', damage)

    def reward(self, monster):
        self.increase('gold', monster.gold['value']*monster.parameter.factor)
        self.increase('exp', monster.exp['value']*monster.parameter.factor)


class Creature:
    """живое создание"""
    def __init__(self, session, factor=1, **par):
        self.parameter = Parameter(self, session, factor, **par)
        self.inventory = Inventory(self, session)
        self.stats = Statistics()
        self.skills = Skills()


class Hero(Creature):
    """герой"""


class Overlord(Hero):
    """класс Повелитель"""
    def __init__(self, session):
        Creature.__init__(self, session=session, lvl=1, heart=25, force=4, dexterity=10, wisdom=3, gold=25, sign='🧝',
                          cls='Повелитель ')


class Thing:
    """Создает все вещи"""
    def __init__(self, lvl=0, name='', attack=0, defence=0, cost=0, rare='', property={'name': 'нет'}, sign='', cls='',
                 active={'name': 'нет'}):
        # создание вещи с данными параметрами
        self.lvl = {'value': lvl, 'front': Fore.YELLOW}
        self.name = {'value': name, 'front': Fore.BLUE}
        self.attack = {'value': attack, 'front': Fore.RED}
        self.defence = {'value': defence, 'front': Fore.GREEN}
        self.cost = {'value': cost, 'front': Fore.YELLOW}
        self.rare = {'value': rare, 'front': Fore.CYAN}
        self.property = {'value': property, 'front': Fore.MAGENTA}
        self.active = {'value': active, 'front': Fore.BLUE}
        self.sign = {'value': sign, 'front': Fore.WHITE}
        self.cls = {'value': cls, 'front': Fore.WHITE}

    def display(self, pos=''):
        color = Fore.WHITE
        if self.rare['value'] == '🔵':
            color = Fore.GREEN
        elif self.rare['value'] == '🟡':
            color = Fore.BLUE
        elif self.rare['value'] == '🔴':
            color = Fore.RED
        elif self.rare['value'] == '⚪':
            color = Fore.CYAN
        elif self.rare['value'] == '⚫':
            color = Fore.BLACK
        if pos:
            print(pos, end=' ')
        print(color + str(self.name['value']), end=' ')
        print(self.lvl['front'] + str(self.lvl['value']), end=' ')
        print(self.sign['front'] + str(self.sign['value']), end='  ')
        print(self.rare['front'] + str(self.rare['value']), end='\n')
        print(self.attack['front'] + '🗡 ' + str(self.attack['value']), end='  ')
        print(self.defence['front'] + '🛡 ' + str(self.defence['value']), end='  ')
        print(self.cost['front'] + '🪙 ' + str(self.cost['value']))
        feature = items.feature[self.property['value']['name']]['description']
        if feature != 'нет':
            print(self.property['front'] + feature + Style.RESET_ALL)
        active = items.active[self.active['value']['name']]['description']
        if active != 'нет':
            print(self.active['front'] + active + Style.RESET_ALL)


class Sword(Thing):
    """Класс всех мечей"""
    def __init__(self, par):
        # создание вещи с переданными параметрами
        Thing.__init__(self, cls='sword', sign='🗡', **par)


class Armor(Thing):
    """Класс брони"""
    def __init__(self, par):
        Thing.__init__(self, cls='armor', sign='🪖', **par)


class Ring(Thing):
    """Класс кольца"""
    def __init__(self, par):
        Thing.__init__(self, cls='ring', sign='💍', **par)


class Cloak(Thing):
    """Класс плаща"""
    def __init__(self, par):
        Thing.__init__(self, cls='cloak', sign='🧣', **par)


class Inventory:
    def __init__(self, player, session):
        self.player = player
        self.session = session
        self.sword = None
        self.armor = None
        self.ring = None
        self.cloak = None
        self.bag = []
        self.chest = []
        # для выбора
        self.order = {}

    def size_bag(self):
        return len(self.bag)

    def size_equipment(self):
        """Есть ли у игрока надетые вещи?"""
        return len([i for i in [self.sword, self.armor, self.cloak, self.ring] if i is not None])

    @staticmethod
    def show_thing(item):
        if item:
            item.display()
        else:
            print('Пусто\n')

    def equipment_show(self):
        """Показывает вещи в инвентаре"""
        print(Fore.BLUE + '═' * 40 + Style.RESET_ALL)
        self.show_thing(self.sword)
        self.show_thing(self.armor)
        self.show_thing(self.cloak)
        self.show_thing(self.ring)
        print(Fore.BLUE + '═' * 40 + Style.RESET_ALL)

    def choose_thing(self):
        print('Введите номер вещи')
        number = int(input())
        return self.order[number], number

    def show_things(self):
        """Функция выводит все вещи игрока в инвентаре"""
        print()
        print(Fore.CYAN + '「Инвентарь 」\n')
        save = {}
        if self.bag:
            for num, item in zip(range(1, 10000), self.bag):
                print(Fore.GREEN + '┅' * 40 + Style.RESET_ALL)
                save[num] = item
                print(num, end=' ')
                self.show_thing(item)
                print(Fore.GREEN + '┅' * 40 + Style.RESET_ALL)
        else:
            print('Инвентарь пуст\n' + Style.RESET_ALL)
        self.order = save

    def remove_thing(self, item):
        self.bag.remove(item)

    def get_thing(self, thing):
        """Передается объект вещи"""
        print(Fore.CYAN + 'Вы получили ' + thing.name['value'] + Style.RESET_ALL)
        self.bag.append(thing)

    def get_bonus(self, item):
        self.player.parameter.full_attack['value'] += item.attack['value']
        self.player.parameter.full_defence['value'] += item.defence['value']

    def lose_bonus(self, item):
        self.player.parameter.full_attack['value'] -= item.attack['value']
        self.player.parameter.full_defence['value'] -= item.defence['value']

    def put_on(self):
        if self.size_bag():
            thing, num = self.choose_thing()
            # добавить старую вещь в инвентарь
            old_thing = getattr(self, thing.cls['value'])
            if old_thing:
                self.lose_bonus(old_thing)
                self.get_thing(old_thing)
            setattr(self, thing.cls['value'], thing)
            self.get_bonus(thing)
            # обновление полученных бонусов
            self.player.parameter.recovery_parameter()
            self.remove_thing(self.order[num])
        else:
            print('Нечего надеть')
            self.session.pause()

    def choice_take_off(self):
        print(Fore.GREEN, end='')
        print('Что снять?')
        print('Меч -> 1')
        print('Броня -> 2')
        print('Плащ -> 3')
        print('Кольцо - 4')
        print(Style.RESET_ALL, end='')
        ch = int(input())
        item = ['', 'sword', 'armor', 'cloak', 'ring']
        self.take_off(item[ch])

    def take_off(self, kind):
        self.bag.append(getattr(self, kind))
        self.lose_bonus(getattr(self, kind))
        setattr(self, kind, None)

    def lose(self, kind):
        """Потерять надетую вещь указанного типа"""
        self.lose_bonus(getattr(self, kind))
        setattr(self, kind, None)

    def display(self):
        while True:
            self.equipment_show()
            self.show_things()
            choice = input("Надеть ➔ 1\n"
                           "Снять ➔ 2\n"
                           "Открыть сундуки ➔ 3\n"
                           "Вернуться ➔ 4\n")
            if choice == '1':
                self.put_on()
            elif choice == '2':
                self.choice_take_off()
            elif choice == '3':
                self.display_chest()
                c = input('Открыть сундуки\nДа -> 1\nНет -> 2\n')
                if c == '1':
                    print('Какой номер?')
                    n = int(input())
                    self.open_chest(n)
            elif choice == '4':
                break

    def display_chest(self):
        """Отображает все сундуки, что есть у игрока, использует заглушку, костыль для отображения. ничего не принимает
        и не возвращает, просто отображает"""
        great_num = 10000000000000000000000
        if len(self.player.inventory.chest) != 0:
            for (num, weapon) in zip(range(1, great_num), self.player.inventory.chest):
                print('{} Сундук {} уровня'.format(num, weapon))
        else:
            print('У вас нет сундуков')
            self.session.pause()

    def give_chest(self, num1, num2, lvl_chest, chance_chest=0):
        """Функция, которая определяет, получает ли игрок сундук или нет. Аргументы: первая цифра для определения
        вероятности из второй цифры, например num1 = 1, num2 = 100, вероятность выпадения сундука будет равна 1%,
        ещё один пример: num1 = 3, num2 = 4 вероятность выпадения сундука - 75%. Второй аргументы - уровень получаемого
        сундука. Третиё аргумент - равен количеству дополнительных процентов выпадения сундука, которые есть у игрока.
        Из - за последнего аргумента функция в основном применяется для опеределения вероятности из 100"""
        chest_drop = random.randint(1, num2) + chance_chest
        if chest_drop <= num1:
            print(Fore.GREEN + 'Вы получили сундук {} уровня, он добавлен в ваш инвентарь'.format(lvl_chest)
                  + Style.RESET_ALL)
            self.player.inventory.chest.append(lvl_chest)
        else:
            pass

    def open_chest(self, chest_num):
        """Происходит открытие данного сундука в инвенторе и удаления его из инвентаря. Передаётся номер сундука
        и не возвращается ничего"""
        great_num = 10000000000000000000000
        for (num, chest) in zip(range(1, great_num), self.player.inventory.chest):
            if chest_num == num:
                self.chest_open(num)
                self.player.inventory.chest.remove(num)
                break
        else:
            print(Fore.RED + 'Данного сундука нет в инвентаре' + Style.RESET_ALL)
            self.session.pause()

    def chest_open(self, lvl):
        """Функция открытия сундука, которая добавляет сундук в инвентарь героя. На вход функции подаётся уровень
        получаемого сунука. Функция при первых значениях добавляет предмет в инвентарь, а при меньших добавляет золото,
        количество которого зависит от уровня героя, причём предмет, доставаемый из сундука, находится в специальном
        словаре под номером, совпадающим с уровнем сундука. Для каждого из четырёх типов предметов своё ветвление
        Подаётся: уровень сундука"""
        # вычисление вероятности
        throw = random.randint(1, 25)
        things = items.ChestThing()
        if throw == 1:
            self.player.inventory.get_thing(Sword(things.sword[lvl]))
        elif throw == 2:
            self.player.inventory.get_thing(Armor(things.armor[lvl]))
        elif throw == 3:
            self.player.inventory.get_thing(Cloak(things.cloak[lvl]))
        elif throw == 4:
            self.player.inventory.get_thing(Ring(things.ring[lvl]))
        else:
            # игрок получает количество золота, помноженное на уровень, если предмета не выпало
            get_gold = throw * self.player.parameter.lvl['value']
            self.player.parameter.increase('gold', get_gold)
        self.session.pause()


class Skills:
    """Скиллы"""
    pass


class Statistics:
    """Статистика"""

    def __init__(self):
        self.battle = 0
        self.earned_gold = 0
        self.cou_kill = 0

    def gold(self, count):
        """Вы задаёте количество золото, которое вы заработали, для увеличения статистики"""
        self.earned_gold += count

    def battles(self, count):
        """Увеличивает счётчик боёв на первой локации"""
        self.battle += count

    def kill(self, count):
        """Увеличивает количество убитых противников в статистике на kills"""
        self.cou_kill += count

    def display(self):
        pass
