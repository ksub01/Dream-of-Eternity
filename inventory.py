from colorama import Fore, Style

import player
import items
import random
import information

# словарь в вещи заменяется словарём
equipment = {'sword': {},
             'armor': {}, 'cloak': {}, 'ring': {}}
# в инвентарь везде в список добавляются словари, кроме лута, в луте в словарь добавляется значение и количество
# в графе про сундуки записаны уровни сундуков
inventory = {'sword': [],
             'armor': [], 'cloak': [], 'ring': [], 'chest': []}


def size_inventory():
    """Возвращает 1, если в инвенторе, что - то есть и 0, если он пуст"""
    if len(inventory['sword'] + inventory['armor'] + inventory['cloak'] + inventory['ring']) != 0:
        return 1
    else:
        return 0


def size_equipment():
    """Есть ли у игрока надетые вещи?"""
    if equipment['sword'] != {} or equipment['armor'] != {} or equipment['cloak'] != {} or equipment['ring'] != {}:
        return 1
    else:
        return 0


def equipment_show():
    """Показывает надетые вещи на игроке. Ничего не принимает и не возвращает"""
    print(Fore.BLUE + '═'*40)
    if 'name' in equipment['sword']:
        print("🗡 «{}»\n⚔ ➔ {}\n"
              "➔"
              " {}\n".format(equipment['sword']['name'], equipment['sword']['attack'],
                             equipment['sword']['property']))
    else:
        print("{:6} {:5}\n".format('🗡', '❌'))
    if 'name' in equipment['armor']:
        print("🪖 «{}»\n🛡 ➔ {}\n"
              "➔"
              " {}\n".format(equipment['armor']['name'], equipment['armor']['defence'],
                             equipment['armor']['property']))
    else:
        print("{:6} {:5}\n".format('🛡', '❌'))
    if 'name' in equipment['cloak']:
        print("🧣 «{}»\n ➔"
              " {}\n".format(equipment['cloak']['name'], equipment['cloak']['property']))
    else:
        print("{:5} {:5}\n".format('🧣', '❌'))
    if 'name' in equipment['ring']:
        print("💍 «{}»\n"
              "➔"
              " {}\n".format(equipment['ring']['name'], equipment['ring']['property']))
    else:
        print("{:5} {:5}\n".format('💍', '❌'))
    print(Fore.BLUE + '═'*40)


def remove_thing(item, inventory_choice):
    """Удаляет данную вещь из данной ячейки инвентаря
    Принимает: словарь вещи и из какой ячейки инвенторя нужно удаалить вещь"""
    all_things = inventory['sword'] + inventory['armor'] + inventory['cloak'] + inventory['ring']
    for item_in_inventory in all_things:  # inventory - словарь для каждого типа со значением списка
        if item_in_inventory == item:
            inventory_choice.remove(item)
            break


def start_inventory():
    """Функция предоставляет основной интерфейс к инвентарю в городе"""
    # print(inventory)
    while True:
        equipment_show()
        show_things()
        # выбор варинта для взаимодействия с инвентарём
        choice = input("Надеть ➔ 1\n"
                       "Снять ➔ 2\n"
                       "Открыть сундуки ➔ 3\n"
                       "Вернуться ➔ 4\n")
        if choice == '1':
            put_on_thing()
        elif choice == '2':
            take_off()
        elif choice == '3':
            display_chest()
            if len(inventory['chest']) != 0:
                open_chest(int(input('Какой сундук открыть?')))
            else:
                print('У вас нет сундуков')
        elif choice == '4':
            break


def show_things():
    """Функция выводит все вещи игрока в инвентаре. Ничего не принимает и ничего не возвращает"""
    great_num = 10000000000000000000000
    # inventory - словарь со списками для каждого типа предметов
    all_things = inventory['sword'] + inventory['armor'] + inventory['cloak'] + inventory['ring']
    print('「Инвентарь 」\n')
    for (num, item) in zip(range(1, great_num), all_things):
        print(Fore.GREEN + '┅' * 40)
        if item['class'] == 'sword':
            print("🗡 " + Fore.GREEN + Style.DIM + "«{}»\n".format(item['name']) + Style.RESET_ALL + "⚔ ➔ {}\n"
                  "➔"
                  " {}\n".format(item['attack'],
                                 item['property']))
        elif item['class'] == 'armor':
            print("🪖 «{}»\n🛡 ➔ {}\n"
                  "➔"
                  " {}\n".format(item['name'], item['defence'],
                                 item['property']))
        elif item['class'] == 'cloak':
            print("🧣 «{}»\n ➔"
                  " {}\n".format(item['name'], item['property']))
        elif item['class'] == 'ring':
            print("💍 «{}»\n"
                  "➔"
                  " {}\n".format(item['name'], item['property']))
        print(Fore.GREEN + '┅' * 40)


def put_on_thing():
    """сложно. Функция снимает с игрока вещь, если на нём она есть, которую он выбрал и надевает новую которую
     он выберет,
    работает даже если нечего снимать"""
    if size_inventory():
        # thing - словарь оружия
        thing = choice_item()
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
        information.pause()


def choice_item():
    """сложно. Функция, которая находит вещь под выбранным номером и возвращает её словарь для обработки, ничего не
     принимает
    """
    great_num = 10000000000000
    thing = {}
    # отображение начинается с 1
    number = 0  # нужен для сохранения значения num между итерациями
    choice_number = int(input('Введите номер предмета в инвентаре, который нужно надеть\n'))
    if inventory['sword']:
        for (item, num) in zip(inventory['sword'], range(number, great_num)):
            if num == choice_number - 1:
                thing = inventory['sword'][num]
            else:
                pass
            number = num
    if inventory['armor']:
        for (item, num) in zip(inventory['armor'], range(number + 1, great_num)):
            if num == choice_number - 1:
                thing = inventory['armor'][num]
            else:
                pass
            number = num
    if inventory['cloak']:
        for item, num in zip(inventory['cloak'], range(number + 1, great_num)):
            if num == choice_number - 1:
                thing = inventory['cloak'][num]
            else:
                pass
            number = num
    if inventory['ring']:
        for item, num in zip(inventory['ring'], range(number + 1, great_num)):
            if num == choice_number - 1:
                thing = inventory['ring'][number]
            else:
                pass
    if thing:
        return thing
    else:
        print('Произошла ошибка')


def put_on_sword(sword_for_put_on):
    """Функция надевает на игрока переданный меч, снимает старый и ничего не возвращает"""
    if equipment['sword']:
        take_off_sword()
    if 'attack' in sword_for_put_on:
        # игрок надевает вещь и получает бонус к атаке
        player.attack_receive(sword_for_put_on['attack'])
    equipment['sword'] = sword_for_put_on
    remove_thing(sword_for_put_on, inventory['sword'])


def put_on_armor(armor_for_put_on):
    """Функция надевает на игрока переданную броню, снимает старую и ничего не возвращает"""
    if 'name' in equipment['armor'] and equipment['armor']['name'] != '':
        take_off_armor()
    if 'defence' in armor_for_put_on:
        player.defence_receive(armor_for_put_on['defence'])
    equipment['armor'] = armor_for_put_on
    remove_thing(armor_for_put_on, inventory['armor'])


def put_on_cloak(cloak_for_put_on):
    """Функция надевает на игрока переданный плащ, снимает старый и ничего не возвращает"""
    if 'name' in equipment['cloak'] and equipment['cloak']['name'] != '':
        take_off_cloak()
    equipment['cloak'] = cloak_for_put_on
    remove_thing(cloak_for_put_on, inventory['cloak'])


def put_on_ring(ring_for_put_on):
    """Функция надевает на игрока переданное кольцо, снимает старое и ничего не возвращает"""
    if 'name' in equipment['ring'] and equipment['ring']['name'] != '':
        take_off_ring()
    equipment['ring'] = ring_for_put_on
    remove_thing(ring_for_put_on, inventory['ring'])


def take_off():
    """Запускается для снятие вещи. Функция снятия вещей из одетого героя в городе. Ничего не принимает и не
     возвращает. Меняет надетые вещи героя"""
    if size_equipment():
        choice1 = input('Что снять? Меч -> 1 Броню -> 2 Плащ -> 3 Кольцо -> 4\n')
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
        information.pause()


def take_off_sword():
    """Функция снятия меча в инвентаре"""
    if 'name' in equipment['sword'] and equipment['sword']['name'] != '':
        give_sword(equipment['sword'])
        player.attack_lose(equipment['sword']['attack'])
        # equipment содержит словари надетых вещей
        equipment['sword'] = {}


def take_off_armor():
    """Функция снятия брони в инвентаре"""
    if 'name' in equipment['armor'] and equipment['armor']['name'] != '':
        give_armor(equipment['armor'])
        player.defence_lose(equipment['armor']['defence'])
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
    # inventory содержит списки под заданной позицией в словаре
    inventory['sword'].append(sword)
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
        player.attack_lose(equipment['sword']['attack'])
        equipment['sword'] = {}
    print('Вы потеряли надетый меч')


def lose_armor():
    """Функция потери надетой брони"""
    if 'name' in equipment['armor'] and equipment['armor']['name'] != '':
        player.defence_lose(equipment['armor']['defence'])
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


def give_thing(item):
    """Функций, которая определяет, к какой конкретно функции обратится для получения вещи. Передаётся словарь оружия.
    Распадается на 4"""
    if item['class'] == 'sword':
        give_sword(item)
    elif item['class'] == 'armor':
        give_armor(item)
    elif item['class'] == 'ring':
        give_ring(item)
    elif item['class'] == 'cloak':
        give_cloak(item)


def display_chest():
    """Отображает все сундуки, что есть у игрока, использует заглушку, костыль для отображения. ничего не принимает
    и не возвращает, просто отображает"""
    great_num = 10000000000000000000000
    if len(inventory['chest']) != 0:
        for (num, weapon) in zip(range(1, great_num), inventory['chest']):
            print('{} Сундук {} уровня'.format(num, weapon))
    else:
        print('У вас нет сундуков')
        information.pause()


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


def open_chest(chest_num):
    """Происходит открытие данного сундука в инвенторе и удаления его из инвентаря. Передаётся номер сундука
    и не возвращается ничего"""
    great_num = 10000000000000000000000
    for (num, chest) in zip(range(1, great_num), inventory['chest']):
        if chest_num == num:
            items.chest_open(num)
            inventory['chest'].remove(num)
            break
        else:
            pass
    else:
        print('Данного сундука нет в инвентаре')
        information.pause()
