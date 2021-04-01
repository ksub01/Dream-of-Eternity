"""Тут расположены функции, используемые постоянно во всех местах игры"""

import hero
import lvl_up


def pause():
    """Пауза после отображения текста, чтобы игрок успел прочитать"""
    input('Нажмите Enter\n')  # задержка для того, чтобы игрок мог прочитать


def goodbye():
    """Прощание с игроком в любой ситуации"""
    print("До свидания")
    pause()


def not_enough_money():
    """Отобаражает, что у игрока не хватает денег"""
    print("У вас не хватает денег")
    pause()


def parameters():
    """Отражение параметров героя в зависимости от выбранного класса героя"""
    print("Ваш класс: {}\nВаши характеристики:\nЗдоровье {}/{}".format(hero.parameter['name'],
                                                                       hero.parameter['heart'],
                                                                       hero.parameter['heart_full']))
    # отображение атаки, если герой не маг
    if 'attack' in hero.parameter:
        print("Атака {}".format(hero.parameter['attack']))
    # отображение магии, если она есть у героя
    if 'magic' in hero.parameter and 'magic_full' in hero.parameter and 'magic_force' in hero.parameter:
        print('Магия {}/{}\n'
              'Магическая сила {}'.format(hero.parameter['magic'], hero.parameter['full_magic'],
                                          hero.parameter['magic_force']))
    # отображение всех остальных характеристик, которыми обладают все
    print("Сила {}\n"
          "Броня {}\n"
          "Ловкость {}\n"
          "Мудрость {}\n"
          "Золото {}\n"
          "Опыт {}\n"
          "Уровень {}\n".format(hero.parameter['force'], hero.parameter['defence'],
                                hero.parameter['dexterity'], hero.parameter['wisdom'],
                                hero.parameter['gold'],
                                hero.parameter['exp'], hero.parameter['lvl']))


def if_lvl_up():
    """В городе отображает строку о возможности перейти на новый уровень. Значения берутся из массива опыта exp
    в lvl_up

    """
    if hero.parameter['exp'] >= lvl_up.exp[hero.parameter['lvl']]:
        print("Поспите, чтобы повысить ваш уровень\n")


def town_places():
    """Постоянно высвечивается в городе для отображения мест, куда игрок может пойти"""
    print("""Вы находитесь в городе Аркона, последнем городе человечества
Торговая лавка => 1
Отдохнуть в гостинице => 2
Пойти в лес на охоту => 3
Сыграть в рулетку => 4
Инвентарь = > 5
Получение заданий от основателей => 6
""")