"""Все функции для казино в городе"""


import hero
import random
import information


def dialogue():
    """Функция для выбора миниигры в рулетке, в которую хочет сыграть игрок и запуска её"""
    choice = input("Здраствуйте. Вы находитесь в казино. Выберите варианты игры\n"
                   "Золотой куш => 1\n"
                   "Выбей уникальное оружие => 2 не готово\n"
                   "Коробка зелья => 3 не готово\n"
                   "Скачки => 4 не готово\n"
                   "Победи толпу => 5 не готово\n"
                   "Вернуться => 6\n\n")
    if choice == '1':
        print('Вы ставите золото, с вас его снимают, вам выпадает число золота, которое вы получаете'
              'Число может выпасть в интервале от [0, 2n], где n ваше число')
        start_game(gold_jackpot)


def start_game(game):
    """Запускает игру заданную в рулетке, то есть даёт полный интерфейс, взаимодёствее перед игрой
    Передаётся: функция игры, в которую игрок хочет играть"""
    while 1:
        what = input("Играть => 1\n"
                     "Нет => 2\n")
        if what == '1':
            game()
        elif what == '2':
            information.goodbye()
            break


def gold_jackpot():
    """Проводит первую миниигру в казино - золотой куш. Игрок ставить золото есу выпадает случайный результат
    из списка [0, его золото*2]"""
    # вводится количество золота, которое игрок ставит
    while 1:
        gold = input("Приветствуем вас в игре золотой куш.\n"
                     "Введите количество золота, которое вы ставите\n"
                     "Введите '0', если хотите уйти")
        if gold.isdigit() and gold != '0':
            if hero.parameter['gold'] >= int(gold):
                gold = int(gold)
                hero.gold_spending(gold)
                print('Игра начинается\n'
                      'Итак выпало...')
                information.pause()
                win_gold = random.randint(0, gold * 2)
                hero.gold_receive(win_gold)
                information.pause()
            else:
                information.not_enough_money()
        elif gold == '0':
            information.goodbye()
            break

