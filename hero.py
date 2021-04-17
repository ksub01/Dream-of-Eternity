"""Этот модуль служит для выдачи основной информации о параметрах, навыках и статистике"""

from colorama import Fore, Style

import inventory
import items
import fight
import information
import lvl_up


class Creature:
    """живое создание"""

    def __init__(self):
        self.heart = 0
        self.attack = 0
        self.force = 0
        self.defence = 0
        self.dexterity = 0
        self.wisdom = 0
        self.lvl = 0
        self.exp = 0
        self.gold = 0


class Hero(Creature):
    """герой"""

    def __init__(self):
        super().__init__()
        self.lvl = 1

    def gold_spending(self, gold):
        """В фукнцию передаем значение золота, которое тратит игрок, возвращает, получится потратить или нет"""
        # если золота достаточно
        if self.gold >= gold:
            print(Fore.YELLOW + 'Вы потратили {}🪙 золота '.format(gold))
            self.gold -= gold
            return 1
        else:
            print('У вас недостаточно золота')
            return 0

    def gold_receive(self, gold):
        """В функцию подаём значение золота, которое игрок получает"""
        parameter['gold'] += self.gold
        print(Fore.YELLOW + '+{} 🪙'.format(gold))

    def attack_new(self, attack):
        """Герой получает данное количество атаки, предыдущее значение нигде не сохраняется"""
        ans = self.attack - attack
        if ans > 0:
            print('Ваша атака уменьшилась на {}'.format(ans))
        elif ans == 0:
            print('Ваша атака не изменилась')
        else:
            print('Ваша атака увеличилась на {}'.format(-ans))
        self.attack = attack

    def attack_receive(self, attack):
        """В функцию подаём значение атаки, которое игрок получает"""
        self.attack += attack
        print('Вы получили {} атаки'.format(attack))

    def attack_lose(attack):
        """Герой теряет данное количество атаки, предыдущее значение нигде не сохраняется"""
        parameter['attack'] -= attack
        print('Ваша атака уменьшилась на {}'.format(attack))


    def defence_receive(defence):
        """Увеличивает на заданную величину броню игрока. Эффект от функции в бою работает только во время текущего боя"""
        parameter['defence'] += defence
        print('Защита повышена на {}'.format(defence))


    def defence_new(defence):
        """Герой получает данное количество брони, предыдущее значение нигде не сохраняется"""
        ans = parameter['defence'] - defence
        if ans > 0:
            print('Ваша защита увеличилась на {}'.format(parameter['defence'] - defence))
        else:
            print('Ваша защита уменьшилась на {}'.format(defence - parameter['defence']))
        parameter['defence'] = defence


    def defence_lose(defence):
        """Герой теряет данное количество брони, предыдущее значение нигде не сохраняется"""
        parameter['defence'] -= defence
        print('Вы потеряли {} брони'.format(defence))


    def defence_save(defence_hero):
        """Сохраняет значение защиты перед боем в параметрах героя"""
        parameter['full_defence'] = defence_hero


    def defence_load():
        """Функция загружает значение брони, т.к. оно могло изменяться во время боя"""
        parameter['defence'] = parameter['full_defence']


    def heart_new(heart):
        """В функцию подаём значение здоровья, которое становится у игрока. Отображает разницу между прошлым и будующим
        здоровьем"""
        ans = heart - parameter['heart']
        if ans >= 0:
            print('Ваша здоровье увеличилась на {}'.format(heart - parameter['heart']))
        else:
            print('Ваша здоровье уменьшилась на {}'.format(parameter['heart'] - heart))
        parameter['heart'] = heart


    def heart_spend(heart):
        """В функцию подаём значение здоровья, которое игрок теряет"""
        parameter['heart'] -= heart
        print(MESSAGE_DAMAGE + '-{} ❤ '.format(heart))


    def heart_recovery(heart):
        """В функцию подаём значение здоровья, которое игрок восстанавливает"""
        ans = parameter['heart'] + heart
        if ans <= parameter['heart_full']:
            parameter['heart'] += heart
            print(MESSAGE_HEAL + '+{} ❤ '.format(heart))
        else:
            print(MESSAGE_HEAL + '+{} ❤ '.format(parameter['heart_full'] - parameter['heart']))
            parameter['heart'] = parameter['heart_full']


    def exp_receive(exp):
        """В функцию подаём значение опыта, которое игрок получает"""
        parameter['exp'] += exp
        print(Fore.BLUE + '+{} 📖'.format(exp))


class Overlord(Hero):
    """класс Повелитель"""

    def __init__(self):
        super().__init__()
        self.heart = 25
        self.force = 4
        self.dexterity = 6
        self.wisdom = 3
        self.gold = 25
        self.sign = '🗡'
        self.name = 'Повелитель'
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


class GoblinWarrior(Creature):
    """Гоблин воин"""

    def __init__(self):
        super().__init__()
        self.heart = 50
        self.force = 2
        self.dexterity = 5
        self.wisdom = 10
        self.lvl = 1
        self.gold = 10
        self.exp = 5
        self.sign = '🐺'
        self.name = 'Гоблин Воин'
        self.skills = []
        self.property = 'Убив тысячу, вы получаете меч Горя'


class Statistics:
    """Статистика"""

    def __init__(self):
        self.battle = 0
        self.earned_gold = 0
        self.kill_monsters = 0


class Quests:
    """Квесты"""

    def __init__(self):
        # для уникального Меча горя
        self.war_goblin = 0


MESSAGE_DAMAGE = Fore.RED + Style.BRIGHT
MESSAGE_HEAL = Fore.RED

skills_have_lord = {'Длань Господа': 0, 'Демоническая ярость': 0, 'Божественное провиденье': 0}
# то, что заполняется при старте игры одним из словарей ниже
parameter = {}
skills = {}

# для заполнения навыками игроками во время прокачки навыков. Заполняется имя + словарь
nav_hero_have = {}
# сюда помещаются количество использований скиллов, которые можно применять в бою. словарь: название: количество
# использования навыков, обновляется каждый бой
count_active_skills = {}
# активные в данный удар навыки
active_this_hit = []



def mission_complete(mission):
    """Функция, которая изменяет прогресс игрока по игровому квест, меняя его значение в статистике
    Передаётся: значение новой миссии"""
    statistics['mission'] = mission


def parameter_choice(what_parameter):
    """Присваивает данный словарь параметров основному словарю, где должны хранится параметры
    Передаётся: словарь параметров выбранного класса"""
    global parameter
    parameter = what_parameter
    print('Вы выбрали класс {}'.format(what_parameter['name']))


def statistics_up_gold(gold):
    """Вы задаёте количество золото, которое вы заработали, для увеличения статистики"""
    statistics['earned_gold'] += gold


def statistics_up_battle1():
    """Увеличивает счётчик боёв на первой локации"""
    statistics['battle_in_location_1'] += 1


def statistics_up_kill(num):
    """Увеличивает количество убитых противников в статистике на num"""
    statistics['kill'] += num


def bonus_war_goblin():
    """Учитывает количество убитых гоблинов воинов, чтобы выдать меч при тысячи"""
    statistics['war_goblin'] += 1
    if statistics['war_goblin'] == 1000:
        print('Вы получили Меч горя')
        inventory.give_sword(items.rare_swords[500])


def heart_full_upgrade(heart):
    """Увеличивает количество максимального здоровья на данную велечину"""
    parameter['heart_full'] += heart
    print('Ваше максимальное здоровье увеличилась на {}'.format(heart))
    information.pause()


def force_upgrade(force):
    """Увеличивает количество силы игрока на данную велечину"""
    parameter['force'] += force
    print('Ваша сила увеличилась на {}'.format(force))
    information.pause()


def dexterity_upgrade(dexterity):
    """Увеличивает количество ловкости игрока на данную велечину"""
    parameter['dexterity'] += dexterity
    print('Ваша ловкость увеличилась на {}'.format(dexterity))
    information.pause()


def wisdom_upgrade(wisdom):
    """Увеличивает количество мудрости игрока на данную велечину"""
    parameter['wisdom'] += wisdom
    print('Ваша мудрость увеличилась на {}'.format(wisdom))
    information.pause()


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


def alive():
    return parameter['heart'] > 0
