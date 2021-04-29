from colorama import Fore, Style
from progress.bar import FillingCirclesBar, FillingSquaresBar

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


def two_choice():
    print('Да -> 1')
    print('Нет -> 2')


class Creature:
    """живое создание"""

    def __init__(self, **par):
        """Начальные параметры"""
        # передача значений по умолчанию
        standard = dict(heart=0, attack=0, force=0, defence=0, dexterity=0, wisdom=0, lvl=0, exp=0, gold=0, sign='🔥',
                        target='', cls='')
        for i in standard:
            if i not in par:
                par[i] = standard[i]
        # опыт до нового уровня
        self.exp_to_lvl = [0, 25, 50, 100, 500, 2500, 7500, 17000, 26000, 52000, 104000, 208000, 512000,
                           1024000]
        self.full_heart = dict(value=par['heart'], sign='💙', name='Здоровье ', front=Fore.RED)
        self.full_attack = dict(value=par['attack'], sign='🗡', name='Атака ', front=Fore.LIGHTGREEN_EX)
        self.full_force = dict(value=par['force'], sign='👊', name='Сила ', front=Fore.LIGHTBLUE_EX + Style.DIM)
        self.full_defence = dict(value=par['defence'], sign='🛡', name='Защита ', front=Fore.LIGHTMAGENTA_EX)
        self.full_dexterity = dict(value=par['dexterity'], sign='🥾', name='Ловкость ', front=Fore.GREEN)
        self.full_wisdom = dict(value=par['wisdom'], sign='🧠', front=Fore.LIGHTBLUE_EX + Style.DIM,
                                name='Мудрость ')
        self.lvl = dict(value=par['lvl'], sign='🕮', name='Уровень ', front=Fore.RED)
        self.exp = dict(value=par['exp'], sign='🌟', name='Опыт ', front=Fore.WHITE + Style.BRIGHT)
        self.gold = dict(value=par['gold'], sign='🪙', name='Золото ', front=Fore.YELLOW)
        self.skills = []
        # имя по которому происходит обращение
        self.target = dict(value=par['target'], name='Имя ', front=Fore.GREEN)
        # значок в игре
        self.sign = dict(value=par['sign'], front=Fore.CYAN)
        # название класса
        self.cls = dict(value=par['sign'], front=Fore.WHITE)

        self.heart = self.full_heart.copy()
        self.heart['sign'] = '♥'
        self.attack = self.full_attack.copy()
        self.force = self.full_force.copy()
        self.defence = self.full_defence.copy()
        self.dexterity = self.full_dexterity.copy()
        self.wisdom = self.full_wisdom.copy()

    def display_parameter(self, name, en='\n'):
        """Передаем имя параметра - выводим цвет и значение"""
        print(getattr(self, name)['front'] + str(getattr(self, name)['value']) + Style.RESET_ALL, end=en)

    def display_name_and_par(self, name, en='\n'):
        """Передаем имя параметра - выводим цвет и значение"""
        print(getattr(self, name)['front'] + getattr(self, name)['name'] + str(getattr(self, name)['value'])
              + Style.RESET_ALL, end=en)

    def display_par_and_sign(self, name, en='\n'):
        """Передаем имя параметра - выводим цвет и значение"""
        print(getattr(self, name)['front'] + getattr(self, name)['sign'] + ' ' + str(getattr(self, name)['value'])
              + Style.RESET_ALL, end=en)

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

    def _reset_front(self):
        """Сброс цвета шрифта"""
        print(Style.RESET_ALL)

    def __repr__(self):
        """Отображение информации о классах"""
        return '[%s: %s]' % (self.__class__.__name__, self._gather_attrs())

    def display(self):
        """Отражение параметров героя в зависимости от выбранного класса героя"""
        print(Fore.YELLOW + '─' * 40)
        self.display_parameter('target', en=' ')
        self.display_name_and_par('lvl', en=' ')
        self.display_parameter('sign')
        self.progress_hp()
        self.progress_exp()
        # выводим значение каждого атрибута
        for atr in ('gold', 'attack', 'force', 'defence', 'dexterity', 'wisdom'):
            self.display_par_and_sign(atr, en='   ')
        self._reset_front()
        print(Fore.YELLOW + '─' * 40 + Style.RESET_ALL)

    def set_name(self, nm):
        """Дает новое имя объекту"""
        # стандартное значение
        if nm:
            self.target['value'] = nm
            return
        while True:
            print('Введите ваше имя')
            nm = input()
            print('Уверены?', nm)
            two_choice()
            st = input()
            if st == '1':
                self.target['value'] = Fore.GREEN + nm + Style.RESET_ALL
                break

    def recovery_parameter(self):
        """Восстанавливает все параметры, которые могли измениться"""
        self.heart = self.full_heart
        self.attack = self.full_attack
        self.force = self.full_force
        self.defence = self.full_defence
        self.dexterity = self.full_dexterity
        self.wisdom = self.full_wisdom

    def alive(self):
        """Возвращает истину, если объект жив"""
        return self.heart['value'] > 0

    def gold_spending(self, gold):
        """В фукнцию передаем значение золота, которое тратит игрок, возвращает, получится потратить или нет"""
        # если золота достаточно
        if self.gold['value'] >= gold:
            print(self.target['value'] + '-{}'.format(gold) + self.gold['sign'])
            self._reset_front()
            self.gold['value'] -= gold
            return 1
        else:
            print(self.target['value'] + 'Недостаточно золота')
            return 0

    def new_value(self, name, value):
        """Установка нового значения в трех режимах n-установка нового значения, - - уменьшение, + - увеличение"""
        ans = getattr(self, name)['value'] - value
        if ans >= 0:
            self.display_parameter('target', en='')
            print(' -> ' + '-{}'.format(ans), end='')
            self.display_parameter('sign', en='\n')
        else:
            self.display_parameter('target', en='')
            print(' -> ' + '+{}'.format(-ans), end='')
            self.display_parameter('sign', en='\n')
        x = getattr(self, name)
        x['value'] = value
        setattr(self, name, x)

    def increase(self, name, value):
        x = getattr(self, name)
        x['value'] += value
        self.display_parameter('target', en='')
        print(' -> ' + '+{}'.format(value), end='')
        self.display_parameter('sign', en='\n')
        setattr(self, name, x)


class Hero(Creature):
    """герой"""


class Overlord(Hero):
    """класс Повелитель"""
    def __init__(self):
        Creature.__init__(self, lvl=1, heart=25, force=4, dexterity=6, wisdom=3, gold=25, sign='🗡', cls='Повелитель ')


class Thing:
    """Создает все вещи"""
    def __init__(self, sign):
        self.lvl = {'value': 0}
        self.name = ''
        self.attack = 0
        self.defence = 0
        self.cost = 0
        self.rare = 'usual'
        self.property = ''
        self.sign = sign


class Sword(Thing):
    """Класс всех мечей"""
    def __init__(self):
        Thing.__init__(self, sign='🗡')


class Armor(Thing):
    """Класс брони"""
    def __init__(self):
        Thing.__init__(self, sign='🪖')


class Ring(Thing):
    """Класс кольца"""
    def __init__(self):
        Thing.__init__(self, sign='💍')


class Cloak(Thing):
    """Класс плаща"""
    def __init__(self):
        Thing.__init__(self, sign='🧣')


class Inventory:
    def __init__(self):
        self.sword = None
        self.armor = None
        self.ring = None
        self.cloak = None
        self.bag = []
        self.chest = []

    def size_bag(self):
        return len(self.bag)

    def size_equipment(self):
        """Есть ли у игрока надетые вещи?"""
        return len([i for i in [self.sword, self.armor, self.cloak, self.ring] if i != {}])

    def show_thing(self, item):
        if item:
            attrs = []
            for key in (x for x in dir(self) if not x.startswith('__')):
                attrs.append(key)
            attrs.sort()
            for i in attrs:
                print(getattr(self, i))
        else:
            print('Пусто')

    def equipment_show(self):
        """Показывает вещи в инвентаре"""
        print(Fore.BLUE + '═' * 40 + Style.RESET_ALL)
        self.show_thing(self.sword)
        self.show_thing(self.armor)
        self.show_thing(self.cloak)
        self.show_thing(self.ring)
        print(Fore.BLUE + '═' * 40 + Style.RESET_ALL)

    def show_things(self):
        """Функция выводит все вещи игрока в инвентаре"""
        print('「Инвентарь 」\n')
        print(Fore.GREEN + '┅' * 40 + Style.RESET_ALL)
        for item in self.bag:
            self.show_thing(item)
        print(Fore.GREEN + '┅' * 40 + Style.RESET_ALL)

    def get_thing(self, thing):
        self.bag.append(thing)

    def take_off(self, name):
        self.bag.append(getattr(self, name))
        setattr(self, name, None)

    def lose(self, name):
        """Потерять надетую вещь указанного типа"""
        setattr(self, name, None)

    def display(self):
        while True:
            self.equipment_show()
            self.show_things()
            # выбор варинта для взаимодействия с инвентарём
            choice = input("Надеть ➔ 1\n"
                           "Снять ➔ 2\n"
                           "Открыть сундуки ➔ 3\n"
                           "Вернуться ➔ 4\n")
            if choice == '1':
                self.put_on_thing()
            elif choice == '2':
                self.take_off()
            elif choice == '3':
                self.display_chest()
                if len(inventory['chest']) != 0:
                    open_chest(int(input('Какой сундук открыть?')))
                else:
                    print('У вас нет сундуков')
            elif choice == '4':
                break


if __name__ == '__main__':
    hero = Overlord()
    print(hero)
    hero.display()
    print('Тратиться 10 золота')
    hero.gold_spending(10)
    hero.display()
    # тратится больше возможного
    print('Тратиться 100 золота, если возможно')
    hero.gold_spending(100)
    hero.display()
    print('Герой получает 9 золота')
    hero.gold_receive(9)
    hero.display()
    print('Герой жив: ' + str(hero.alive()))
    hero.display()
    hero.heart['value'] = 0
    hero.display()
    print('Герой жив: ' + str(hero.alive()))
    print('Выбор имени')
    hero.set_name('Данила')
    hero.display()
    print('Установка силы на 100')
    hero.new_value('force', 100)
    hero.display()
    print('Увеличение ловкости на 77')
    hero.increase('dexterity', 77)
    hero.display()
    print('Возвращение временных значений к первоначальным')
    hero.recovery_parameter()
    hero.display()
