from colorama import Fore, Style

import hero

HELP_MESSAGE = Fore.CYAN + Style.DIM
LVL_UP_MESSAGE = Fore.YELLOW + Style.BRIGHT
passive_skills = ['Демонический облик']
exp = [0, 50, 100, 500, 2500, 7500, 17000, 26000, 52000, 104000, 208000, 512000, 1024000]


def start():
    """Функция, которой герой выбирает какие параметры прокачивать, не сделано для всех классов"""
    hero.get_lvl(1)
    print(HELP_MESSAGE + "Выберите две характеристики для повышения")
    print(HELP_MESSAGE + 'Введите первую')
    parameter()
    print(HELP_MESSAGE + 'Введите вторую')
    parameter()


def parameter():
    """Вы выбираете характеристику, она повышается. Ничего не возвращает"""
    while True:
        number_characteristic = int(input(LVL_UP_MESSAGE + 'Здоровье + {} -> 1\n'
                                          'Сила + {} -> 2\n'
                                          'Ловкость + {} -> 3\n'
                                          'Мудрость + {} -> 4\n' + Style.RESET_ALL +
                                          ''.format(10 * (hero.parameter['lvl'] - 1),
                                                    2 * (hero.parameter['lvl'] - 1),
                                                    3 * (hero.parameter['lvl'] - 1),
                                                    4 * (hero.parameter['lvl'] - 1))))
        if number_characteristic == 1:
            hero.heart_full_upgrade(10 * (hero.parameter['lvl'] - 1))
            break
        elif number_characteristic == 2:
            hero.force_upgrade(2 * (hero.parameter['lvl'] - 1))
            break
        elif number_characteristic == 3:
            hero.dexterity_upgrade(3 * (hero.parameter['lvl'] - 1))
            break
        elif number_characteristic == 4:
            hero.wisdom_upgrade(4 * (hero.parameter['lvl'] - 1))
            break
        else:
            pass


def choice_skills():  # выбор скила
    """Один из этих словарей, в зависимости от класса, присваивается словарю nav, при старте игры
    Навык характеризуется списком следующим образом 1ая цифра - уровень прокачки навыка от 0 до 3,
    2ая цифра - прокачка эффекта во всех четырёх состояниях навыка: не прокачен, первого уровня, второго,
    третьего. 3ая цифра - то, под каким номером он выводился игроку"""
    while True:
        display_inf_skills()
        if hero.parameter['name'] == 'Повелитель':
            # переход в меню выбора навыка
            choice_lord_skills()
            break


def display_inf_skills():
    """Отображение вкаченных навыков и уровней прокачки для всех классов"""
    if hero.parameter['name'] == 'Повелитель':
        if 'Длань господа' in hero.nav_hero_have:
            hand_of_god = hero.nav_hero_have['Длань господа'][0]
        else:
            hand_of_god = 0
        print('1 Длань господа *{}*: вы наносите мощный удар, который в [5, 10, 15] раз\n'
              'больше вашей атаки. Сила зависит от прокачки. Один раз за бой'.format(hand_of_god))

        if 'Божественное провиденье' in hero.nav_hero_have:
            divine_providence = hero.nav_hero_have['Божественное провиденье'][0]
        else:
            divine_providence = 0
        print('2 Божественное провиденье *{}*: Увеличивает вашу атаку на [5, 10, 20]'
              ''.format(divine_providence))

        if 'Демонический облик' in hero.nav_hero_have:
            demon_outlook = hero.nav_hero_have['Демонический облик'][0]
        else:
            demon_outlook = 0
        print('3 Демонический облик *{}*: Ваша атака увеличивается в 2 раза,\n'
              'но вы возвращаете [50, 40, 30] процентов урона себе'.format(demon_outlook))


def choice_lord_skills():
    """Выбор навыка лорда в зависимости от цифры. Передаётся цифра навыка, который игрок хочет вкачать"""
    while True:
        number = int(input('Какой навык прокачать?\n'))
        if number == 1:
            if upgrade_nav('Длань господа', [0, {1: 5, 2: 10, 3: 15}]) == 1:
                break
        elif number == 2:
            if upgrade_nav('Божественное провиденье', [0, {1: 5, 2: 10, 3: 20}]) == 1:
                break
        elif number == 3:
            if upgrade_nav('Демонический облик', [0, [50, 40, 30]]) == 1:
                break


def upgrade_nav(name, grade):
    """Даёт полный интерфейс к прокачке данного навыка, подаётся имя навыка и его прокачка. Возвращает удалась прокачка
    или нет. Тут подавляется прокачка выше 3его уровня
    Возвращает: удалась или не удалась прокачка"""
    # проверяет, есть ли в имеющихся навыках данный навык
    if name in hero.nav_hero_have:
        # проверяет, можно ли его ещё прокачивать
        if hero.nav_hero_have[name][0] < 3:
            hero.upgrade_lvl_nav(name)
            return 1
        else:
            print(Fore.RED + Style.BRIGHT + 'Навык {} нельзя больше прокачать'.format(name))
            return 0
    else:
        hero.append_new_nav(name, grade)
        return 1
