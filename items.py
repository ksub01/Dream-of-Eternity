"""Модуль, в котором перечислены все предметы, которые может одеть игрок и функция открытия сундуков."""
import random
import inventory
import player
import information


def chest_open(num):
    """Функция открытия сундука, которая добавляет сундук в инвентарь героя. На вход функции подаётся уровень
    получаемого сунука. Функция при первых значениях добавляет предмет в инвентарь, а при меньших добавляет золото,
    количество которого зависит от уровня героя, причём предмет, доставаемый из сундука, находится в специальном словаре
    под номером, совпадающим с уровнем сундука. Для каждого из четырёх типов предметов своё ветвление
    Подаётся: уровень сундука"""
    # вычисление вероятности
    throw = random.randint(1, 25)
    if throw == 1:
        inventory.give_sword(rare_swords[num])
    elif throw == 2:
        inventory.give_armor(rare_armor[num])
    elif throw == 3:
        inventory.give_cloak(rare_cloak[num])
    elif throw == 4:
        inventory.give_ring(rare_ring[num])
    else:
        # игрок получает количество золота, помноженное на уровень, если предмета не выпало
        get_gold = throw * player.parameter['lvl']
        player.gold_receive(get_gold)
    # пауза при любом исходе
    information.pause()


"""Мечи, которые можно купить в магазине"""
swords_shop = {1: {'name': 'Сломанный меч', 'attack': 2, 'gold': 10, 'property': 'нет',
               'lvl': 1, 'upgrade': [i+2 for i in range(1, 101)], 'rare': 1, 'class': 'sword'},
               # попытка придумать улучшение
               2: {'name': 'Меч чести', 'attack': 2, 'gold': 150,
                   'property': 'При ударе, с вероятностью 20%, увеличивает вашу броню на время боя на 1', 'lvl': 1,
                   'class': 'sword'},
               3: {'name': 'Меч лести', 'attack': 0, 'gold': 75,
                   'property': 'Пока носите этот меч вы получаете с монстра на 20% золота больше', 'lvl': 1,
                   'class': 'sword'},
               4: {'name': 'Меч алхимика', 'attack': 0, 'gold': 100,
                   'property': 'При ударе может отравить противника. Яд наносит 10% урона от текущего здоровья монстра',
                   'lvl': 1, 'class': 'sword'},
               5: {'name': 'Меч повелителя гоблинов', 'attack': 5, 'gold': 1400,
                   'property': 'При ударе гоблин отдаёт вам своё золото, добавляя 10%\n'
                               'Наделяет своим опытом и увеличит вероятность выпадения сундука',
                   'lvl': 1, 'num': 5, 'class': 'sword'},
               }

"""Мечи, которые можно получить лишь из сундука, соответствующего уровня, кроме (500) он уникален"""
rare_swords = {500: {'name': 'Меч горя', 'attack': 10, 'gold': 0,
                     'property': 'При ударе восстанавливает здоровье на 10% от нанесённого урона',
                     'lvl': 1, 'class': 'sword'},
               1: {'name': 'Меч будущего героя',
                   'attack': 4, 'gold': 1000, 'property':
                   'Вы с 10% вероятностью игнорируете урон противника, сочетается с предметами, повышающими '
                   'эффективность лечения',
                   'lvl': 1, 'num': 1, 'class': 'sword'}
               }

"""Броня, которую можно купить в магазине"""
armor_shop = {1: {'name': 'Сломанные доспехи', 'defence': 1, 'gold': 350, 'property': 'нет',
                  'lvl': 1, 'class': 'armor'},
              2: {'name': 'Доспехи правосудия', 'defence': 2, 'gold': 550, 'property': 'нет',
                  'lvl': 1, 'class': 'armor'},
              3: {'name': 'Доспехи богатства', 'defence': 1, 'gold': 470, 'property':
                  'Увеличивает золото с монстров на 10%',
                  'lvl': 1, 'class': 'armor'},
              4: {'name': 'Доспехи лекаря', 'defence': 2, 'gold': 1200, 'property': 'Восстанавливает 1 здоровья за ход',
                  'lvl': 1, 'class': 'armor'},
              }

"""Броня, которую можно получить лишь из сундука, соответствующего уровня"""
rare_armor = {1: {'name': 'Броня солнца', 'defence': 2,
                  'gold': 1400, 'property':
                  'Возвращает 10% атаки противнику обратно', 'lvl': 1, 'class': 'armor'}}

"""Плащи, которые можно купить в магазине"""
cloak_shop = {1: {'name': 'Порванный плащ', 'gold': 350,
                  'property': 'Увеличивает количество восстанавливоемого здоровье на 50%',
                  'lvl': 1, 'class': 'cloak'},
              2: {'name': 'Плащ мудреца', 'gold': 700,
                  'property': 'Увеличивает количество опыта с монстра на 10%',
                  'lvl': 1, 'class': 'cloak'},
              3: {'name': 'Плащ защитника человечества', 'gold': 1000,
                  'property': 'С вероятностью 10% удар противника не причиняет вам вреда',
                  'lvl': 1, 'class': 'cloak'}
              }

"""Плащи, которые можно получить лишь из сундука, соответствующего уровня"""
rare_cloak = {1: {'name': 'Плащ регенерации', 'gold': 1200,
                  'property': 'В конце хода вы восстаналиваете 3 здоровья',
                  'lvl': 1, 'class': 'cloak'}}

"""Кольца которые можно купить в магазине"""
ring_shop = {1: {'name': 'Кольцо травника', 'gold': 650, 'property': 'Восстанавливает 10% здоровья один раз за бой',
                 'lvl': 1, 'class': 'ring'},
             2: {'name': 'Кольцо кладоискателя', 'gold': 750,
                 'property': 'Увеличивает вероятность получить сундук на 3%',
                 'lvl': 1, 'class': 'ring'},
             3: {'name': 'Кольцо настоящего мужщины', 'gold': 1200,
                 'property': 'в начале боя даёт вам 10 дополнительного здоровья',
                 'lvl': 1, 'class': 'ring'},
             }

"""Кольца, которые можно получить лишь из сундука, соответствующего уровня"""
rare_ring = {1: {'name': 'Кольцо болтуна', 'gold': 800,
                 'property': 'Вы получаете 10% скидку в магазине',
                 'lvl': 1, 'class': 'ring'}}
