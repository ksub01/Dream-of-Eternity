"""Покупка, продажа и улучшение оружия"""


import hero_stats_great
import inventory_hero_great
import items_and_chest_great
import start_game_great


def chosen_item_in_inventory(item, discount):
    """Проверяет, хватает ли у игрока денег, если да, то добавляет данный предмет в инвентарь. Функция принимает
    предмет, золото и модификатор"""
    if hero_stats_great.parameter['gold'] >= int(item['gold'] * discount):
        hero_stats_great.gold_spending(int(item['gold'] * discount))
        inventory_hero_great.give_ring(item)
        print('Спасибо за покупку\n')
        start_game_great.outlast()
    else:
        print('У вас не хватает денег')
        start_game_great.outlast()


def shop_discount():
    """Действуют предметы, влияющие на цену"""
    discount = 1  # модификатор цен
    if inventory_hero_great.equipment['ring'] != {} and inventory_hero_great.equipment['ring']['name'] ==\
            'Кольцо болтуна':
        discount -= 0.1
    return discount


def blacksmith():
    """Основной интерфейс кузнеца"""
    while 1:
        discount = shop_discount()
        choice_division = display_shop()
        if choice_division == '1' and hero_stats_great.parameter['name'] == 'Повелитель':  # выбор зависит от класса
            display_shop_sword(discount)
            print('Купить -> 1\nУйти -> 2\n')
            choice = input()
            if choice == '1':
                print('Какой из мечей?')
                choice_sword = input()
                if choice_sword.isdigit():
                    buy_sword_in_shop(choice_sword, discount)
                else:
                    pass
            else:
                print('Простите')
                start_game_great.outlast()
                pass
        elif choice_division == '2':
            display_shop_armor(discount)
            print('Купить -> 1\nУйти -> 2\n')
            choice = input()
            if choice == '1':
                print('Какой из доспехов?')
                choice_armor = input()
                if choice_armor.isdigit():
                    buy_armor_in_shop(choice_armor, discount)
                else:
                    pass
            else:
                print('Простите')
                start_game_great.outlast()
                pass
        elif choice_division == '3':
            display_shop_cloak(discount)
            print('Купить -> 1\nУйти -> 2\n')
            choice = input()
            if choice == '1':
                print('Какой из плащей?')
                choice_cloak = input()
                if choice_cloak.isdigit():
                    buy_cloak_in_shop(choice_cloak, discount)
                else:
                    pass
            else:
                print('Простите')
                start_game_great.outlast()
                pass
        elif choice_division == '4':
            display_shop_ring(discount)
            choice_shop = input('Купить -> 1\nУйти -> 2\n\n')
            if choice_shop == '1':
                print('Какое из колец?')
                choice_ring = input()
                if choice_ring.isdigit():
                    buy_ring_in_shop(choice_ring, discount)
                else:
                    pass
            else:
                print('Простите')
                start_game_great.outlast()
                pass
        elif choice_division == '7':
            break


def display_shop():
    """Отображает отделы магазина, запрашивает и возвращает выбранный отдел"""
    h = input("Здраствуй, хочешь чего нибудь купить?\n"
              "Оружие => 1\n"
              "Броня => 2\n"
              "Плащи => 3\n"
              "Кольца => 4\n"
              "Продать вещи => 5\n"
              "Зелья => 6\n"
              "Вернуться => 7\n")
    return h


def display_shop_sword(discount):
    """Отображает мечи доступные в магазине соответствующие уровню"""
    for key in items_and_chest_great.swords_shop:
        if hero_stats_great.parameter['lvl'] >= items_and_chest_great.swords_shop[key]['lvl']:
            print('{} <{}> Атака ⟨{}⟩ Цена *{}* \n'
                  'Особое свойство <<{}>>\nУровень {}\n'
                  ''.format(key, items_and_chest_great.swords_shop[key]['name'],
                            items_and_chest_great.swords_shop[key]['attack'],
                            int(items_and_chest_great.swords_shop[key]['gold'] * discount),
                            items_and_chest_great.swords_shop[key]['property'],
                            items_and_chest_great.swords_shop[key]['lvl']))


def display_shop_armor(discount):
    """Отображает броню доступную в магазине соответствующую уровню"""
    for key in items_and_chest_great.armor_shop:
        if hero_stats_great.parameter['lvl'] >= items_and_chest_great.armor_shop[key]['lvl']:
            print('{} <{}> Броня ⟨{}⟩ Цена *{}* \n'
                  'Особое свойство <<{}>>\nУровень {}\n'
                  ''.format(key, items_and_chest_great.armor_shop[key]['name'],
                            items_and_chest_great.armor_shop[key]['defence'],
                            int(items_and_chest_great.armor_shop[key]['gold'] * discount),
                            items_and_chest_great.armor_shop[key]['property'],
                            items_and_chest_great.armor_shop[key]['lvl']))


def display_shop_cloak(discount):
    """Отображает мечи доступные в магазине соответствующие уровню"""
    for key in items_and_chest_great.cloak_shop:
        if hero_stats_great.parameter['lvl'] >= items_and_chest_great.cloak_shop[key]['lvl']:
            print('{} <{}> Цена *{}* \n'
                  'Особое свойство <<{}>>\nУровень {}\n'
                  ''.format(key, items_and_chest_great.cloak_shop[key]['name'],
                            int(items_and_chest_great.cloak_shop[key]['gold'] * discount),
                            items_and_chest_great.cloak_shop[key]['property'],
                            items_and_chest_great.cloak_shop[key]['lvl']))


def display_shop_ring(discount):
    """Отображает кольца доступные в магазине соответствующие уровню"""
    for key in items_and_chest_great.ring_shop:
        # проверка, чтобы отображались предметы не выше уровня героя
        if hero_stats_great.parameter['lvl'] >= items_and_chest_great.ring_shop[key]['lvl']:
            print('{} <{}> Цена *{}* \n'
                  'Особое свойство <<{}>>\nУровень {}\n'
                  ''.format(key, items_and_chest_great.ring_shop[key]['name'],
                            int(items_and_chest_great.ring_shop[key]['gold'] * discount),
                            items_and_chest_great.ring_shop[key]['property'],
                            items_and_chest_great.ring_shop[key]['lvl']))


def buy_sword_in_shop(choice_sword, discount):
    """Покупка меча под номером указанным в атрибуте в словаре, и переданный модификатор цены"""
    choice_sword = int(choice_sword)
    for sword_number in items_and_chest_great.swords_shop:
        if sword_number == choice_sword:
            print('Ваше золото: {}'.format(hero_stats_great.parameter['gold']))
            print('Вы точно хотите купить <{}>?\nАтака ⟨{}⟩ Цена *{}*\n'
                  'Особое свойство: <<{}>>\nУровень {}\n'
                  'Да -> 1 Нет -> 2\n'.format(items_and_chest_great.swords_shop[sword_number]['name'],
                                              items_and_chest_great.swords_shop[sword_number]['attack'],
                                              int(items_and_chest_great.swords_shop[sword_number]['gold'] * discount),
                                              items_and_chest_great.swords_shop[sword_number]['property'],
                                              items_and_chest_great.swords_shop[sword_number]['lvl']))
            choice = int(input())
            if choice == 1:
                chosen_item_in_inventory(items_and_chest_great.swords_shop[sword_number], discount)
            break


def buy_armor_in_shop(choice_armor, discount):
    """Покупка брони под номером указанным в атрибуте в словаре, и переданный модификатор цены"""
    choice_armor = int(choice_armor)
    for armor_number in items_and_chest_great.armor_shop:
        if armor_number == choice_armor:
            print('Ваше золото: {}'.format(hero_stats_great.parameter['gold']))
            print('Вы точно хотите купить <{}>?\nБроня ⟨{}⟩ Цена *{}*\n'
                  'Особое свойство: <<{}>>\nУровень {}\n'
                  'Да -> 1 Нет -> 2\n'.format(items_and_chest_great.armor_shop[armor_number]['name'],
                                              items_and_chest_great.armor_shop[armor_number]['defence'],
                                              int(items_and_chest_great.armor_shop[armor_number]['gold'] * discount),
                                              items_and_chest_great.armor_shop[armor_number]['property'],
                                              items_and_chest_great.armor_shop[armor_number]['lvl']))
            choice = int(input())
            if choice == 1:
                chosen_item_in_inventory(items_and_chest_great.armor_shop[armor_number], discount)
            break


def buy_cloak_in_shop(choice_cloak, discount):
    """Покупка плаща под номером указанным в атрибуте в словаре, и переданный модификатор цены"""
    choice_cloak = int(choice_cloak)
    for cloak_number in items_and_chest_great.cloak_shop:
        if cloak_number == choice_cloak:
            print('Ваше золото: {}'.format(hero_stats_great.parameter['gold']))
            print('Вы точно хотите купить <{}>?\nЦена *{}*\n'
                  'Особое свойство: <<{}>>\nУровень {}\n'
                  'Да -> 1 Нет -> 2\n'.format(items_and_chest_great.cloak_shop[cloak_number]['name'],
                                              int(items_and_chest_great.cloak_shop[cloak_number]['gold'] * discount),
                                              items_and_chest_great.cloak_shop[cloak_number]['property'],
                                              items_and_chest_great.cloak_shop[cloak_number]['lvl']))
            choice = int(input())
            if choice == 1:
                chosen_item_in_inventory(items_and_chest_great.cloak_shop[cloak_number], discount)


def buy_ring_in_shop(choice_ring, discount):
    """Покупка кольца под номером указанным в атрибуте в словаре, и переданный модификатор цены"""
    choice_ring = int(choice_ring)
    for ring_number in items_and_chest_great.ring_shop:
        if ring_number == choice_ring:
            print('Ваше золото: {}'.format(hero_stats_great.parameter['gold']))
            print('Вы точно хотите купить <{}>?\nЦена *{}*\n'
                  'Особое свойство: <<{}>>\nУровень {}\n'
                  'Да -> 1 Нет -> 2\n'.format(items_and_chest_great.ring_shop[ring_number]['name'],
                                              int(items_and_chest_great.ring_shop[ring_number]['gold'] * discount),
                                              items_and_chest_great.ring_shop[ring_number]['property'],
                                              items_and_chest_great.ring_shop[ring_number]['lvl']))
            choice = input()
            if choice == '1':
                chosen_item_in_inventory(items_and_chest_great.ring_shop[ring_number], discount)
