"""Тут расположены функции, используемые постоянно во всех местах игры"""

import hero
import lvl_up
from colorama import Fore, Style

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


def parameters():
    """Отражение параметров героя в зависимости от выбранного класса героя"""
    print()
    print(Fore.WHITE + Style.BRIGHT + "Уровень {}".format(hero.parameter['lvl']), end='  ')
    print(Fore.MAGENTA + hero.parameter['sign'], end='  ')
    print(Fore.RED + Style.BRIGHT + "❤ {}/{}".format(hero.parameter['heart'],
                                                     hero.parameter['heart_full']), end='  ')
    print(Fore.YELLOW + '🪙 {}'.format(hero.parameter['gold']), end='  ')
    if 'attack' in hero.parameter:
        print(Fore.BLUE + "⚔ {}".format(hero.parameter['attack']), end='  ')
    print(Fore.LIGHTBLUE_EX + Style.DIM + '👊 {}'.format(hero.parameter['force']), end='  ')
    print(Fore.LIGHTMAGENTA_EX + '🛡 {}'.format(hero.parameter['defence']), end='  ')
    print(Fore.GREEN + '🥾 {}'.format(hero.parameter['dexterity']), end='  ')
    print(Fore.LIGHTBLUE_EX + Style.DIM + '🧠 {}'.format(hero.parameter['wisdom']), end='  ')
    print(Fore.GREEN + '📖 {}\n'.format(hero.parameter['exp']))


def if_lvl_up():
    """В городе отображает строку о возможности перейти на новый уровень. Значения берутся из массива опыта exp
    в lvl_up

    """
    if hero.parameter['exp'] >= lvl_up.exp[hero.parameter['lvl']]:
        print(INVENTORY_MESSAGE + "Поспите, чтобы повысить ваш уровень\n")


def town_places():
    """Постоянно высвечивается в городе для отображения мест, куда игрок может пойти"""
    print(TOWN_MESSAGE + 'Вы находитесь в городе Аркона, последнем городе человечества\n')
    print(MENU_TOWN_MASSAGE +
          'Торговая лавка => 1\n'
          'Отдохнуть в гостинице => 2\n'
          'Пойти в лес на охоту => 3\n'
          'Сыграть в рулетку => 4\n'
          'Инвентарь = > 5')
