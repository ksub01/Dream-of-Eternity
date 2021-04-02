"""Модуль, описывающий то, как происходит восстановление здоровья героя и маны"""


import hero_stats_great
import lvl_up_great
import start_game_great

# золота для лечения при разных локациях
money = [0, 5, 40, 100, 400, 800, 1200, 1700, 2100, 2600, 3000]


def hotel():
    """Основной модуль, где происходит восстановление здоровья героя"""
    while 1:
        k = input("Вы находитесь в гостинице\n"
                  "Здраствуйте. Воспользоваться нашими услугами вы можете за {} монет\n"
                  "Согласны?\n"
                  "Да => 1\n"
                  # количество золота для восстановления в зависимости от локации
                  "Нет => 2\n\n".format(money[hero_stats_great.statistics['location']]))
        if k == '1':
            if hero_stats_great.parameter['gold'] >= money[hero_stats_great.statistics['location']]:
                hero_stats_great.gold_spending(money[hero_stats_great.statistics['location']])
                # повышение уровня пока игрок спит, если хватает опыта
                if hero_stats_great.parameter['exp'] >= lvl_up_great.exp[hero_stats_great.parameter['lvl'] - 1]:
                    lvl_up_great.lvl_up()
                    lvl_up_great.skills()
                hero_stats_great.heart_new(hero_stats_great.parameter['heart_full'])
                if 'magic' in hero_stats_great.parameter:
                    hero_stats_great.magic_recovery(hero_stats_great.parameter['magic_full'])
                print('Спасибо, что отдохнули у нас')
                start_game_great.outlast()
                break
            else:
                print("У вас не хватает денег")
                start_game_great.outlast()
        elif k == '2':
            print("До свидания\n")
            start_game_great.outlast()
            break
        else:
            pass
