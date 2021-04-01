"""Этот модуль служит для выдачи основной информации о параметрах, навыках и статистике"""

import inventory
import items
import fight
import information
import lvl_up

# при выборе класса, один из этих словарей добавляется в параметры игрока
parameter_lord = {'heart_full': 20, 'heart': 20, 'attack': 0, 'force': 3, 'defence_full': 0, 'defence': 0,
                  'dexterity': 6, 'wisdom': 3, 'gold': 25, 'exp': 0, 'lvl': 1, 'name': 'Повелитель',}
parameter_shadow_catcher = {'heart_full': 10, 'heart': 10, 'attack': 0, 'force': 3, 'defence_full': 0,
                            'defence': 0, 'dexterity': 3, 'wisdom': 3, 'gold': 40,
                            'exp': 0, 'lvl': 1, 'name': 'Ловец душ'}
parameter_sage = {'heart_full': 10, 'heart': 10, 'magic': 0, 'magic_full': 0, 'magic_force': 0, 'force': 3,
                  'defence_full': 0, 'defence': 0, 'dexterity': 6, 'wisdom': 3, 'gold': 10, 'exp': 0, 'lvl': 1,
                  'class': 'name'}

# то, что заполняется при старте игры одним из словарей ниже
parameter = {}

# для заполнения навыками игроками во время прокачки навыков. Заполняется имя + словарь
nav_hero_have = {}
# сюда помещаются количество использований скиллов, которые можно применять в бою. словарь: название: количество
# использования навыков, обновляется каждый бой
count_active_skills = {}
# активные в данный удар навыки
active_this_hit = []

"""
Статистика: локации - для лечения и допуска, миссии - для выдачи миссий, количество боёв на разных локациях, 
заработаное золото, количество убитых гоблинов воинов - для уникального меча, количество убитых монстров -
для статистики 
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


def attack_new(attack):
    """Герой получает данное количество атаки, предыдущее значение нигде не сохраняется"""
    ans = parameter['attack'] - attack
    if ans > 0:
        print('Ваша атака увеличилась на {}'.format(parameter['attack'] - attack))
    else:
        print('Ваша атака уменьшилась на {}'.format(attack - parameter['attack']))
    parameter['attack'] = attack


def attack_receive(attack):
    """В функцию подаём значение атаки, которое игрок получает"""
    parameter['attack'] += attack
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
    print('Вы потеряли {} здоровья'.format(heart))


def heart_recovery(heart):
    """В функцию подаём значение здоровья, которое игрок восстанавливает"""
    ans = parameter['heart'] + heart
    if ans <= parameter['heart_full']:
        parameter['heart'] += heart
        print('Вы восстановили {} здоровья'.format(heart))
    else:
        print('Вы восстановили {} здоровья'.format(parameter['heart_full'] - parameter['heart']))
        parameter['heart'] = parameter['heart_full']


if 'magic' in parameter:
    def magic_recovery(magic):
        """"В функцию подаём значение маны, которое игрок восстанавливает. Отображает разницу между прошлым и значением,
        которое игрок получает, есть ограницение на восстановление"""
        ans = parameter['magic'] + magic
        if ans <= parameter['magic_full']:
            parameter['magic'] += magic
            print('Вы восстановили {} маны'.format(magic))
        else:
            print('Вы восстановили {} маны'.format(parameter['magic_full'] - parameter['magic']))
            parameter['magic'] = parameter['magic_full']


def exp_receive(exp):
    """В функцию подаём значение опыта, которое игрок получает"""
    parameter['exp'] += exp
    print('Вы получили {} опыта'.format(exp))


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
    print('Ваше максмальное здоровье увеличилась на {}'.format(heart))
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
