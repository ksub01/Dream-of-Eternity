"""Все функции для казино в городе"""


import hero
import random
import town
import information


def dialogue():
    """Функция для выбора миниигры в рулетке, в которую хочет сыграть игрок и запуска её"""
    while 1:
        # список игр для выбора
        choice = input("Здраствуйте. Вы находитесь в казино. Выберите варианты игры\n"
                       "Золотой куш => 1\n"
                       "Выбей уникальное оружие => 2 не готово\n"
                       "Коробка зелья => 3 не готово\n"
                       "Скачки => 4 не готово\n"
                       "Победи толпу => 5 не готово\n"
                       "Вернуться => 6\n\n")
        if choice == '1':
            print("Вы ставите золото, с вас его снимают, вам выпадает число золота, которое вы получаете")
            print('Число может выпасть в интервале от [0, 2n], где n ваше число')
            # запуск функции диалога с NPC, где выбирается игра, передаётся объект функции игры
            goodbye(gold_jackpot)
        elif choice == '2':
            ...
        elif choice == '6':
            break
        else:
            pass


def goodbye(func):
    """Запускает игру заданную в рулетке, то есть даёт полный интерфейс, взаимодёствее перед игрой
    Передаётся: функция игры, в котрую игрок хочет играть"""
    while 1:
        # выбор игрока: играть или нет
        what = input("Играть => 1\n"
                     "Нет => 2\n")
        if what == '1':
            # запуск функции игры
            func()
        elif what == '2':
            information.goodbye()
            # выход в главное меню казино
            break
        else:
            # игнорирование если такой цифры нет
            pass


def gold_jackpot():
    """Проводит первую миниигру в казино - золотой куш. Игрок ставить золото есу выпадает случайный результат
    из списка [0, его золото*2]"""
    # вводится количество золота, которое игрок ставит
    gold = input("Приветствуем вас в игре золотой куш.\nВведите количество золота, которое вы ставите"
                 "\n")
    if gold.isdigit():
        # проверка: хватает ли золота у игрока
        if hero.parameter['gold'] >= int(gold):
            # интование золота без ошибки т.к. известно, что это число
            gold = int(gold)
            hero.gold_spending(gold)
            print("Игра начинается\nИтак выпало...")
            information.pause()
            win_gold = random.randint(0, gold * 2)
            hero.gold_receive(win_gold)
            information.pause()
        else:
            town.not_enough_money()
    else:
        pass