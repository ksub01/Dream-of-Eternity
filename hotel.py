"""Модуль, описывающий то, как происходит восстановление здоровья героя и маны, а также повышение уровня (поднятие
навыков и скилла) при приходе героя в гостиницу"""

from colorama import Fore, Style

import hero
import lvl_up
import information

TOWN_MESSAGE = Style.DIM + Fore.LIGHTYELLOW_EX
HELP_MESSAGE = Fore.CYAN + Style.DIM
MESSAGE_DIALOGUE = Fore.GREEN

# количество золота для лечения в разных локациях
price_sleep = [0, 5, 40, 100, 400, 800, 1200, 1700, 2100, 2600, 3000]


def dialogue():
    """Основной модуль (эта функция запускается при выборе гостиницы в главном меню), где модулируется поведение
    гостиницы и происходит выбор услуг, а также происходит проверка
    выбранной услуги для оказания её пользователю. Также тут запускается процесс сна где происходит восстановление
    параметров и повышение уровня"""
    while True:
        print(TOWN_MESSAGE + 'Вы находитесь в гостинице')
        ans = input(Style.RESET_ALL + MESSAGE_DIALOGUE + 'Здраствуйте. Воспользоваться нашими услугами вы можете за'
                    ' {} монет\n'
                    'Согласны?\n'
                    'Да ➔ 1\n'
                    'Нет ➔ 2\n'.format(price_sleep[hero.statistics['location']]))
        if ans == '1':
            if hero.parameter['gold'] >= price_sleep[hero.statistics['location']]:
                # тратятся деньги, причём индекс затрат равен параметру 'location' который берётся из статистики героя,
                # важно учесть что он начинается с единицы
                gold = price_sleep[hero.statistics['location']]
                hero.gold_spending(gold)
                sleep()
                information.goodbye()
                break
            else:
                information.not_enough_money()
        elif ans == '2':
            information.goodbye()
            break


def sleep():
    """Моделирует поведение сна, запускаются все функции, которые нужно запускать во время сна
    (повышение уровня и восстановление параметров). Этот модуль и есть полная эмуляция поведения сна.
    Его можно использовать без интефейса гостиницы"""
    test_lvl()
    recovery_all()


def recovery_all():
    """Восстановление потраченных параметров во время сна"""
    need_heal = hero.parameter['heart_full'] - hero.parameter['heart']
    hero.heart_recovery(need_heal)
    # если игрок маг то восстанавливается вся магия путём установления нового значения


def test_lvl():
    """Проверка опыта для поднятия уровня во время сна и поднятие уровня"""
    # если опыта больше чем в массиве с количеством опыта для следующего уровня, то уровень повышается
    # опыт не сбрасывается с повышением, позиция для нужного количества опыта соответствует текущему уровню игрока
    if hero.parameter['exp'] >= lvl_up.exp[hero.parameter['lvl']]:
        # повышение характеристик
        lvl_up.start()
        # повышение уровня навыка
        lvl_up.choice_skills()
