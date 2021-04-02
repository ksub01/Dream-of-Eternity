"""Основной модуль запуска программы, начальное обучение, город и весь игровой процесс"""


import hero_stats_great
import hotel_great
import start_game_great
import roulette_great
import basics_fight
import blacksmith_grate
import inventory_hero_great
import mission_battle_after_great
import music_no_yet

music_no_yet.music_play()  # запуск музыки

start_game_great.prologue()  # показ версии с задержкой и сюжет


while 1:
    """Согласны или несогласны вы на обучения в игре, если да,
     то выбор класса, также загрузка сохранённой игры"""
    what_is = input("\nХотите пройти обучение? Да => 1 Нет => 2 Загрузить игру => 3\n")
    if what_is == '1':
        start_game_great.guide()  # гайд
        start_game_great.choice_of_class()  # выбор класса
        break
    elif what_is == '2':
        start_game_great.choice_of_class()
        break
    elif what_is == '3':
        print('Сохранения пока не работают')
        start_game_great.outlast()
    else:
        pass


while hero_stats_great.parameter['heart'] > 0:
    """Основной цикл игры, город, место, где вы выбираете место куда пойти"""
    start_game_great.parameters()  # отображение параметров героя
    start_game_great.start_town()  # показ мест, что есть в городе
    b = input()
    if b == '1':
        blacksmith_grate.blacksmith()
    elif b == '2':
        hotel_great.hotel()
    elif b == '3':
        basics_fight.forest()
    elif b == '4':
        roulette_great.roulette()
    elif b == '5':
        inventory_hero_great.main_inventory()
    elif b == '6':
        mission_battle_after_great.task()
    else:
        pass
else:
    if hero_stats_great.parameter['heart'] <= 0:
        print("Вы проиграли. Озирис уничтожил мир, а Аркона пала.")
