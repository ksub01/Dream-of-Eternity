"""Этот модуль служит для выдачи основной информации о параметрах, навыках и статистике"""

from colorama import Fore, Style

import inventory
import world
import fight
import information
import lvl_up

MESSAGE_DAMAGE = Fore.GREEN + Style.DIM
MESSAGE_HEAL = Fore.MAGENTA + Style.BRIGHT


def make_hero(cls):
    global heroes
    print('новый экземпляр во внутреннем файле')
    heroes = cls()


class Hero(world.Creature):
    """герой"""

    def __init__(self):
        super().__init__()
        self.lvl = 1
        self.target = ''
        self.skills = []
        self.exp_to_lvl = [0, 25, 50, 100, 500, 2500, 7500, 17000, 26000, 52000, 104000, 208000, 512000, 1024000]

    def new_name(self):
        """Выбор имени"""
        self.target = input()


class Overlord(Hero):
    """класс Повелитель"""

    def __init__(self):
        super().__init__()
        self.lvl = 1
        self.full_heart = 25
        self.heart = 25
        self.full_force = 25
        self.force = 4
        self.full_dexterity = 25
        self.dexterity = 6
        self.full_wisdom = 25
        self.wisdom = 3
        self.gold = 25
        self.sign = '🗡'
        self.cls = 'Повелитель'
        self.skills = []


class Skill:
    """Скиллы"""

    def __init__(self):
        self.lvl = 0


class HandGod(Skill):
    """Длань господа"""

    def __init__(self):
        super().__init__()
        self.lvl_up = [0, 5, 10, 15]
        self.info = ('Вы наносите мощный удар, который в раз больше вашей атаки. Сила зависит от прокачки.'
                     'Один раз за бой')
        self.influence = 'Вы чувствуете, что ваши руки способны на большее'


class DivineProvidence(Skill):
    """Божественное провиденье"""

    def __init__(self):
        super().__init__()
        self.lvl_up = [0, 5, 10, 20]
        self.info = 'Увеличивает вашу атаку'
        self.influence = 'Вы осознали, что нечто большее влияет на этот мир'


class DemonicFury(Skill):
    """Демоническая ярость"""

    def __init__(self):
        super().__init__()
        self.lvl_up = [0, 50, 40, 30]
        self.info = 'Увеличивает вашу атаку'
        self.influence = 'Ваша атака увеличивается в 2 раза, но вы возвращаете часть урона себе'


class Statistics:
    """Статистика"""

    def __init__(self):
        self.battle = 0
        self.earned_gold = 0
        self.kill_monsters = 0

    def gold(self, gold):
        """Вы задаёте количество золото, которое вы заработали, для увеличения статистики"""
        self.earned_gold += gold

    def battles(self, battle):
        """Увеличивает счётчик боёв на первой локации"""
        self.battle += battle

    def kill(self, kills):
        """Увеличивает количество убитых противников в статистике на kills"""
        self.kill += kills


class Quests:
    """Квесты"""

    def __init__(self):
        # для уникального Меча горя
        self.war_goblin = 0

    def bonus_war_goblin(self, goblins):
        """Учитывает количество убитых гоблинов воинов, чтобы выдать меч при тысячи"""
        self.war_goblin += 1
        if self.war_goblin == 1000:
            # НЕАВВВВВВВВВВВВВВВВВВВВВВВВВВВВВВВВВВВВВВВВВВВВВВВВВВВВВВВЫОЛДВАОВЫДАОВЫДАЛОЫВДЛАОЫВДЛОАДЛ
            pass






skills_have_lord = {'Длань Господа': 0, 'Демоническая ярость': 0, 'Божественное провиденье': 0}

skills = {}

# для заполнения навыками игроками во время прокачки навыков. Заполняется имя + словарь
nav_hero_have = {}
# сюда помещаются количество использований скиллов, которые можно применять в бою. словарь: название: количество
# использования навыков, обновляется каждый бой
count_active_skills = {}
# активные в данный удар навыки
active_this_hit = []




def parameter_choice(what_parameter):
    """Присваивает данный словарь параметров основному словарю, где должны хранится параметры
    Передаётся: словарь параметров выбранного класса"""
    global parameter
    parameter = what_parameter
    print('Вы выбрали класс {}'.format(what_parameter['name']))

















def get_lvl(num):
    """Повышает параметр уровня героя на num и добавляет сундк в инвентарь уровня, которыё равен полученному уровню
    Передаётся: количество уровней, которые получает игрок"""
    parameter['lvl'] += num
    print("Ваш уровень повышен {} => {}".format(parameter['lvl'] - num, parameter['lvl']))
    inventory.give_chest(100, 100, parameter['lvl'] - 1, 0)
    if parameter['name'] == 'Повелитель':
        skills.update()
    information.pause()


def append_new_nav(name, nav_hero):
    """Добавляет в словарь навыков героя новый навык(элемент) заданый в агрументе функции, плюс уровень навыка и его
    прокачку
    Передаётся: имя навыка и его прокачка"""
    nav_hero_have[name] = nav_hero
    nav_hero_have[name][0] += 1
    print('Вы получили новый навык {}'.format(name))
    skills_additional_setting(name)
    information.pause()


def upgrade_lvl_nav(name):
    """Принимает навык который нужно прокачивать и прокачивает его на 1
    Передаётся: имя навыка"""
    nav_hero_have[name][0] += 1
    print('Навык {} {} -> {} прокачен'.format(name, nav_hero_have[name][0] - 1, nav_hero_have[name][0]))
    skills_additional_setting(name)
    information.pause()


def skills_additional_setting(name):
    """Реализация некоторых навыков сразу после прокачки. Подаётся имя навыка. Добавляются активные навыки в список
    Передаётся: имя навыка, который обладает таким эффектом"""
    if name == 'Божественное провиденье':
        attack_receive(skills_value_for_grade('Божественное провиденье'))


def skills_value_for_grade(name):
    """Передаёт значения навыка на прокачке через два путя. Первый раз и не первый, чтобы не было out of range.
    После добавления навыка в список. value = разница значений двух уровней навыка, определяемых словарём навыков.
    вычисляется разница между прошлым и настоящим значениями
    Подаётся: имя навыка с пассивыным эффектом. """
    if nav_hero_have[name][0] <= 1:
        value = nav_hero_have[name][1][nav_hero_have[name][0]]
    else:
        value = nav_hero_have[name][1][nav_hero_have[name][0]] - nav_hero_have[name][1][nav_hero_have[name][0] - 1]
    return value


def skill_count_fill():
    """Заполнение значений всех разовые скилов перед боем, для многоразоваого использования, в дальнейшем количество
    уменьшается"""
    if 'Демонический облик' in nav_hero_have:
        count_active_skills['Демонический облик'] = 'full'
    if 'Длань господа' in nav_hero_have:
        count_active_skills['Длань господа'] = 1


def skills_clear():
    """Очищает список активных скиллов игрока от одноразовых, оставляя скилы состояний, должен работать после каждой
    атаки"""
    # список скилов, которые работают постоянно и их не надо выключать
    skills_active_hero_on = ['Демонический облик']
    for skill in active_this_hit:
        if skill in skills_active_hero_on:
            pass
        else:
            active_this_hit.remove(skill)


def use_skill(name_skills, monster, value):
    """Функция использования заданного навыка с боем и количества использований скилла
    Передаётся: название навыка, словарь монстра, количество использований скилла"""
    if value == 'full' or value > 0:
        global active_this_hit
        # вычитание количество исопльзований, если количество не бесконечно
        if value != 'full':
            count_active_skills[name_skills] -= 1
        print('Вы используете навык {}'.format(name_skills))
        # добавление в лист активных для проверки эффекта в бою
        active_this_hit.append(name_skills)
        # костыль, проверка на эффект для пассивных навыков
        # не модулирует бой, если навык пассивный
        if name_skills in lvl_up.passive_skills:
            pass
        else:
            fight.who_first_attack(monster)
    else:
        print('Навык нельзя больше использовать')

print('новый экземпляр во внешнем файле')
heroes = Overlord()