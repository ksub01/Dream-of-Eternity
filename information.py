"""Тут расположены функции, используемые постоянно во всех местах игры"""

import hero
import lvl_up
from colorama import Fore, Back, Style, init


# сброс параметров после каждого вывода
init(autoreset=True)


def pause():
    """Пауза после отображения текста, чтобы игрок успел прочитать"""
    input(Fore.CYAN + Style.DIM + 'Нажмите Enter\n')  # задержка для того, чтобы игрок мог прочитать
    print(Style.RESET_ALL)


def goodbye():
    """Прощание с игроком в любой ситуации"""
    print(Fore.CYAN + Style.DIM + 'До свидания')
    pause()


def end_game():
    print(Fore.RED + Style.BRIGHT + 'Вы проиграли. Озирис уничтожил мир, а Аркона пала.')


def not_enough_money():
    """Отобаражает, что у игрока не хватает денег"""
    print(Fore.GREEN + "У вас не хватает денег")
    pause()


def parameters():
    """Отражение параметров героя в зависимости от выбранного класса героя"""
    print(Fore.MAGENTA + "Ваш класс: {}".format(hero.parameter['name']))
    print(Fore.WHITE + Style.BRIGHT + "Уровень {}".format(hero.parameter['lvl']), end='  ')
    print(Fore.RED + Style.BRIGHT + "❤ {}/{}".format(hero.parameter['heart'],
                                                            hero.parameter['heart_full']), end='  ')
    print(Fore.YELLOW + '🪙 {}'.format(hero.parameter['gold']), end='  ')

    if 'attack' in hero.parameter:
        print(Fore.BLUE + "⚔ {}".format(hero.parameter['attack']), end='  ')
    if 'magic' in hero.parameter:
        print(Fore.BLUE + 'Магия {}/{}'.format(hero.parameter['magic'],
                                                              hero.parameter['full_magic']))
        print(Fore.CYAN + 'Магическая сила {}'.format(hero.parameter['magic_force']))
    print(Fore.LIGHTBLUE_EX + Style.DIM + '👊 {}'.format(hero.parameter['force']), end='  ')
    print(Fore.LIGHTMAGENTA_EX + '🛡 {}'.format(hero.parameter['defence']), end='  ')
    print(Fore.GREEN + '🥾 {}'.format(hero.parameter['dexterity']), end='  ')
    print(Fore.LIGHTBLUE_EX + Style.DIM + '🧠 {}'.format(hero.parameter['wisdom']), end='  ')
    print(Fore.GREEN + '📖 {}\n'.format(hero.parameter['exp']), end='')


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