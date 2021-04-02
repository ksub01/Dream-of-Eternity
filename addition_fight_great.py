"""Дополнительные функции для свойств предметов во время боя"""


import random
import start_game_great
import hero_stats_great
import inventory_hero_great
import monsters_great


def dragon_time():
    """Функция которая выдаёт множитель силы монстров при входе в данж. В дальнейшем будет переделана, чтобы
    работала долго для защиты от абуза, возвращает множитель события, 1 - если ничего, 2 - если что-то"""
    if random.randint(1, 10) == 1:
        print('!' * 40)
        print('Озирис делится своей силой с лесом Смерти')
        print('!' * 40)
        start_game_great.outlast()
        return 2
    else:
        print('Сегодня лес спокоен и угрозы Озириса нет')
        start_game_great.outlast()
        return 1


def calculation_heal_power():
    """Рассчитывает heal power для лечащих предметов, перед запуском основной функции"""
    heal_power = 1
    if inventory_hero_great.equipment['cloak'] != {} and inventory_hero_great.equipment['cloak']['name']\
            == 'Порванный плащ':
        heal_power += 0.5
    return heal_power


def hero_defence_after_fight(name):
    """Действия, которые происходят перед самим боем, при встрече монстра"""
    if name['name'] == 'Гоблин Убийца':
        hero_stats_great.parameter['defence'] = 0
    if inventory_hero_great.equipment['ring'] != {} and inventory_hero_great.equipment['ring']['name'] == \
            'Кольцо начтоящего мужчины':
        hero_stats_great.heart_recovery(10)


def after_damage_hero_in_monster(damage):
    """Модификация урона предметами и скилами перед ударом. Возвращает урон"""
    if 'Длань господа' in hero_stats_great.active:
        damage = damage * hero_stats_great.nav['Длань господа'][1][hero_stats_great.nav['Длань господа'][0]]
    if 'Демонический облик' in hero_stats_great.active:
        damage = damage * 2
    return damage


def after_damage_monster_in_hero(damage):
    """Функция возвращает урон нанесённый монстром герою, модифицируя его, возвращает урон наносимый монстром"""
    if (inventory_hero_great.equipment['cloak'] != {} and inventory_hero_great.equipment['cloak']['name']
            == 'Плащ защитника человечества'):
        b = random.randint(1, 10)
        if b == 1:
            damage = 0
            print('Плащ защитника человечества нейтрализовал урон, нанесённый монстром')
    return damage


def past_damage_hero_in_monster(name, damage_hero_in_monster):
    """Функция проявляет действие многих предметов после удара героя. В том числе лечение, повышение защиты или
    мгновенная смерть монстра, вампиризм. Ничего не возвращает, передаём словарь мостра и урон героя монстру"""
    # переменная регистрирует эффективность предметов восстанавливающих здоровье на основе других предметов
    heal_power = calculation_heal_power()

    if inventory_hero_great.equipment['sword'] != {} and inventory_hero_great.equipment['sword']['name'] == 'Меч чести':
        # повышение защиты в бою после каждой атаки, для этого как раз защита и сохранялась
        if random.randint(1, 10) <= 2:
            hero_stats_great.receive_defence(1)

    if inventory_hero_great.equipment['sword'] != {} and inventory_hero_great.equipment['sword']['name'] ==\
            'Меч алхимика':
        print('Противник отравлен')
        monsters_great.monster_spend_heart(name, int(name['heart'] * 0.1))

    if inventory_hero_great.equipment['sword'] != {} and inventory_hero_great.equipment['sword']['name'] ==\
            'Меч повелителя гоблинов' and name['names'].find("Гоблин") >= 0:
        monsters_great.monster_heart_new(name, 0)
        print('Гоблин усмирён')

    if inventory_hero_great.equipment['sword'] != {} and inventory_hero_great.equipment['sword']['name'] == "Меч горя":
        hero_stats_great.heart_recovery(int(damage_hero_in_monster * 0.1 * heal_power))

    if 'Демонический облик' in hero_stats_great.active:
        hero_stats_great.heart_spend(int(damage_hero_in_monster * hero_stats_great.nav['Демонический облик'][1][
                                             hero_stats_great.nav['Демонический облик'][0]] / 100))


def past_damage_monster_in_hero(name):
    """Функция проявляет действие многих предметов и способностей после удара монстра. В том числе отражение урона
    обратно в монстра, лечение монстра, кража монстром, отравление игрока. Ничего не возвращает"""
    heal_power = calculation_heal_power()

    if name['name'] == 'Гоблин Шаман':
        monsters_great.monster_recovery_heart(name, 2)

    if inventory_hero_great.equipment['armor'] != {} and inventory_hero_great.equipment['armor']['name']\
            == 'Броня солнца':
        monsters_great.monster_spend_heart(name, int(name['attack'] * 0.1))

    if name['name'] == 'Змея Варганиса':
        # змея отравляет на 20 процентов, перед каждым ударом
        hero_stats_great.heart_spend(int(hero_stats_great.parameter['heart'] * 0.2))

    if name['name'] == 'Култист Озириса':
        # культист крадёт одну из четырёх экипированных вещей
        item = random.randint(1, 12)
        if item == 1:
            inventory_hero_great.lose_sword()
            print('Монстр украл ваш меч')
        elif item == 2:
            inventory_hero_great.lose_armor()
            print('Монстр украл ваши доспехи')
        elif item == 3:
            inventory_hero_great.lose_cloak()
            print('Монстр украл ваш плащ')
        elif item == 4:
            inventory_hero_great.lose_ring()
            print('Монстр украл ваше кольцо')
        else:
            print('Попытка кражи не удалась')
            pass
    if inventory_hero_great.equipment['armor'] != {} and inventory_hero_great.equipment['armor']['name'] ==\
            'Доспехи лекаря':
        hero_stats_great.heart_recovery(int(1 * heal_power))

    if inventory_hero_great.equipment['cloak'] != {} and inventory_hero_great.equipment['cloak']['name']\
            == 'Плащ регенерации':
        hero_stats_great.heart_recovery(int(3 * heal_power))


def addition_reward(name):
    """Обрабатывает статистику перед получением наград и делает дополнительные действия: например выдаёт награду за
    1000 убитых монстров, запускает уникальные события, получает словарь"""
    if name['name'] == 'Гоблин Воин':
        hero_stats_great.war_goblin_bonus()


def after_gold_and_exp__monster(monster):
    """Функция, которая вычисляет ваше золото исходя из предметов и вероятность сундука по 100 бальной шкале
     из предметов и возвращает кортеж"""
    # эти переменные меняются и возвращаются в функции
    # всё вычисляется в процентах
    quantity_gold = 0
    probability_chest = 0
    quantity_exp = 0

    if inventory_hero_great.equipment['sword'] != {} and inventory_hero_great.equipment['sword']['name'] == 'Меч лести':
        quantity_gold += 20
        print('Количество золото увеличено на 20%')

    if inventory_hero_great.equipment['armor'] != {} and inventory_hero_great.equipment['armor']['name'] ==\
            'Доспехи богатства':
        quantity_gold += 10
        print('Количество золото увеличено на 10%')

    if inventory_hero_great.equipment['sword'] != {} and inventory_hero_great.equipment['sword']['name'] ==\
            'Меч повелителя гоблинов':
        probability_chest += 5
        quantity_gold += 10

    if inventory_hero_great.equipment['ring'] != {} and inventory_hero_great.equipment['ring']['name']\
            == 'Кольцо кладоискателя':
        probability_chest += 3

    if inventory_hero_great.equipment['cloak'] != {} and inventory_hero_great.equipment['cloak']['name']\
            == 'Плащ мудреца':
        quantity_exp += 10

    # вычисляет количество золото через проценты
    coefficient_gold = int(1 + (quantity_gold/100))
    coefficient_exp = int(1 + (quantity_exp/100))
    loot(monster)
    return coefficient_gold, probability_chest, coefficient_exp


def loot(name_monster):
    """Функция выдаёт вам лут исходя из имени монстра и добавляет его в инвентарь"""
    if random.randint(1, 2) == 1 and name_monster['name'] == 'Гоблин Воин':
        inventory_hero_great.give_item('Сердце гоблина война', 1)
