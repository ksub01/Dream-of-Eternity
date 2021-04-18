"""Основной модуль запуска программы, подготовка к запуску, настройка и игровой цикл"""
from colorama import init


import start
import information
import blacksmith
import fight
import hotel
import casino
import inventory
from player import heroes


def start_game():
    """Функции, включающиеся перед самым запуском игры"""
    start.about()
    start.prologue()


def setting():
    """Выбор класса перед началом игры"""
    start.choice_class()


def playing_loop():
    """Основной цикл игры, с действиями внутри города и боями"""
    while heroes.alive():
        print('Текущее имя' + heroes.target)
        # проблема выбора имени и выбора из трехклассов, а не из одного
        # проблема с присвоением и изменением экземпляров классов в других модулях
        heroes.parameters()
        information.town_places()
        information.if_lvl_up()
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
    else:
        if not heroes.alive():
            information.end_game()


if __name__ == '__main__':
    start_game()
    setting()
    playing_loop()
