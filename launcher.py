"""Основной модуль запуска программы, подготовка к запуску, настройка и игровой цикл"""
import start
import information
import blacksmith
import fight
import hotel
import sages
import casino
import inventory
import hero


def start_game():
    """Функции, включающиеся перед самым запуском игры"""
    start.about()
    start.prologue()
    start.guide()


def setting():
    """Выбор класса перед началом игры"""
    start.choice_class()


def playing_loop():
    """Основной цикл игры, с действиями внутри города и боями"""
    while hero.alive():
        information.parameters()
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
        elif choice == '6':
            sages.dialogue()
        else:
            pass
    else:
        if not hero.alive():
            print("Вы проиграли. Озирис уничтожил мир, а Аркона пала.")


if __name__ == '__main__':
    start_game()
    setting()
    playing_loop()
