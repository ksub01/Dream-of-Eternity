"""Все функции для казино в городе"""

from colorama import Fore, Style, init

import hero
import random
import information

TOWN_MESSAGE = Style.DIM + Fore.LIGHTYELLOW_EX
MESSAGE_DIALOGUE = Fore.GREEN
HELP_MESSAGE = Fore.CYAN + Style.DIM

init(autoreset=True)


def dialogue():
    """Функция для выбора миниигры в рулетке, в которую хочет сыграть игрок и запуска её"""
    while True:
        choice = input(Style.RESET_ALL + MESSAGE_DIALOGUE + 'Здраствуйте. Вы находитесь в казино.'
                       ' Выберите варианты игры\n'
                       'Золотой куш ➔ 1\n'
                       'Выйти ➔ 2\n')
        if choice == '1':
            print(HELP_MESSAGE + 'Вы указываете золото, с вас его снимают, вам выпадает число золота, которое вы'
                  ' получаете\n'
                  'Число может выпасть в интервале от [0, 2n], где n ваше число')
            start_game(gold_jackpot)
            break
        elif choice == '2':
            break


def start_game(game):
    """Запускает игру заданную в рулетке, то есть даёт полный интерфейс, взаимодёствее перед игрой
    Передаётся: функция игры, в которую игрок хочет играть"""
    while True:
        what = input(HELP_MESSAGE + 'Играть => 1\n' + 'Нет => 2\n')
        if what == '1':
            game()
        elif what == '2':
            information.goodbye()
            break


def gold_jackpot():
    """Проводит первую миниигру в казино - золотой куш. Игрок ставить золото есу выпадает случайный результат
    из списка [0, его золото*2]"""
    # вводится количество золота, которое игрок ставит
    while True:
        gold = input(Style.RESET_ALL + MESSAGE_DIALOGUE + 'Приветствуем вас в игре Золотой куш.\n'
                     'Введите количество золота, которое вы ставите\n'
                     'Выход ➔ 0\n')
        if gold.isdigit() and gold != '0':
            if hero.parameter['gold'] >= int(gold):
                gold = int(gold)
                hero.gold_spending(gold)
                print(HELP_MESSAGE + 'Игра начинается\n'
                      'Итак выпало...')
                information.pause()
                win_gold = random.randint(0, gold * 2)
                print(Fore.YELLOW + '*' + str(win_gold) + '*')
                hero.gold_receive(win_gold)
                information.pause()
            else:
                information.not_enough_money()
        elif gold == '0':
            information.goodbye()
            break

