"""Этот модуль служит для выдачи основной информации о параметрах, навыках и статистике"""

import inventory_hero_great
import items_and_chest_great
import start_game_great
import basics_fight

"""При выборе класса, один из этих словарей добавляется в параметры игрока"""

parameter_lord = {'heart_full': 20, 'heart': 20, 'attack': 0, 'force': 3, 'full_defence': 0, 'defence': 0,
                  'dexterity': 6, 'wisdom': 3, 'gold': 2000000000, 'exp': 5000000000, 'lvl': 1, 'name': 'Повелитель', }
parameter_shadow_catcher = {'heart_full': 10, 'heart': 10, 'attack': 0, 'force': 3,
                            'defence': 0, 'dexterity': 3, 'wisdom': 3, 'gold': 40,
                            'exp': 0, 'lvl': 1, 'name': 'Ловец душ'}
parameter_sage = {'heart_full': 10, 'heart': 10, 'magic': 0, 'magic_full': 0, 'magic_force': 0, 'force': 3,
                  'defence': 0, 'dexterity': 6, 'wisdom': 3, 'gold': 10, 'exp': 0, 'lvl': 1, 'class': 'name'}

# то, что заполняется при старте игры одним из словарей ниже
parameter = {}

# для заполнения выбором во время прокачки навыков. Заполняется имя + словарь
nav = {}
# сюда помещаются активные скилы, применяемые в бою. словарь значие: количество использований
skills_active = {}
# используемые в данный момент навыки
active = []

"""
Статистика. Локации - для лечения и допуска. Миссии - для выдачи миссий. Статистика боёв для статистики.
Заработаное золото, количество боёв на разных локациях
"""
statistics = {'location': 1, 'mission': 0, 'battle_in_location_1': 0, 'earned_gold': 0, 'war_goblin': 0, 'kill': 0}


def gold_spending(gold):
    """В функцию подаём значение золота, которое игрок тратит"""
    parameter['gold'] -= gold
    print('Вы потратили {} золота'.format(gold))


def gold_receive(gold):
    """В функцию подаём значение золота, которое игрок получает"""
    parameter['gold'] += gold
    print('Вы получили {} золота'.format(gold))


def new_attack(attack):
    """Герой получает данное количество атаки, предыдущее значение нигде не сохраняется"""
    parameter['attack'] += attack
    print('Ваша атака увеличилась на {}'.format(attack))


def attack_receive(attack):
    """В функцию подаём значение атаки, которое игрок получает"""
    parameter['attack'] += attack
    print('Вы получили {} атаки'.format(attack))


def lose_attack(attack):
    """Герой теряет данное количество атаки, предыдущее значение нигде не сохраняется"""
    parameter['attack'] -= attack
    print('Ваша атака уменьшилась на {}'.format(attack))


def receive_defence(defence):
    """Увеличивает на заданную величину броню игрока. Эффект от функции в бою работает только во время текущего боя"""
    parameter['defence'] += defence
    print('Защита повышена на {}'.format(defence))


def new_defence(defence):
    """Герой получает данное количество брони, предыдущее значение нигде не сохраняется"""
    parameter['attack'] += defence
    print('Ваша броня увеличилась на {}'.format(defence))


def lose_defence(defence):
    """Герой теряет данное количество брони, предыдущее значение нигде не сохраняется"""
    parameter['defence'] -= defence
    print('Вы потеряли {} брони'.format(defence))


def save_defence(defence_hero):
    """Сохраняет значение защиты перед боем в параметрах героя"""
    parameter['full_defence'] = defence_hero


def load_defence():
    """Функция загружает значение брони, т.к. оно могло изменяться во время боя"""
    parameter['defence'] = parameter['full_defence']


def heart_new(heart):
    """В функцию подаём значение здоровья, которое становится у игрока"""
    parameter['heart'] = heart


def heart_spend(heart):
    """В функцию подаём значение здоровья, которое игрок теряет"""
    parameter['heart'] -= heart
    print('Вы потеряли {} здоровья'.format(heart))


def heart_recovery(heart):
    """В функцию подаём значение здоровья, которое игрок восстанавливает"""
    parameter['heart'] += heart
    print('Вы восстановили {} здоровья'.format(heart))


if 'magic' in parameter:
    def magic_recovery(magic):
        """"В функцию подаём значение маны, которое игрок восстанавливает"""
        parameter['magic'] = magic
        print('Вы восстановили {} магии'.format(magic))


def exp_receive(exp):
    """В функцию подаём значение опыта, которое игрок получает"""
    parameter['exp'] += exp
    print('Вы получили {} опыта'.format(exp))


def mission_complete(mission):
    """Функция, которая изменяет прогресс игрока по игровому квест, меняя его значение в статистике"""
    statistics['mission'] = mission


def parameter_choice(what_parameter):
    """Присваивает данный словарь параметров основному словарю, где должны хранится параметры"""
    global parameter
    parameter = what_parameter
    print('Вы выбрали класс {}'.format(what_parameter['name']))


def statistics_gold(gold):
    """Вы задаёте количество золото, которое вы заработали, для увеличения статистики"""
    statistics['earned_gold'] += gold


def statistics_battle1():
    """Увеличивает счётчик боёв на первой локации"""
    statistics['battle_in_location_1'] += 1


def statistics_kill(num):
    """Увеличивает количество убитых противников в статистике на num"""
    statistics['kill'] += num


def war_goblin_bonus():
    """Учитывает количество убитых гоблинов воинов, чтобы выдать меч при тысячи"""
    statistics['war_goblin'] += 1
    if statistics['war_goblin'] == 1000:
        print('Вы получили Меч горя')
        inventory_hero_great.give_sword(items_and_chest_great.rare_swords[500])


def give_lvl(num):
    """Повышает параметр уровня героя на num и добавляет сундку в инвентарь уровня, которым стал герой"""
    parameter['lvl'] += num
    print("Ваш уровень повышен {} => {}".format(parameter['lvl'] - num, parameter['lvl']))
    inventory_hero_great.give_chest(100, 100, parameter['lvl'], 0)
    start_game_great.outlast()


def heart_full_upgrade(heart):
    """Увеличивает количество максимального здоровья на данную велечину"""
    parameter['heart_full'] += heart
    print('Ваше здоровье увеличилась на {}'.format(heart))
    start_game_great.outlast()


def force_upgrade(force):
    """Увеличивает количество силы игрока на данную велечину"""
    parameter['force'] += force
    print('Ваша сила увеличилась на {}'.format(force))
    start_game_great.outlast()


def dexterity_upgrade(dexterity):
    """Увеличивает количество ловкости игрока на данную велечину"""
    parameter['dexterity'] += dexterity
    print('Ваша ловкость увеличилась на {}'.format(dexterity))
    start_game_great.outlast()


def wisdom_upgrade(wisdom):
    """Увеличивает количество мудрости игрока на данную велечину"""
    parameter['wisdom'] += wisdom
    print('Ваша мудрость увеличилась на {}'.format(wisdom))
    start_game_great.outlast()


def new_nav(name, nav_hero):
    """Добавляет в словарь навыков героя новый навык(элемент) заданый в агрументе функции, плюс уровень навыка и его
    прокачку"""
    nav[name] = nav_hero
    nav[name][0] += 1
    print('Вы получили новый навык {}'.format(name))
    additional_setting_skills(name)
    start_game_great.outlast()


def upgrade_nav(name):
    """Принимает навык который нужно прокачивать и прокачивает его на 1"""
    nav[name][0] += 1
    print('Навык {} {} -> {} прокачен'.format(name, nav[name][0]-1, nav[name][0]))
    additional_setting_skills(name)
    start_game_great.outlast()


def additional_setting_skills(name):
    """Реализация некоторых навыков сразу после прокачки. Подаётся имя навыка. Добавляются активные навыки в список"""
    if name == 'Божественное провиденье':
        attack_receive(grade_nav_value_lvl_difference('Божественное провиденье'))


def grade_nav_value_lvl_difference(name):
    """Передаёт значения навыка на прокачке через два путя. Первый раз и непервый, чтобы не out of range.
    После добавления навыка в список. value = разница значений двух уровней навыка, определяемых словарём навыков.
    Подаётся имя добавленного навыка. Используемый одноразовыми навыками. вычисляется разница между прошлым и
    настоящим значением"""
    if nav[name][0] <= 1:
        value = nav[name][1][nav[name][0]]
    else:
        value = nav[name][1][nav[name][0]] - nav[name][1][nav[name][0]-1]
    return value


def skill_on():
    """Заполнение значений всех разовые скилов перед боем, для многоразоваого использования"""
    if 'Демонический облик' in nav:
        skills_active['Демонический облик'] = 'full'
    if 'Длань господа' in nav:
        skills_active['Длань господа'] = 1


def skills_clear():
    """Очищает список активных скиллов игрока от одноразовых, оставляя скилы состояний, должен работать после каждой
    атаки"""
    # список скилов, которые работают постоянно
    skills_active_hero_on = ['Демонический облик']
    for skill in active:
        if skill not in skills_active_hero_on:
            active.remove(skill)


def activated_skill(name_skills, monster, value):
    """Функция использования заданного навыка с полным расчётом боя, проверкой и учётом использования"""
    if value == 'full' or value > 0:
        global active
        if value != 'full':
            skills_active[name_skills] -= 1
        print('Вы используете навык {}'.format(name_skills))
        active.append(name_skills)
        if name_skills != 'Демонический облик':
            basics_fight.attack(monster)
    else:
        print('Навык нельзя больше использовать')
