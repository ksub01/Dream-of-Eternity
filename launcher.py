"""Основной модуль запуска программы, подготовка к запуску, настройка и игровой цикл"""
import start
import parameters
import town
import blacksmith
import fight
import hotel
import sages
import casino
import inventory
import hero


def start_game():
    """Функции, включающиеся перед самым запуском игры"""
    start.parameters()
    start.prologue()
    start.guide()


def setting():
    """Загрузка и выбор класса перед началом игры"""
    ans = input("Хотите ли вы загрузить игру или хотите начать новую? Начать новую => 1 Загрузить => 2\n")
    if ans == '1':
        pass
    else:
        pass
    start.choice_class()


def playing_loop():
    """Основной цикл игры, с вычвелчивание города и боями"""

    while hero.parameter['heart'] > 0:
        """Основной цикл игры, город, место, где вы выбираете место куда пойти"""
        parameters.display_parameters()
        town.places()
        town.display_lvl_up()
        choice = input()
        if choice == '1':
            blacksmith.dialogue()
        elif choice == '2':
            hotel.dialogue()
        elif choice == '3':
            fight.dungeon()
        elif choice == '4':
            casino.dialogue()
        elif choice == '5':
            inventory.start_inventory()
        elif choice == '6':
            sages.dialogue()
        else:
            pass
    else:
        if hero.parameter['heart'] <= 0:
            print("Вы проиграли. Озирис уничтожил мир, а Аркона пала.")


start_game()
setting()
playing_loop()
