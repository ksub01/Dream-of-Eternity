"""Основной модуль запуска программы, подготовка к запуску, настройка и игровой цикл"""
from colorama import init
import pygame

import start
import information
import blacksmith
import fight
import hotel
import casino
import inventory
import hero

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
# сброс параметров после каждого вывода
pygame.init()
size = [700, 500]
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Dream of Eternity')
clock = pygame.time.Clock()
init(autoreset=True)
done = False


def start_game():
    """Функции, включающиеся перед самым запуском игры"""
    start.about()
    start.prologue()


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
    else:
        if not hero.alive():
            information.end_game()


if __name__ == '__main__':
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        start_game()
        setting()
        playing_loop()
        screen.fill(BLACK)
        pygame.display.flip()
        clock.tick(20)
        pygame.quit()