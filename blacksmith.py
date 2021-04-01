"""Покупка, продажа и улучшение оружия"""
import hero
import inventory
import items
import information


def get_item(item, discount):
    """Проверяет, хватает ли у игрока денег, если да, то добавляет данный предмет в инвентарь.
    Принимает: предмет и модификатор цены"""
    if hero.parameter['gold'] >= int(item['gold'] * discount):
        hero.gold_spending(int(item['gold'] * discount))
        inventory.give_thing(item)
        print('Спасибо за покупку\n')
        information.pause()
    else:
        information.not_enough_money()


def calc_discount():
    """Действуют предметы, влияющие на цену. Функция возвращает этот модификатор"""
    discount = 1  # модификатор цен в процентах
    if inventory.equipment['ring'] != {} and inventory.equipment['ring']['name'] ==\
            'Кольцо болтуна':
        discount -= 0.1
    return discount


def dialogue():
    """Основной интерфейс кузнеца"""
    while 1:
        discount = calc_discount()  # в десятых долях от целой части
        choice_division = showcase()
        # выбор зависит от класса
        if choice_division == '1' and hero.parameter['name'] == 'Повелитель':
            display_sword(discount)
            print('Купить -> 1\nУйти -> 2\n')
            choice = input()
            if choice == '1':
                print('Какой из мечей?')
                choice_sword = input()
                if choice_sword.isdigit():
                    buy_sword(choice_sword, discount)
                else:
                    pass
            else:
                print('Простите')
                information.pause()
                pass
        elif choice_division == '2':
            display_armor(discount)
            print('Купить -> 1\nУйти -> 2\n')
            choice = input()
            if choice == '1':
                print('Какой из доспехов?')
                choice_armor = input()
                if choice_armor.isdigit():
                    buy_armor(choice_armor, discount)
                else:
                    pass
            else:
                print('Простите')
                information.pause()
                pass
        elif choice_division == '3':
            display_cloak(discount)
            print('Купить -> 1\nУйти -> 2\n')
            choice = input()
            if choice == '1':
                print('Какой из плащей?')
                choice_cloak = input()
                if choice_cloak.isdigit():
                    buy_cloak(choice_cloak, discount)
                else:
                    pass
            else:
                print('Простите')
                information.pause()
                pass
        elif choice_division == '4':
            display_ring(discount)
            choice_shop = input('Купить -> 1\nУйти -> 2\n\n')
            if choice_shop == '1':
                print('Какое из колец?')
                choice_ring = input()
                if choice_ring.isdigit():
                    buy_ring(choice_ring, discount)
                else:
                    pass
            else:
                print('Простите')
                information.pause()
                pass
        elif choice_division == '7':
            break


def showcase():
    """Отображает отделы магазина, запрашивает и возвращает выбранный отдел"""
    choice = input(
        "Здраствуй, хочешь чего нибудь купить?\n"
        "Оружие => 1\n"
        "Броня => 2\n"
        "Плащи => 3\n"
        "Кольца => 4\n"
        "Продать вещи => 5\n"
        "Зелья => 6\n"
        "Вернуться => 7\n")
    return choice


def display_sword(discount):
    """Отображает мечи доступные в магазине соответствующие уровню"""
    for key in items.swords_shop:
        if hero.parameter['lvl'] >= items.swords_shop[key]['lvl']:
            print('{} <{}> Атака <{}> Цена *{}* \n'
                  'Особое свойство <<{}>>\nУровень {}\n'
                  ''.format(key, items.swords_shop[key]['name'],
                            items.swords_shop[key]['attack'],
                            int(items.swords_shop[key]['gold'] * discount),
                            items.swords_shop[key]['property'],
                            items.swords_shop[key]['lvl']))


def display_armor(discount):
    """Отображает броню доступную в магазине соответствующую уровню"""
    for key in items.armor_shop:
        if hero.parameter['lvl'] >= items.armor_shop[key]['lvl']:
            print('{} <{}> Броня <{}> Цена *{}* \n'
                  'Особое свойство <<{}>>\nУровень {}\n'
                  ''.format(key, items.armor_shop[key]['name'],
                            items.armor_shop[key]['defence'],
                            int(items.armor_shop[key]['gold'] * discount),
                            items.armor_shop[key]['property'],
                            items.armor_shop[key]['lvl']))


def display_cloak(discount):
    """Отображает мечи доступные в магазине соответствующие уровню"""
    for key in items.cloak_shop:
        if hero.parameter['lvl'] >= items.cloak_shop[key]['lvl']:
            print('{} <{}> Цена *{}* \n'
                  'Особое свойство <<{}>>\nУровень {}\n'
                  ''.format(key, items.cloak_shop[key]['name'],
                            int(items.cloak_shop[key]['gold'] * discount),
                            items.cloak_shop[key]['property'],
                            items.cloak_shop[key]['lvl']))


def display_ring(discount):
    """Отображает кольца доступные в магазине соответствующие уровню"""
    for key in items.ring_shop:
        # проверка, чтобы отображались предметы не выше уровня героя
        if hero.parameter['lvl'] >= items.ring_shop[key]['lvl']:
            print('{} <{}> Цена *{}* \n'
                  'Особое свойство <<{}>>\nУровень {}\n'
                  ''.format(key, items.ring_shop[key]['name'],
                            int(items.ring_shop[key]['gold'] * discount),
                            items.ring_shop[key]['property'],
                            items.ring_shop[key]['lvl']))


def buy_sword(choice_sword, discount):
    """Покупка меча под номером указанным в атрибуте в словаре, и переданный модификатор цены"""
    choice_sword = int(choice_sword)
    for sword_number in items.swords_shop:
        if sword_number == choice_sword:
            print('Ваше золото: {}'.format(hero.parameter['gold']))
            print('Вы точно хотите купить <{}>?\nАтака <{}> Цена *{}*\n'
                  'Особое свойство: <<{}>>\nУровень {}\n'
                  'Да -> 1 Нет -> 2\n'.format(items.swords_shop[sword_number]['name'],
                                              items.swords_shop[sword_number]['attack'],
                                              int(items.swords_shop[sword_number]['gold'] * discount),
                                              items.swords_shop[sword_number]['property'],
                                              items.swords_shop[sword_number]['lvl']))
            choice = int(input())
            if choice == 1:
                get_item(items.swords_shop[sword_number], discount)
            break


def buy_armor(choice_armor, discount):
    """Покупка брони под номером указанным в атрибуте в словаре, и переданный модификатор цены"""
    choice_armor = int(choice_armor)
    for armor_number in items.armor_shop:
        if armor_number == choice_armor:
            print('Ваше золото: {}'.format(hero.parameter['gold']))
            print('Вы точно хотите купить <{}>?\nБроня <{}> Цена *{}*\n'
                  'Особое свойство: <<{}>>\nУровень {}\n'
                  'Да -> 1 Нет -> 2\n'.format(items.armor_shop[armor_number]['name'],
                                              items.armor_shop[armor_number]['defence'],
                                              int(items.armor_shop[armor_number]['gold'] * discount),
                                              items.armor_shop[armor_number]['property'],
                                              items.armor_shop[armor_number]['lvl']))
            choice = int(input())
            if choice == 1:
                get_item(items.armor_shop[armor_number], discount)
            break


def buy_cloak(choice_cloak, discount):
    """Покупка плаща под номером указанным в атрибуте в словаре, и переданный модификатор цены"""
    choice_cloak = int(choice_cloak)
    for cloak_number in items.cloak_shop:
        if cloak_number == choice_cloak:
            print('Ваше золото: {}'.format(hero.parameter['gold']))
            print('Вы точно хотите купить <{}>?\nЦена *{}*\n'
                  'Особое свойство: <<{}>>\nУровень {}\n'
                  'Да -> 1 Нет -> 2\n'.format(items.cloak_shop[cloak_number]['name'],
                                              int(items.cloak_shop[cloak_number]['gold'] * discount),
                                              items.cloak_shop[cloak_number]['property'],
                                              items.cloak_shop[cloak_number]['lvl']))
            choice = int(input())
            if choice == 1:
                get_item(items.cloak_shop[cloak_number], discount)


def buy_ring(choice_ring, discount):
    """Покупка кольца под номером указанным в атрибуте в словаре, и переданный модификатор цены"""
    choice_ring = int(choice_ring)
    for ring_number in items.ring_shop:
        if ring_number == choice_ring:
            print('Ваше золото: {}'.format(hero.parameter['gold']))
            print('Вы точно хотите купить <{}>?\nЦена *{}*\n'
                  'Особое свойство: <<{}>>\nУровень {}\n'
                  'Да -> 1 Нет -> 2\n'.format(items.ring_shop[ring_number]['name'],
                                              int(items.ring_shop[ring_number]['gold'] * discount),
                                              items.ring_shop[ring_number]['property'],
                                              items.ring_shop[ring_number]['lvl']))
            choice = input()
            if choice == '1':
                get_item(items.ring_shop[ring_number], discount)
