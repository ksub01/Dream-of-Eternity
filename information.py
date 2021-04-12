"""Тут расположены функции, используемые постоянно во всех местах игры"""

from progress.bar import FillingSquaresBar, FillingCirclesBar
from colorama import Fore, Style, init

import hero
import lvl_up


INVENTORY_MESSAGE = Fore.GREEN + Style.BRIGHT
DIE_MASSAGE = Fore.RED + Style.BRIGHT
HELP_MESSAGE = Fore.CYAN + Style.DIM
TOWN_MESSAGE = Style.DIM + Fore.LIGHTYELLOW_EX
MENU_TOWN_MASSAGE = Fore.LIGHTBLUE_EX


def pause():
    """Пауза после отображения текста, чтобы игрок успел прочитать"""
    input(Style.RESET_ALL + HELP_MESSAGE + 'Нажмите Enter\n')  # задержка для того, чтобы игрок мог прочитать


def goodbye():
    """Прощание с игроком в любой ситуации"""
    print(HELP_MESSAGE + 'До свидания')
    pause()


def end_game():
    print(DIE_MASSAGE + 'Вы проиграли. Озирис уничтожил мир, а Аркона пала.')


def not_enough_money():
    """Отобаражает, что у игрока не хватает денег"""
    print(INVENTORY_MESSAGE + "У вас не хватает денег")
    pause()


def progress_hp():
    """отображает количество здоровья в виде прогресс-бара"""
    s = '{}{}'.format(Fore.RED, '❤ ')
    bar = FillingSquaresBar(s, max=hero.parameter['heart_full'])
    bar.index = hero.parameter['heart']
    bar.update()
    print()


def progress_exp():
    """отображает количество здоровья в виде прогресс-бара"""
    s = '{}{}'.format(Fore.BLUE, '📖')
    lvl = hero.parameter['lvl']
    exp_for_next = lvl_up.exp[lvl] - lvl_up.exp[lvl-1]
    bar = FillingCirclesBar(s, max=exp_for_next)
    bar.index = hero.parameter['exp'] - lvl_up.exp[lvl-1]
    bar.update()
    print()


def parameters():
    """Отражение параметров героя в зависимости от выбранного класса героя"""
    print(Style.RESET_ALL + '─'*40)
    print(Fore.WHITE + Style.BRIGHT + "Уровень {}".format(hero.parameter['lvl']), end='  ')
    print(Fore.MAGENTA + hero.parameter['sign'])
    progress_hp()
    progress_exp()
    print(Fore.YELLOW + '🪙 {}'.format(hero.parameter['gold']), end='  ')
    if 'attack' in hero.parameter:
        print(Fore.BLUE + "⚔ {}".format(hero.parameter['attack']), end='  ')
    print(Fore.LIGHTBLUE_EX + Style.DIM + '👊 {}'.format(hero.parameter['force']), end='  ')
    print(Fore.LIGHTMAGENTA_EX + '🛡 {}'.format(hero.parameter['defence']), end='  ')
    print(Fore.GREEN + '🥾 {}'.format(hero.parameter['dexterity']), end='  ')
    print(Fore.LIGHTBLUE_EX + Style.DIM + '🧠 {}'.format(hero.parameter['wisdom']))
    print('─'*40 + '\n')


def if_lvl_up():
    """В городе отображает строку о возможности перейти на новый уровень. Значения берутся из массива опыта exp
    в lvl_up

    """
    if hero.parameter['exp'] >= lvl_up.exp[hero.parameter['lvl']]:
        print(INVENTORY_MESSAGE + "Поспите, чтобы повысить ваш уровень\n")


def town_places():
    """Постоянно высвечивается в городе для отображения мест, куда игрок может пойти"""
    print(TOWN_MESSAGE + 'Вы находитесь в городе Аркона, последнем оплоте человечества' + '\n')
    print('╍'*40)
    print(MENU_TOWN_MASSAGE +
          '🛖 ➔ 1\n'
          '🛌 ➔ 2\n'
          '🌲 ➔ 3\n'
          '🎲 ➔ 4\n'
          '🏡 ➔ 5')
    print('╍'*40)
