from colorama import Fore, Style

import hero

HELP_MESSAGE = Fore.CYAN + Style.DIM
LVL_UP_MESSAGE = Fore.YELLOW + Style.BRIGHT
passive_skills = ['Демонический облик']
exp = [0, 25, 50, 100, 500, 2500, 7500, 17000, 26000, 52000, 104000, 208000, 512000, 1024000]


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
        print(LVL_UP_MESSAGE + 'Здоровье + {} -> 1'.format(14 * (hero.parameter['lvl'] - 1)))
        print(LVL_UP_MESSAGE + 'Сила + {} -> 2'.format(3 * (hero.parameter['lvl'] - 1),))
        print(LVL_UP_MESSAGE + 'Ловкость + {} -> 3'.format(3 * (hero.parameter['lvl'] - 1)))
        print(LVL_UP_MESSAGE + 'Мудрость + {} -> 4'.format(4 * (hero.parameter['lvl'] - 1)) + Style.RESET_ALL)
        number_characteristic = input()
        if number_characteristic == '1':
            hero.heart_full_upgrade(14 * (hero.parameter['lvl'] - 1))
            break
        elif number_characteristic == '2':
            hero.force_upgrade(3 * (hero.parameter['lvl'] - 1))
            break
        elif number_characteristic == '3':
            hero.dexterity_upgrade(3 * (hero.parameter['lvl'] - 1))
            break
        elif number_characteristic == '4':
            hero.wisdom_upgrade(4 * (hero.parameter['lvl'] - 1))
            break
        else:
            pass


def choice_skills():  # выбор скила
    """Один из этих словарей, в зависимости от класса, присваивается словарю nav, при старте игры
    Навык характеризуется списком следующим образом 1ая цифра - уровень прокачки навыка от 0 до 3,
    2ая цифра - прокачка эффекта во всех четырёх состояниях навыка: не прокачен, первого уровня, второго,
    третьего. 3ая цифра - то, под каким номером он выводился игроку"""
    display_inf_skills()
    choice_skills()
    number = int(input('Какой навык прокачать?\n'))


def display_inf_skills():
    """Отображение вкаченных навыков и уровней прокачки для всех классов"""
    for perk in hero.skills:
        print(hero.skills[perk]['info'])


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
