import hero_stats_great
import items_and_chest_great
import start_game_great
import random

# словарь заменяется словарём
equipment = {'sword': {},
             'armor': {}, 'cloak': {}, 'ring': {}}
# в инвентарь везде в список добавляются словари, кроме лута, в луте в словарь добавляется значение
inventory = {'sword': [],
             'armor': [], 'cloak': [], 'ring': [], 'chest': [], 'loot': {}}

# сюда перед началом боя будут собираться все вещи, которые будут использоваться в бою
item_for_use = []


def inventory_not_empty():
    """Возвращает 1, если инвентарь не пуст и 0, если он пуст"""
    if len(inventory['sword'] + inventory['armor'] + inventory['cloak'] + inventory['ring']) != 0:
        return 1
    else:
        return 0


def equipment_show():
    """Показывает надетые вещи на игроке. Ничего не принимает и не возвращает"""
    if 'name' in equipment['sword'] and 'attack' in equipment['sword']:
        print("<{}>\nАтака -> {}\n"
              "Уникальный эффект ->"
              " {}\n".format(equipment['sword']['name'], equipment['sword']['attack'],
                             equipment['sword']['property']))
    else:
        print("Меч: нет\n")
    if 'name' in equipment['armor'] and 'defence' in equipment['armor']:
        print("<{}>\nБроня -> {}\n"
              "Уникальный эффект ->"
              " {}\n".format(equipment['armor']['name'], equipment['armor']['defence'],
                             equipment['armor']['property']))
    else:
        print("Броня: нет\n")
    if 'name' in equipment['cloak']:
        print("{}\nУникальный эффект ->"
              " {}\n".format(equipment['cloak']['name'], equipment['cloak']['property']))
    else:
        print("Плащ: нет\n")
    if 'name' in equipment['ring']:
        print("{}\nУникальный эффект ->"
              " {}\n".format(equipment['ring']['name'], equipment['ring']['property']))
    else:
        print("Кольцо: нет\n\n")


def remove_item_in_inventory(item, inventory_choice):
    """Удаляет данную вещь из данной ячейки инвентаря"""
    for item_in_inventory in inventory:
        if item_in_inventory == item:
            inventory_choice.remove(item)
        else:
            print('Произошла ошибка')
            pass


def main_inventory():
    """Функция предоставляет основной интерфейс к инвентарю в городе"""
    while 1:
        equipment_show()
        inventory_show()
        choice_inventory = input("Надеть => 1\n"
                                 "Снять => 2\n"
                                 "Открыть сундуки => 3\n"
                                 "Вещи, выпавшие с монстров => 4\n"
                                 "Вернуться => 5\n")
        if choice_inventory == '1':
            put_on_a_thing()
        elif choice_inventory == '2':
            take_off_in_inventory()
        elif choice_inventory == '3':
            display_chest()
            if len(inventory['chest']) != 0:
                inventory_open_chest(int(input('Какой сундук открыть?')))
        elif choice_inventory == '4':
            display_monsters_items()
        elif choice_inventory == '5':
            break
        else:
            pass


def inventory_show():
    """Функция выводит все вещи игрока в инвентаре. Ничего не принимает и ничего не возвращает"""
    great_num = 10000000000000000000000
    all_items = inventory['sword'] + inventory['armor'] + inventory['cloak'] + inventory['ring']
    print("```Инвентарь```\n")
    for (num, item) in zip(range(1, great_num), all_items):
        if item['class'] == 'sword':
            print("{} <<{}>>\nАтака -> {}\n"
                  "Уникальный эффект ->"
                  " {}\n".format(num, item['name'], item['attack'], item['property']))
        elif item['class'] == 'armor':
            print("{} <{}>\nБроня -> {}\n"
                  "Уникальный эффект ->"
                  " {}\n".format(num, item['name'], item['defence'], item['property']))
        elif item['class'] == 'cloak':
            print("{} <{}>\nУникальный эффект ->"
                  " {}\n".format(num, item['name'], item['property']))
        elif item['class'] == 'ring':
            print("{} <{}>\nУникальный эффект ->"
                  " {}\n".format(num, item['name'], item['property']))


def put_on_a_thing():
    """Функция снимает с игрока вещь, которую он выбрал и надевает новую которую он выберет, работает даже если ничего
    не надеть"""
    if len(inventory['sword'] + inventory['armor'] + inventory['cloak'] + inventory['ring']) != 0:
        thing = choice_item_in_inventory_for_buy()
        if thing['class'] == 'sword':
            put_on_sword(thing)
        elif thing['class'] == 'armor':
            put_on_armor(thing)
        elif thing['class'] == 'cloak':
            put_on_cloak(thing)
        elif thing['class'] == 'ring':
            put_on_ring(thing)
        else:
            pass
    else:
        print('Нечего надеть')
        start_game_great.outlast()


def choice_item_in_inventory_for_buy():
    """Функция, которая находит вещь под выбранным номером и возвращает её словарь для обработки, ничего не принимает
    """
    great_num = 10000000000000000000000
    thing = {}
    choice_number = int(input('Введите номер предмета в инвентаре, который нужно надеть\n'))
    num = 1  # счётчик отображения вещей, меняется с каждой вещью, должен совпась в выбранной цифрой
    if inventory['sword']:
        for (item, number) in zip((inventory['sword'], range(1, great_num))):
            # number нужен для верной вещи в верной ячейке
            if num == choice_number:
                thing = inventory['armor'][number]
            else:
                pass
            num += 1
    if inventory['armor']:
        for (item, number) in zip((inventory['armor'], range(1, great_num))):
            if num == choice_number:
                thing = inventory['armor'][number]
            else:
                pass
            num += 1
    if inventory['cloak']:
        for (item, number) in zip((inventory['cloak'], range(1, great_num))):
            if num == choice_number:
                thing = inventory['cloak'][number]
            else:
                pass
            num += 1
    if inventory['ring']:
        for (item, number) in zip((inventory['ring'], range(1, great_num))):
            if num == choice_number:
                thing = inventory['ring'][number]
            else:
                pass
            num += 1
    return thing


def put_on_sword(sword_for_put_on):
    """Функция надевает на игрока переданный меч, снимает старый и ничего не возвращает"""
    if 'name' in equipment['sword'] and equipment['sword']['name'] != '':
        take_off_sword()
    if 'attack' in sword_for_put_on:
        hero_stats_great.attack_receive(sword_for_put_on['attack'])
    equipment['sword'] = sword_for_put_on
    remove_item_in_inventory(sword_for_put_on, inventory['sword'])


def put_on_armor(armor_for_put_on):
    """Функция надевает на игрока переданную броню, снимает старую и ничего не возвращает"""
    if 'name' in equipment['armor'] and equipment['armor']['name'] != '':
        take_off_armor()
    if 'defence' in armor_for_put_on:
        hero_stats_great.receive_defence(armor_for_put_on['defence'])
    equipment['armor'] = armor_for_put_on
    remove_item_in_inventory(armor_for_put_on, inventory['armor'])


def put_on_cloak(cloak_for_put_on):
    """Функция надевает на игрока переданный плащ, снимает старый и ничего не возвращает"""
    if 'name' in equipment['cloak'] and equipment['cloak']['name'] != '':
        take_off_cloak()
    equipment['cloak'] = cloak_for_put_on
    remove_item_in_inventory(cloak_for_put_on, inventory['cloak'])


def put_on_ring(ring_for_put_on):
    """Функция надевает на игрока переданное кольцо, снимает старое и ничего не возвращает"""
    if 'name' in equipment['ring'] and equipment['ring']['name'] != '':
        take_off_ring()
    equipment['ring'] = ring_for_put_on
    remove_item_in_inventory(ring_for_put_on, inventory['ring'])


def take_off_in_inventory():
    """Запускается для снятие вещи. Функция снятия вещей в инвентаре героя в городе. Ничего не принимает и не
     возвращает. Меняет инвентарь героя"""
    if inventory_not_empty():
        choice1 = input('Что снять? Меч -> 1 Броню -> 2 Плащ -> 3 Кольцо -> 4')
        if choice1 == '1':
            take_off_sword()
        elif choice1 == '2':
            take_off_armor()
        elif choice1 == '3':
            take_off_cloak()
        elif choice1 == '4':
            take_off_ring()
        else:
            pass
    else:
        print('Снять нечего')
        start_game_great.outlast()


def take_off_sword():
    """Функция снятия меча в инвентаре"""
    if 'name' in equipment['sword'] and equipment['sword']['name'] != '':
        give_sword(equipment['sword'])
        hero_stats_great.lose_attack(equipment['sword']['attack'])
        equipment['sword'] = {}


def take_off_armor():
    """Функция снятия брони в инвентаре"""
    if 'name' in equipment['armor'] and equipment['armor']['name'] != '':
        give_armor(equipment['armor'])
        hero_stats_great.lose_defence(equipment['armor']['defence'])
        equipment['armor'] = {}


def take_off_cloak():
    """Функция снятия плаща в инвентаре"""
    if 'name' in equipment['cloak'] and equipment['cloak']['name'] != '':
        give_cloak(equipment['armor'])
        equipment['cloak'] = {}


def take_off_ring():
    """Функция снятия кольца в инвентаре"""
    if 'name' in equipment['ring'] and equipment['ring']['name'] != '':
        give_ring(equipment['ring'])
        equipment['ring'] = {}


def give_sword(sword):
    """Функция, которая добавляет меч из аргумента функции, предсавленного словарём в твой инвентарь.
    Сделать ли отдельную функцию для каждого типа одежды"""
    inventory['cloak'].append(sword)
    print('Вы получили {}'.format(sword['name']))


def give_armor(armor):
    """Функция, которая добавляет броню из аргумента функции, предсавленного словарём в твой инвентарь"""
    inventory['armor'].append(armor)
    print('Вы получили {}'.format(armor['name']))


def give_cloak(cloak):
    """Функция, которая добавляет плащ из аргумента функции, предсавленного словарём в твой инвентарь"""
    inventory['cloak'].append(cloak)
    print('Вы получили {}'.format(cloak['name']))


def give_ring(ring):
    """Функция, которая добавляет кольцо из аргумента функции, предсавленного словарём в твой инвентарь"""
    inventory['ring'].append(ring)
    print('Вы получили {}'.format(ring['name']))


def lose_sword():
    """Герой теряет надетый меч"""
    if 'name' in equipment['sword'] and equipment['sword']['name'] != '':
        hero_stats_great.lose_attack(equipment['sword']['attack'])
        equipment['sword'] = {}
    print('Вы потеряли надетый меч')


def lose_armor():
    """Функция потери надетой брони"""
    if 'name' in equipment['armor'] and equipment['armor']['name'] != '':
        hero_stats_great.lose_defence(equipment['armor']['defence'])
        equipment['armor'] = {}
        print('Вы потеряли вашу броню')
    print('Вы потеряли надетую броню')


def lose_cloak():
    """Герой теряет надетый плащ"""
    equipment['cloak'] = {}
    print('Вы потеряли надетый плащ')


def lose_ring():
    """Герой теряет надетое кольцо"""
    equipment['ring'] = {}
    print('Вы потеряли надетое кольцо')


def display_monsters_items():
    """Просто отображает все ваши вещи, выпавшие с монстра. Ничего не принимает и не возвращает. Просто отображает"""
    if inventory['loot'] != {}:
        for weapon in inventory['loot']:
            print('{} количество *{}'.format(weapon, inventory['loot'][weapon]))
        start_game_great.outlast()
    else:
        print('У вас нет вещей, выпавших с монстров')
        start_game_great.outlast()


def give_item(item, num):
    """Вы получаете num предметов с именем item в свой инвентарь"""
    if item in inventory['loot']:
        inventory['loot'][item] += num
        print('Вы получаете {} - в количестве {} штук'.format(item, num))
    else:
        inventory['loot'][item] = 1


def spend_items(items, value):
    """Этой функции мы задаём предмет с монстра и значение которое нужно изнять у игрока, предмет - строка, ключ словаря
    Возвращает 1 если удалось потратить и 0 если нет"""
    # проверка, есть ли предмет в инвентаре и извлечение значения
    if items in inventory['loot'] and inventory['loot'][items] >= value:
        inventory['loot'][items] -= value
        print('Вы отдали {} - {}'.format(items, value))
        return 1
    else:
        return 0


def display_chest():
    """Отображает все сундуки, что есть у игрока, использует заглушку, костыль для отображения. ничего не принимает
    и не возвращает, просто отображает"""
    great_num = 10000000000000000000000
    if len(inventory['chest']) != 0:
        for (num, weapon) in zip(range(1, great_num), inventory['chest']):
            print('{} Сундук {} уровня'.format(num, weapon))
    else:
        print('У вас нет сундуков')
        start_game_great.outlast()


def give_chest(num1, num2, lvl_chest, chance_chest):
    """Функция, которая определяет, получает ли игрок сундук или нет. Аргументы: первая цифра для определения
    вероятности из второй цифры, например num1 = 1, num2 = 100, вероятность выпадения сундука будет равна 1%,
    ещё один пример: num1 = 3, num2 = 4 вероятность выпадения сундука - 75%. Второй аргументы - уровень получаемого
    сундука. Третиё аргумент - равен количеству дополнительных процентов выпадения сундука, которые есть у игрока.
    Из - за последнего аргумента функция в основном применяется для опеределения вероятности из 100"""
    chest_drop = random.randint(1, num2) + chance_chest
    if chest_drop <= num1:
        print('Вы получили сундук {} уровня, он добавлен в ваш инвентарь'.format(lvl_chest))
        inventory['chest'].append(lvl_chest)
    else:
        pass


def inventory_open_chest(chest_num):
    """Происходит открытие данного сундука в инвенторе и удаления его из инвентаря. Передаётся номер сундука
    и не возвращается ничего"""
    great_num = 10000000000000000000000
    for (num, chest) in zip(range(1, great_num), inventory['chest']):
        if chest_num == num:
            items_and_chest_great.chest_open(num)
            inventory['chest'].remove(num)
            break
        else:
            pass
    else:
        print('Данного сундука нет в инвентаре')
        start_game_great.outlast()


def append_items_for_using():
    """Во время боя отображает предметы преднозначенные для использования"""
    using_items = ['Кольцо травника']
    for choice_item in (equipment['sword'], equipment['armor'], equipment['cloak'], equipment['ring']):
        if choice_item in using_items:
            item_for_use.append(choice_item)
