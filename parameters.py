"""Тут расположены функции, используемые постоянно во всех местах игры"""

import hero


def pause():
    """Пауза после отображения текста, чтобы игрок успел прочитать"""
    input('Нажмите Enter\n')  # задержка для того, чтобы игрок мог прочитать


def display_parameters():
    """Отражение параметров героя в зависимости от выбранного класса героя, появляется постоянно в городе и в бою"""
    print("Ваш класс: {}\n"
          "Ваши характеристики:\nЗдоровье {}/{}".format(hero.parameter['name'],
                                                        hero.parameter['heart'],
                                                        hero.parameter['heart_full']))
    # отображение атаки, если герой не маг
    if 'attack' in hero.parameter:
        print("Атака {}".format(hero.parameter['attack']))
    # отображение магии, если она есть у героя
    if ('magic' in hero.parameter and 'magic_full' in hero.parameter and
            'magic_force' in hero.parameter):
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


def goodbye():
    """Прощание с игроком в любой ситуации"""
    print("До свидания")
    pause()
