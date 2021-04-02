"""Тут находится функции казино для игроков"""


import hero_stats_great
import random
import start_game_great


def roulette():
    """Функция для рулетки, с самыми разными играми"""
    while 1:
        choice = input("Здраствуйте. Вы находитесь в казино. Выберите варианты игры\n"
                       "Золотой куш => 1 "
                       "Выбей уникальное оружие => 2 "
                       "Коробка зелья => 3 "
                       "Скачки => 4 "
                       "Победи толпу => 5 "
                       "Вернуться => 6\n")
        if choice == '1':
            print("Вы ставите золото, с вас его снимают, вам выпадает число золота, которое вы получаете")
            while 1:
                what = input("Играть => 1\n"
                             "Нет => 2\n")
                if what == '1':
                    gold = input("Приветствуем вас в игре золотой куш.\nВведите количество золота, которое вы ставите"
                                 "\n")
                    if gold.isdigit():
                        if hero_stats_great.parameter['gold'] >= gold:
                            hero_stats_great.gold_spending(gold)
                            print("Игра начинается")
                            print("Итак выпало...")
                            start_game_great.outlast()
                            how_much_gold = random.randint(0, gold*2)
                            hero_stats_great.gold_receive(how_much_gold)
                            start_game_great.outlast()
                        else:
                            print("У вас не хватает денег")
                            start_game_great.outlast()
                elif what == '2':
                    print("До свидания")
                    start_game_great.outlast()
                    break
                else:
                    pass
        elif choice == '2':
            ...
        elif choice == '6':
            break
        else:
            pass
