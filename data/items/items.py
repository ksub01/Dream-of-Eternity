"""Модуль, в котором перечислены все предметы, которые может одеть игрок и функция открытия сундуков."""
# import sys
# sys.path.append('/home/dreamer/projects/DreamOfEternity')
import data.world.creature as world


feature = {'нет': {'description': 'нет'},
           'Ярость черепахи': {'description': 'При ударе, с вероятностью 20%, увеличивает вашу броню'
                                              ' на время боя на 1'},
           'Достойная награда': {'description': 'Увеличивает количество золота после боя'},
           'Повелитель гоблинов': {'description': 'При ударе гоблин отдаёт вам своё золото, добавляя 10%. '
                                                  'Наделяет своим опытом и увеличит вероятность выпадения сундука'},
           'Ловкач': {'description': 'Вы с 10% вероятностью игнорируете урон противника'},
           'Бешенство': {'description': 'Возвращает 10% атаки противнику обратно'},
           'Регенерация': {'description': 'В конце хода вы восстаналиваете 3 здоровья'},
           'Скидка': {'description': 'Вы получаете 10 процентную скидку в магазине'},
           'Живучесть': {'description': 'Увеличивает эффективность лечащих эффектов'},
           'Мудрец': {'description': 'Увеличивает количество опыта, которое игрок получает после боя'},
           'Уклонение': {'description': 'С вероятностью противник не попадет'},
           'Большая удача': {'description': 'Увеличивает вероятность получить сундук'},
           'Боевая медицина': {'description': 'В начале боя дает вам дополнительное здоровье, после боя эффект пропадат'},
           'Вампиризм': {'description': 'При ударе восстанавливает здоровье на 10% от нанесённого урона'},
           'Яд': {'description': 'При ударе отравляет противника'},
           }

active = {'нет': {'description': 'нет'},
          'Лечение': {'description': 'Восстанавливает здоровье'},


}

buy_sword = [{},
             dict(name='Сломанный меч', attack=2, cost=10, rare='🔵', lvl=1),
             dict(name='Меч чести', lvl=1, attack=2, cost=150, rare='🟡', property={'name': 'Ярость черепахи'}),
             dict(name='Меч лести', lvl=1, attack=0, cost=75, rare='🟡', property={'name': 'Достойная награда'}),
             dict(name='Меч алхимика', lvl=1, attack=0, cost=550, rare='🟡', property={'name': 'Яд'}),
             dict(name='Меч повелителя гоблинов', lvl=1, attack=5, cost=1400, rare='🔴',
                  property={'name': 'Повелитель гоблинов'}),
             ]

buy_armor = [{},
             dict(name='Сломанные доспехи', defence=1, cost=15, rare='🔵', lvl=1),
             dict(name='Доспехи правосудия', defence=2, cost=550, rare='🔵', lvl=1),
             dict(name='Доспехи богатства', defence=1, cost=470, rare='🔵', property={'name': 'Достойная награда'}, lvl=1),
             dict(name='Доспехи лекаря', defence=1, cost=800, rare='🔴', property={'name': 'Регенерация'}, lvl=1),
             ]
buy_cloak = [{},
             dict(name='Порванный плащ', cost=350, rare='🔵', property={'name': 'Живучесть'}, lvl=1),
             dict(name='Плащ мудреца', cost=700, rare='🔵', property={'name': 'Мудрец'}, lvl=1),
             dict(name='Плащ защитника человечества', cost=1000, rare='🔴', property={'name': 'Уклонение'}, lvl=1),
             ]
buy_ring = [{},
            dict(name='Кольцо травника', cost=650, rare='🔵', active={'name': 'Лечение'}, lvl=1),
            dict(name='Кольцо кладоискателя', cost=750, rare='🔵', property={'name': 'Большая удача'}, lvl=1),
            dict(name='Кольцо настоящего мужщины', cost=1200, rare='🔴', property={'name': 'Боевая медицина'}, lvl=1),
            ]


class Goods:
    def __init__(self):
        self.sword = buy_sword
        self.armor = buy_armor
        self.ring = buy_ring
        self.cloak = buy_cloak


def factory_buy_sword(name: str):
    """создает вещь, возвращает объект вещи"""
    ...
    # return world.Sword(buy_sword[name])


rare_sword = [{},
              dict(name='Меч горя', attack=10, cost=0, rare='🔵', property={'name': 'Вампиризм'}, lvl=1),
              ]


chest_swords = [None, dict(name='Меч будущего героя', attack=4, cost=1000, rare='⚪', property={'name': 'Ловкач'}, lvl=1,
                           )]
chest_armor = [None, dict(name='Броня солнца', defence=2, cost=1400, rare='⚪', property={'name': 'Бешенство'}, lvl=1,
                          )]
chest_cloak = [None, dict(name='Плащ регенерации', cost=1200, rare='⚪', property={'name': 'Регенерация'},
                          lvl=1)]
chest_ring = [None, dict(name='Кольцо болтуна', cost=1200, rare='⚪', property={'name': 'Скидка'},
                         lvl=1)]


class ChestThing:
    def __init__(self):
        self.sword = chest_swords
        self.armor = chest_armor
        self.cloak = chest_cloak
        self.ring = chest_ring


if __name__ == '__main__':
    hero = world.Overlord()
    print('Добавить Сломанный меч и Меч повелителя гоблинов')
    hero.inventory.get_thing(factory_buy_sword('Сломанный меч'))
    hero.inventory.get_thing(factory_buy_sword('Меч лести'))
    hero.inventory.get_thing(factory_buy_sword('Меч повелителя гоблинов'))
    print('Размер рюкзака')
    print(hero.inventory.size_bag())
    print('Отобразить всё содержимое сумки')
    hero.inventory.show_things()
    hero.inventory.equipment_show()
    hero.inventory.put_on()
    hero.inventory.equipment_show()
    hero.inventory.show_things()
    hero.inventory.take_off('sword')
    hero.inventory.equipment_show()
    hero.inventory.show_things()
    hero.inventory.display()