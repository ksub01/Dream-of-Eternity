"""Тут расположены функции, используемые постоянно во всех местах игры"""

from progress.bar import FillingSquaresBar, FillingCirclesBar
from colorama import Fore, Style, init

from player import heroes


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


def if_lvl_up():
    """В городе отображает строку о возможности перейти на новый уровень. Значения берутся из массива опыта exp
    в lvl_up"""
    if heroes.exp >= heroes.exp_to_lvl[heroes.lvl]:
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
