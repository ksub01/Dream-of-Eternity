"""Модуль, описывающий то, как происходит восстановление здоровья героя и маны, а также повышение уровня (поднятие
навыков и скилла) при приходе героя в гостиницу"""

import hero
import lvl_up
import parameters
import town

# количество золота для лечения в разных локациях
price_for_sleep_in_different_location = [0, 5, 40, 100, 400, 800, 1200, 1700, 2100, 2600, 3000]


def dialogue():
    """Основной модуль (эта функция запускается при выборе гостиницы в главном меню), где модулируется поведение
    гостиницы и происходит выбор услуг, а также происходит проверка
    выбранной услуги для оказания её пользователю. Также тут запускается процесс сна где происходит восстановление
    параметров и повышение уровня"""
    while 1:
        # выбор услуг
        k = input("Вы находитесь в гостинице\n"
                  "Здраствуйте. Воспользоваться нашими услугами вы можете за {} монет\n"
                  "Согласны?\n"
                  "Да => 1\n"
                  # количество золота для восстановления в зависимости от локации
                  "Нет => 2\n\n".format(price_for_sleep_in_different_location[hero.statistics['location']]))
        if k == '1':
            # если денег в инвентаре меньше чем цена за сон
            if (hero.parameter['gold'] >=
                    price_for_sleep_in_different_location[hero.statistics['location']]):
                # тратятся деньги, причём индекс затрат равен параметру 'location' который берётся из статистики героя,
                # важно учесть что он начинается с единицы
                hero.gold_spending(
                    price_for_sleep_in_different_location[hero.statistics['location']])
                # запускается сон - основной процесс в котором происходит лечение и поднятие уровня
                sleep()
                parameters.goodbye()
                # выход из цикла гостиницы и возвращение в город
                break
            else:
                town.not_enough_money()
        elif k == '2':
            parameters.goodbye()
            # выход из цикла гостиницы и возвращение в город
            break
        else:
            # пропуск при неправильной цифре
            pass


def sleep():
    """Моделирует поведение сна, запускаются все функции, которые нужно запускать во время сна
    (повышение уровня и восстановление параметров). Этот модуль и есть полная эмуляция поведения сна.
    Его можно использовать без интефейса гостиницы"""
    test_lvl()
    recovery_all()


def recovery_all():
    """Восстановление потраченных параметров во время сна"""
    hero.heart_new(hero.parameter['heart_full'])
    # если игрок маг то восстанавливается вся магия путём установления нового значения
    if 'magic' in hero.parameter:
        hero.magic_recovery(hero.parameter['magic_full'])


def test_lvl():
    """Проверка опыта для поднятия уровня во время сна и поднятие уровня"""
    # если опыта больше чем в массиве с количеством опыта для следующего уровня, то уровень повышается
    # опыт не сбрасывается с повышением, позиция для нужного количества опыта соответствует текущему уровню игрока
    if hero.parameter['exp'] >= lvl_up.exp[hero.parameter['lvl']]:
        # повышение характеристик
        lvl_up.start()
        # повышение уровня навыка
        lvl_up.choice_skills()
