"""Основной модуль запуска программы, подготовка к запуску, настройка и игровой цикл"""
import data.world.world as world

if __name__ == '__main__':
    Game = world.Game()
    Game.start()
