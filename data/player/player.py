"""Этот модуль служит для выдачи основной информации о параметрах, навыках и статистике"""

from colorama import Fore, Style

import inventory
import world
import fight
import information
import lvl_up

MESSAGE_DAMAGE = Fore.GREEN + Style.DIM
MESSAGE_HEAL = Fore.MAGENTA + Style.BRIGHT


def make_hero(cls):
    global heroes
    print('новый экземпляр во внутреннем файле')
    heroes = cls()


class Hero(world.Creature):
    """герой"""
    def __init__(self):
        super().__init__()
        self.lvl = 1
        self.target = ''
        self.skills = []
        self.exp_to_lvl = [0, 25, 50, 100, 500, 2500, 7500, 17000, 26000, 52000, 104000,
                           208000, 512000, 1024000]

    def new_name(self):
        """Выбор имени"""
        self.target = input()






class Overlord(Hero):
    """класс Повелитель"""

    def __init__(self):
        super().__init__()
        self.lvl = 1
        self.full_heart = 25
        self.heart = 25
        self.full_force = 25
        self.force = 4
        self.full_dexterity = 25
        self.dexterity = 6
        self.full_wisdom = 25
        self.wisdom = 3
        self.gold = 25
        self.sign = '🗡'
        self.cls = 'Повелитель'
        self.skills = []


class Inventory:
    def __init__(self):
        self.sword = {}
        self.armor = {}
        self.ring = {}
        self.cloak = {}
        self.bag = {}
        self.chest = {}

    def size_bag(self):
        return len(self.bag)

    def size_equipment(self):
        """Есть ли у игрока надетые вещи?"""
        return len([i for i in [self.sword, self.armor, self.cloak, self.ring] if i != {}])

    def equipment_show():
        """Показывает надетые вещи на игроке. Ничего не принимает и не возвращает"""
        print(Fore.BLUE + '═' * 40)
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
        print(Fore.BLUE + '═' * 40)

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
                                                                                                         " {}\n".format(
                    item['attack'],
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


class Skill:
    """Скиллы"""

    def __init__(self):
        self.lvl = 0

    def start():
        """Функция, которой герой выбирает какие параметры прокачивать, не сделано для всех классов"""
        player.get_lvl(1)
        print(HELP_MESSAGE + "Выберите две характеристики для повышения")
        print(HELP_MESSAGE + 'Введите первую')
        parameter()
        print(HELP_MESSAGE + 'Введите вторую')
        parameter()

    def parameter():
        """Вы выбираете характеристику, она повышается. Ничего не возвращает"""
        while True:
            print(LVL_UP_MESSAGE + 'Здоровье + {} -> 1'.format(14 * (player.parameter['lvl'] - 1)))
            print(LVL_UP_MESSAGE + 'Сила + {} -> 2'.format(3 * (player.parameter['lvl'] - 1), ))
            print(LVL_UP_MESSAGE + 'Ловкость + {} -> 3'.format(3 * (player.parameter['lvl'] - 1)))
            print(LVL_UP_MESSAGE + 'Мудрость + {} -> 4'.format(4 * (player.parameter['lvl'] - 1)) + Style.RESET_ALL)
            number_characteristic = input()
            if number_characteristic == '1':
                player.heart_full_upgrade(14 * (player.parameter['lvl'] - 1))
                break
            elif number_characteristic == '2':
                player.force_upgrade(3 * (player.parameter['lvl'] - 1))
                break
            elif number_characteristic == '3':
                player.dexterity_upgrade(3 * (player.parameter['lvl'] - 1))
                break
            elif number_characteristic == '4':
                player.wisdom_upgrade(4 * (player.parameter['lvl'] - 1))
                break
            else:
                pass

    def choice_skills():  # выбор скила
        """Один из этих словарей, в зависимости от класса, присваивается словарю nav, при старте игры
        Навык характеризуется списком следующим образом 1ая цифра - уровень прокачки навыка от 0 до 3,
        2ая цифра - прокачка эффекта во всех четырёх состояниях навыка: не прокачен, первого уровня, второго,
        третьего. 3ая цифра - то, под каким номером он выводился игроку"""
        display_inf_skills()
        choice_skills()
        number = int(input('Какой навык прокачать?\n'))

    def display_inf_skills():
        """Отображение вкаченных навыков и уровней прокачки для всех классов"""
        for perk in player.skills:
            print(player.skills[perk]['info'])

    def upgrade_nav(name, grade):
        """Даёт полный интерфейс к прокачке данного навыка, подаётся имя навыка и его прокачка. Возвращает удалась прокачка
        или нет. Тут подавляется прокачка выше 3его уровня
        Возвращает: удалась или не удалась прокачка"""
        # проверяет, есть ли в имеющихся навыках данный навык
        if name in player.nav_hero_have:
            # проверяет, можно ли его ещё прокачивать
            if player.nav_hero_have[name][0] < 3:
                player.upgrade_lvl_nav(name)
                return 1
            else:
                print(Fore.RED + Style.BRIGHT + 'Навык {} нельзя больше прокачать'.format(name))
                return 0
        else:
            player.append_new_nav(name, grade)
            return 1


class HandGod(Skill):
    """Длань господа"""

    def __init__(self):
        super().__init__()
        self.lvl_up = [0, 5, 10, 15]
        self.info = ('Вы наносите мощный удар, который в раз больше вашей атаки. Сила зависит от прокачки.'
                     'Один раз за бой')
        self.influence = 'Вы чувствуете, что ваши руки способны на большее'


class DivineProvidence(Skill):
    """Божественное провиденье"""

    def __init__(self):
        super().__init__()
        self.lvl_up = [0, 5, 10, 20]
        self.info = 'Увеличивает вашу атаку'
        self.influence = 'Вы осознали, что нечто большее влияет на этот мир'


class DemonicFury(Skill):
    """Демоническая ярость"""

    def __init__(self):
        super().__init__()
        self.lvl_up = [0, 50, 40, 30]
        self.info = 'Увеличивает вашу атаку'
        self.influence = 'Ваша атака увеличивается в 2 раза, но вы возвращаете часть урона себе'


class Statistics:
    """Статистика"""

    def __init__(self):
        self.battle = 0
        self.earned_gold = 0
        self.kill_monsters = 0

    def gold(self, gold):
        """Вы задаёте количество золото, которое вы заработали, для увеличения статистики"""
        self.earned_gold += gold

    def battles(self, battle):
        """Увеличивает счётчик боёв на первой локации"""
        self.battle += battle

    def kill(self, kills):
        """Увеличивает количество убитых противников в статистике на kills"""
        self.kill += kills


class Quests:
    """Квесты"""

    def __init__(self):
        # для уникального Меча горя
        self.war_goblin = 0

    def bonus_war_goblin(self, goblins):
        """Учитывает количество убитых гоблинов воинов, чтобы выдать меч при тысячи"""
        self.war_goblin += 1
        if self.war_goblin == 1000:
            # НЕАВВВВВВВВВВВВВВВВВВВВВВВВВВВВВВВВВВВВВВВВВВВВВВВВВВВВВВВЫОЛДВАОВЫДАОВЫДАЛОЫВДЛАОЫВДЛОАДЛ
            pass






skills_have_lord = {'Длань Господа': 0, 'Демоническая ярость': 0, 'Божественное провиденье': 0}

skills = {}

# для заполнения навыками игроками во время прокачки навыков. Заполняется имя + словарь
nav_hero_have = {}
# сюда помещаются количество использований скиллов, которые можно применять в бою. словарь: название: количество
# использования навыков, обновляется каждый бой
count_active_skills = {}
# активные в данный удар навыки
active_this_hit = []




def parameter_choice(what_parameter):
    """Присваивает данный словарь параметров основному словарю, где должны хранится параметры
    Передаётся: словарь параметров выбранного класса"""
    global parameter
    parameter = what_parameter
    print('Вы выбрали класс {}'.format(what_parameter['name']))

















def get_lvl(num):
    """Повышает параметр уровня героя на num и добавляет сундк в инвентарь уровня, которыё равен полученному уровню
    Передаётся: количество уровней, которые получает игрок"""
    parameter['lvl'] += num
    print("Ваш уровень повышен {} => {}".format(parameter['lvl'] - num, parameter['lvl']))
    inventory.give_chest(100, 100, parameter['lvl'] - 1, 0)
    if parameter['name'] == 'Повелитель':
        skills.update()
    information.pause()


def append_new_nav(name, nav_hero):
    """Добавляет в словарь навыков героя новый навык(элемент) заданый в агрументе функции, плюс уровень навыка и его
    прокачку
    Передаётся: имя навыка и его прокачка"""
    nav_hero_have[name] = nav_hero
    nav_hero_have[name][0] += 1
    print('Вы получили новый навык {}'.format(name))
    skills_additional_setting(name)
    information.pause()


def upgrade_lvl_nav(name):
    """Принимает навык который нужно прокачивать и прокачивает его на 1
    Передаётся: имя навыка"""
    nav_hero_have[name][0] += 1
    print('Навык {} {} -> {} прокачен'.format(name, nav_hero_have[name][0] - 1, nav_hero_have[name][0]))
    skills_additional_setting(name)
    information.pause()


def skills_additional_setting(name):
    """Реализация некоторых навыков сразу после прокачки. Подаётся имя навыка. Добавляются активные навыки в список
    Передаётся: имя навыка, который обладает таким эффектом"""
    if name == 'Божественное провиденье':
        attack_receive(skills_value_for_grade('Божественное провиденье'))


def skills_value_for_grade(name):
    """Передаёт значения навыка на прокачке через два путя. Первый раз и не первый, чтобы не было out of range.
    После добавления навыка в список. value = разница значений двух уровней навыка, определяемых словарём навыков.
    вычисляется разница между прошлым и настоящим значениями
    Подаётся: имя навыка с пассивыным эффектом. """
    if nav_hero_have[name][0] <= 1:
        value = nav_hero_have[name][1][nav_hero_have[name][0]]
    else:
        value = nav_hero_have[name][1][nav_hero_have[name][0]] - nav_hero_have[name][1][nav_hero_have[name][0] - 1]
    return value


def skill_count_fill():
    """Заполнение значений всех разовые скилов перед боем, для многоразоваого использования, в дальнейшем количество
    уменьшается"""
    if 'Демонический облик' in nav_hero_have:
        count_active_skills['Демонический облик'] = 'full'
    if 'Длань господа' in nav_hero_have:
        count_active_skills['Длань господа'] = 1


def skills_clear():
    """Очищает список активных скиллов игрока от одноразовых, оставляя скилы состояний, должен работать после каждой
    атаки"""
    # список скилов, которые работают постоянно и их не надо выключать
    skills_active_hero_on = ['Демонический облик']
    for skill in active_this_hit:
        if skill in skills_active_hero_on:
            pass
        else:
            active_this_hit.remove(skill)


def use_skill(name_skills, monster, value):
    """Функция использования заданного навыка с боем и количества использований скилла
    Передаётся: название навыка, словарь монстра, количество использований скилла"""
    if value == 'full' or value > 0:
        global active_this_hit
        # вычитание количество исопльзований, если количество не бесконечно
        if value != 'full':
            count_active_skills[name_skills] -= 1
        print('Вы используете навык {}'.format(name_skills))
        # добавление в лист активных для проверки эффекта в бою
        active_this_hit.append(name_skills)
        # костыль, проверка на эффект для пассивных навыков
        # не модулирует бой, если навык пассивный
        if name_skills in lvl_up.passive_skills:
            pass
        else:
            fight.who_first_attack(monster)
    else:
        print('Навык нельзя больше использовать')

print('новый экземпляр во внешнем файле')
heroes = Overlord()