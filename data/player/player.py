"""Этот модуль служит для выдачи основной информации о параметрах, навыках и статистике"""

from colorama import Fore, Style

import inventory
import world
import fight
import information
import lvl_up

    def remove_thing(item, inventory_choice):
        """Удаляет данную вещь из данной ячейки инвентаря
        Принимает: словарь вещи и из какой ячейки инвенторя нужно удаалить вещь"""
        all_things = inventory['sword'] + inventory['armor'] + inventory['cloak'] + inventory['ring']
        for item_in_inventory in all_things:  # inventory - словарь для каждого типа со значением списка
            if item_in_inventory == item:
                inventory_choice.remove(item)
                break


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


def dragon_time():
    """Функция которая выдаёт множитель силы монстров при входе в данж. В дальнейшем будет переделана, чтобы
    работала долго для защиты от абуза
    Возвращает множитель события, 1 - если ничего, 2 - если что-то и этот множитель в дальнейшем используетяс
    для умножения всех параметров"""
    if random.randint(1, 10) == 1:
        print('!' * 40)
        print('Озирис делится своей силой с лесом Смерти')
        print('!' * 40)
        information.pause()
        return 2
    else:
        print('Сегодня лес спокоен и угрозы Озириса нет')
        information.pause()
        return 1


def calc_heal_power():
    """Рассчитывает heal power для лечащих предметов, перед запуском основной функции"""
    heal_power = 1
    if inventory.equipment['cloak'] != {} and inventory.equipment['cloak']['name'] \
            == 'Порванный плащ':
        heal_power += 0.5
    return heal_power


def after_fight(name):
    """Действия, которые происходят перед самим боем, при встрече монстра, после сохранения защиты и только один раз"""
    if name['name'] == 'Гоблин Убийца':
        player.parameter['defence'] = 0
    if inventory.equipment['ring'] != {} and inventory.equipment['ring']['name'] == \
            'Кольцо настоящего мужчины':
        player.heart_recovery(10)


def after_damage_in_monster(damage):
    """Модификация урона предметами и скилами перед ударом. Возвращает урон"""
    if 'Длань господа' in player.active_this_hit:
        damage = damage * \
                 player.nav_hero_have['Длань господа'][1][player.nav_hero_have['Длань господа'][0]]
    if 'Демонический облик' in player.active_this_hit:
        damage = damage * 2
    return damage


def after_damage_in_hero(damage):
    """Функция возвращает урон, нанесённый монстром герою, модифицируя его, возвращает урон наносимый монстром"""
    if (inventory.equipment['cloak'] != {} and inventory.equipment['cloak']['name']
            == 'Плащ защитника человечества'):
        if random.randint(1, 10) == 1:
            damage = 0
            print('Плащ защитника человечества нейтрализовал урон, нанесённый монстром')
    return damage


def past_damage_in_monster(name, damage_hero_in_monster):
    """Функция проявляет действие многих предметов после удара героя. В том числе лечение, повышение защиты или
    мгновенная смерть монстра, вампиризм. Ничего не возвращает, передаём словарь мостра и урон героя монстру"""
    # переменная регистрирует эффективность предметов восстанавливающих здоровье на основе других предметов
    heal_power = calc_heal_power()

    if inventory.equipment['sword'] != {} and inventory.equipment['sword']['name'] == 'Меч чести':
        # повышение защиты в бою после каждой атаки, для этого как раз защита и сохранялась
        if random.randint(1, 10) <= 2:
            player.defence_receive(1)

    if inventory.equipment['sword'] != {} and inventory.equipment['sword']['name'] == \
            'Меч алхимика':
        print('Противник отравлен')
        monsters.monster_spend_heart(name, int(name['heart'] * 0.1))

    if inventory.equipment['sword'] != {} and inventory.equipment['sword']['name'] == \
            'Меч повелителя гоблинов' and name['names'].find("Гоблин") >= 0:
        monsters.monster_heart_new(name, 0)
        print('Гоблин усмирён')

    if inventory.equipment['sword'] != {} and inventory.equipment['sword']['name'] == "Меч горя":
        player.heart_recovery(int(damage_hero_in_monster * 0.1 * heal_power))

    if 'Демонический облик' in player.active_this_hit:
        player.heart_spend(int(damage_hero_in_monster * player.nav_hero_have['Демонический облик'][1][
            player.nav_hero_have['Демонический облик'][0]] / 100))


def past_damage_in_hero(name):
    """Функция проявляет действие многих предметов и способностей после удара монстра. В том числе отражение урона
    обратно в монстра, лечение монстра, кража монстром, отравление игрока. Ничего не возвращает"""
    heal_power = calc_heal_power()

    if name['name'] == 'Гоблин Шаман':
        monsters.monster_recovery_heart(name, 2)

    if inventory.equipment['armor'] != {} and inventory.equipment['armor']['name'] \
            == 'Броня солнца':
        monsters.monster_spend_heart(name, int(name['attack'] * 0.1))

    if name['name'] == 'Змея Варганиса':
        # змея отравляет на 20 процентов, перед каждым ударом
        player.heart_spend(int(player.parameter['heart'] * 0.2))
    if name['name'] == 'Култист Озириса':
        # культист крадёт одну из четырёх экипированных вещей
        item = random.randint(1, 12)
        if item == 1:
            inventory.lose_sword()
            print('Монстр украл ваш меч')
        elif item == 2:
            inventory.lose_armor()
            print('Монстр украл ваши доспехи')
        elif item == 3:
            inventory.lose_cloak()
            print('Монстр украл ваш плащ')
        elif item == 4:
            inventory.lose_ring()
            print('Монстр украл ваше кольцо')
        else:
            print('Попытка кражи не удалась')
            pass
    if inventory.equipment['armor'] != {} and inventory.equipment['armor']['name'] == \
            'Доспехи лекаря':
        player.heart_recovery(int(1 * heal_power))

    if inventory.equipment['cloak'] != {} and inventory.equipment['cloak']['name'] \
            == 'Плащ регенерации':
        player.heart_recovery(int(3 * heal_power))


def addition_reward(name):
    """Обрабатывает статистику перед получением наград и делает дополнительные действия: например выдаёт награду за
    1000 убитых монстров, запускает уникальные события, получает словарь"""
    if name['name'] == 'Гоблин Воин':
        player.bonus_war_goblin()


def before_award(monster):
    """Функция, которая вычисляет ваше золото исходя из предметов и вероятность сундука по 100 бальной шкале
     из предметов и возвращает кортеж всех этих значений"""
    # эти переменные меняются и возвращаются в функции
    # всё вычисляется в процентах
    quantity_gold = 0
    probability_chest = 0
    quantity_exp = 0

    if inventory.equipment['sword'] != {} and inventory.equipment['sword']['name'] == 'Меч лести':
        quantity_gold += 20
        print('Количество золота увеличено на 20%')

    if inventory.equipment['armor'] != {} and inventory.equipment['armor']['name'] == 'Доспехи богатства':
        quantity_gold += 10
        print('Количество золото увеличено на 10%')

    if inventory.equipment['sword'] != {} and inventory.equipment['sword']['name'] == 'Меч повелителя гоблинов':
        probability_chest += 5
        quantity_gold += 10

    if inventory.equipment['ring'] != {} and inventory.equipment['ring']['name'] \
            == 'Кольцо кладоискателя':
        probability_chest += 3

    if inventory.equipment['cloak'] != {} and inventory.equipment['cloak']['name'] \
            == 'Плащ мудреца':
        quantity_exp += 10

    # вычисляет количество золото через проценты
    coefficient_gold = int(1 + (quantity_gold / 100))
    coefficient_exp = int(1 + (quantity_exp / 100))
    return coefficient_gold, probability_chest, coefficient_exp


def display_skills():
    """Отображает навыки и предметы, которые герой может использовать. Навыки извлекаются из списка"""
    for (number, skills_name) in zip(range(3, 100000000), player.count_active_skills):
        if player.count_active_skills[skills_name] == 'full':
            print(skills_name, '->', number)
        else:
            print(skills_name, '*{}*'.format(player.count_active_skills[skills_name]), '->', number)


def using_skills(number_skills, name_monster):
    """Функция, которая даёт возможность использовать выбранный навык. Для каждого навыка свой код и особенность
    применения, для каждого происходит удар"""
    # проверяет какой скилл активировать
    for (number, skills) in zip(range(3, 100000000), player.count_active_skills):
        if number == number_skills:
            player.use_skill(skills, name_monster,
                             player.count_active_skills[skills])
            information.pause()


def monster_information(name):
    """Функция выдаёт всю инфрмацию о монстре при достаточной разнице в мудрости: равенство, больше на 5, больше на 10
    Передаётся: словарь монстра"""
    print(Fore.RED + name['name'] + ' 🐺')
    if player.parameter['wisdom'] >= name['wisdom']:
        print("Уровень: {}".format(name['lvl']))
    if player.parameter['wisdom'] >= name['wisdom'] + 5:
        print("🖤: {}\nАтака: {}".format(name['heart'], name['attack']))
    if player.parameter['wisdom'] >= name['wisdom'] + 10:
        print("⛨: {}\nЛовкость: {}".format(name['defence'],
                                           name['dexterity']))
    if player.parameter['wisdom'] >= name['wisdom'] + 15:
        print(name['property'])


def first_hit_hero(name):
    """Сценарий удара, если первым бъёт герой, то есть ловкость героя больше, передаётся словарь монстра
    Передаётся: словарь монстра"""
    heroes_hit(name)
    if name['heart'] > 0:
        monsters_hit(name)


def first_hit_monster(name):
    """Сценарий ударов, если первым бьёт монстр, , то есть ловкость монстра больше
    Передаётся: словарь монстра"""
    monsters_hit(name)
    if player.parameter['heart'] > 0:
        heroes_hit(name)


def attack_monster(name):
    """Функция рассчитывает урон монстра, который он наносит герою, функция также возвращает этот урон,
    но защита монстра блокирует максимум 60%, продумана только
    Передаётся: словарь монстра"""
    if name['attack'] - player.parameter['defence'] <= int(name['attack'] * 0.4):
        damage = int(name['attack'] * 0.4)
    else:
        damage = name['attack'] - player.parameter['defence']
    if damage < 1:
        damage = 1
    return damage


def attack_hero(name):
    """Функция расчитывает урон, который он наносит герой, но защита монстра блокирует максимум 60%, продумана только
     для одного класса, функция также возвращает этот урон
     Передаётся: словарь монстра"""
    if 'force' in player.parameter:
        if (player.parameter['attack'] +
                player.parameter['force'] - name['defence'] <=
                int(player.parameter['attack'] +
                    player.parameter['force'] * 0.4)):
            damage = int(name['attack'] * 0.4)
        else:
            damage = player.parameter['attack'] + \
                     player.parameter['force'] - name['defence']
        if damage < 1:
            damage = 1
        return damage


def effect_hit_hero():
    s = '{} {}{} '.format('🗡', Fore.GREEN, '')
    spinner = Spinner(s)
    for i in range(3):
        time.sleep(0.1)
        spinner.next()
    print(end=' ')


def effect_hit_monster():
    s = '{}{} '.format('🐾', Fore.RED, '')
    spinner = Spinner(s)
    for i in range(3):
        time.sleep(0.1)
        spinner.next()
    print(end=' ')


def heroes_hit(name):
    """То как расчитывается урон героя. после чего включаются соответствующие эффекты. в будующем удар героя,
     как и монста будет проходить обработку, передаётся словарь монстра"""
    # разброс урона 0.8 - 1.2
    effect_hit_hero()
    damage = int(effects.after_damage_in_monster(attack_hero(name)) * random.randint(8, 12) / 10)
    monsters.monster_spend_heart(name, damage)
    effects.past_damage_in_monster(name, damage)


def monsters_hit(name):
    """То как расчитывается урон монстра. урон монстра проходит обработу, после чего наносится по герою, после чего
     включаются соответствующие эффекты, передаётся словарь монстра"""
    # разброс урона 0.8 - 1.2
    effect_hit_monster()
    damage = int(effects.after_damage_in_hero(attack_monster(name)) * random.randint(8, 12) / 10)
    player.heart_spend(damage)
    effects.past_damage_in_hero(name)


def escape(name):
    """Побег от монстра, вункция возвращает 1 если побег удался и 0 если не удался"""
    print("Вы пытаетесь сбежать")
    information.pause()
    escape_from_monster = random.randint(1, 20)
    if escape_from_monster > 6:
        print("Вы сбежали")
        player.defence_load()
        information.pause()
        return 1
    else:
        print("Вам не удалось сбежать")
        monsters_hit(name)
        information.pause()
        return 0


def rewards(name, event_dragon):
    """Функция, которая награждает игрока.
    Передаётся: словарь монстра, коэффицент опыта, множитель Озириса"""
    coefficient_gold, probability_chest, coefficient_exp = effects.before_award(name)
    effects.addition_reward(name)
    player.gold_receive(int(name['gold'] * event_dragon * coefficient_gold))
    player.statistics_up_gold(int(name['gold'] * event_dragon * coefficient_gold))
    player.exp_receive(int(name['exp'] * coefficient_exp * event_dragon))
    inventory.give_chest(1, 50, name['lvl'], probability_chest)
    player.defence_load()
    information.pause()








class Chest(Thing):
    """Класс сундуков"""
    def __init__(self, lvl):
        super().__init__()
        self.lvl = lvl

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


class Game:
    """Основные функциии для игры"""
    def pause(self):
        """Пауза после отображения текста, чтобы игрок успел прочитать"""
        input(Style.RESET_ALL + HELP_MESSAGE + 'Нажмите Enter\n')  # задержка для того, чтобы игрок мог прочитать

    def goodbye(self):
        """Прощание с игроком в любой ситуации"""
        print(HELP_MESSAGE + 'До свидания')
        pause()

    def end_game():
        print(DIE_MASSAGE + 'Вы проиграли. Озирис уничтожил мир, а Аркона пала.')

    def about():
        """Отображение имени игры и её версии перед её началом, частично копирует README (Github)"""
        version = '0.1.1.6.0'
        print(Fore.MAGENTA + Style.BRIGHT + 'Dream of Eternity')
        print(Fore.MAGENTA + Style.DIM + 'Версия {}'.format(version))
        information.pause()

    def prologue():
        """Вывод начальной информации о мире игры перед её началом"""
        print(STORY_MESSAGE + 'Здраствуй, великий герой Мрака, призванный спасти наш мир от великой угрозы.\n'
                              'Опасность возникла внезапно, когда великий дракон Озирис поселился в нашем мире.\n'
                              'Он послал на нас орды монстров, которые грабили и убивали. Прошло время, Озирис успокоился '
                              'и настал мир,\n '
                              'но внезапно, всё возобновилось, страдания и смерти снова вернулись. '
                              'Сейчай люди умирают и надежды уже нет.\n'
                              'Использовав последние запасы кристалов пробуждения мы призвали трёх великих геров Страха,\n'
                              'имевщих девять жизней, которые вскоре пали под\n'
                              'натиском дракона и его приспешников, уничтожав их и захватив\n'
                              'их сферы пробуждения Озирис лишь усилил свой напор.\n'
                              'Надежды уже не осталось, но великая жрица Элиза воспользовалась жертвенной магией\n'
                              'для призыва ещё одного героя - тебя. По правде сказать шансов у тебя немного и попытка '
                              'всего одна\n '
                              'Мы не надеямся на твою победу, но возможно благодаря тебе мы сможем прожить чуть дольше\n'
                              'В любом случае, у нас не будет шанса против Озириса, если мы не убьём 10 его верных '
                              'приспешников:\n '
                              'Варганиса - повелителя леса Смерти, Ламура - обитателя пустыни, Сноуфейри - жительницу '
                              'снегов,\n '
                              'Варлиту, захватившую океан, Металику - королеву парящих островов, Гримура, жаждующего '
                              'порчи, Тераэль,\n '
                              'находящуюся в недрах, Виризиса, уничтожившего племя Ваши, Некрола, воскресающего и Ларита,\n'
                              'повелителя Бездны, который помог Озирису уничтожить всё человечесто, и который уничтожил '
                              'источник\n '
                              'Исполнения. Мы, основатели, сделали всё что смогли, прости нас, что обрекаем тебя на '
                              'верную смерть')
        information.pause()

    def choice_class():
        """Выбор класса в начале игры для присвоения словаря навыков игроку. Словарь находится в hero_stats"""
        flag = 1
        while flag:
            print(Fore.CYAN + 'Выберите класс:')
            choice = input(Style.RESET_ALL + Fore.YELLOW + 'Повелитель ➔ 1 (воин, владеющий силой и уничтожающий '
                                                           'монстров мечом)\n')
            if choice == '1':
                player.make_hero(player.Overlord)
                flag = 0
            name = input('Введите имя\n')
            player.heroes.target = name
            print('текущее имя' + player.heroes.target)

    def start_game():
        """Функции, включающиеся перед самым запуском игры"""
        start.about()
        start.prologue()


    def setting():
        """Выбор класса перед началом игры"""
        start.choice_class()


    def playing_loop():
        """Основной цикл игры, с действиями внутри города и боями"""
        while heroes.alive():
            print('Текущее имя' + heroes.target)
            # проблема выбора имени и выбора из трехклассов, а не из одного
            # проблема с присвоением и изменением экземпляров классов в других модулях
            heroes.parameters()
            information.town_places()
            information.if_lvl_up()
            choice = input()
            if choice == '1':
                blacksmith.dialogue()
            elif choice == '2':
                hotel.dialogue()
            elif choice == '3':
                fight.dungeon()
            elif choice == '4':
                casino.dialogue()
            elif choice == '5':
                inventory.start_inventory()
        else:
            if not heroes.alive():
                information.end_game()

class Town:
    """Город"""

    def if_lvl_up():
        """В городе отображает строку о возможности перейти на новый уровень. Значения берутся из массива опыта exp
        в lvl_up"""
        if heroes.exp >= heroes.exp_to_lvl[heroes.lvl]:
            print(INVENTORY_MESSAGE + "Поспите, чтобы повысить ваш уровень\n")

    def town_places():
        """Постоянно высвечивается в городе для отображения мест, куда игрок может пойти"""
        print(TOWN_MESSAGE + 'Вы находитесь в городе Аркона, последнем оплоте человечества' + '\n')
        print('╍' * 40)
        print(MENU_TOWN_MASSAGE +
              '🛖 ➔ 1\n'
              '🛌 ➔ 2\n'
              '🌲 ➔ 3\n'
              '🎲 ➔ 4\n'
              '🏡 ➔ 5')
        print('╍' * 40)


class Blacksmith:
    def get_item(item, discount):
        """Проверяет, хватает ли у игрока денег, если да, то добавляет данный предмет в инвентарь.
        Принимает: предмет и модификатор цены"""
        if player.parameter['gold'] >= int(item['gold'] * discount):
            player.gold_spending(int(item['gold'] * discount))
            inventory.give_thing(item)
            print('Спасибо за покупку\n')
            information.pause()
        else:
            information.not_enough_money()

    def calc_discount():
        """Действуют предметы, влияющие на цену. Функция возвращает этот модификатор"""
        discount = 1  # модификатор цен в процентах
        if inventory.equipment['ring'] != {} and inventory.equipment['ring']['name'] == \
                'Кольцо болтуна':
            discount -= 0.1
        return discount

    def dialogue():
        """Основной интерфейс кузнеца"""
        while 1:
            discount = calc_discount()  # в десятых долях от целой части
            choice_division = showcase()
            # выбор зависит от класса
            if choice_division == '1' and player.parameter['name'] == 'Повелитель':
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
            if player.parameter['lvl'] >= items.swords_shop[key]['lvl']:
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
            if player.parameter['lvl'] >= items.armor_shop[key]['lvl']:
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
            if player.parameter['lvl'] >= items.cloak_shop[key]['lvl']:
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
            if player.parameter['lvl'] >= items.ring_shop[key]['lvl']:
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
                print('Ваше золото: {}'.format(player.parameter['gold']))
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
                print('Ваше золото: {}'.format(player.parameter['gold']))
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
                print('Ваше золото: {}'.format(player.parameter['gold']))
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
                print('Ваше золото: {}'.format(player.parameter['gold']))
                print('Вы точно хотите купить <{}>?\nЦена *{}*\n'
                      'Особое свойство: <<{}>>\nУровень {}\n'
                      'Да -> 1 Нет -> 2\n'.format(items.ring_shop[ring_number]['name'],
                                                  int(items.ring_shop[ring_number]['gold'] * discount),
                                                  items.ring_shop[ring_number]['property'],
                                                  items.ring_shop[ring_number]['lvl']))
                choice = input()
                if choice == '1':
                    get_item(items.ring_shop[ring_number], discount)



class Casino:
    def dialogue():
        """Функция для выбора миниигры в рулетке, в которую хочет сыграть игрок и запуска её"""
        while True:
            choice = input(Style.RESET_ALL + MESSAGE_DIALOGUE + 'Здраствуйте. Вы находитесь в казино.'
                                                                ' Выберите варианты игры\n'
                                                                'Золотой куш ➔ 1\n'
                                                                'Выйти ➔ 2\n')
            if choice == '1':
                print(HELP_MESSAGE + 'Вы указываете золото, с вас его снимают, вам выпадает число золота, которое вы'
                                     ' получаете\n'
                                     'Число может выпасть в интервале от [0, 2n], где n ваше число')
                start_game(gold_jackpot)
                break
            elif choice == '2':
                break

    def start_game(game):
        """Запускает игру заданную в рулетке, то есть даёт полный интерфейс, взаимодёствее перед игрой
        Передаётся: функция игры, в которую игрок хочет играть"""
        while True:
            what = input(HELP_MESSAGE + 'Играть => 1\n' + 'Нет => 2\n')
            if what == '1':
                game()
            elif what == '2':
                information.goodbye()
                break

    def gold_jackpot():
        """Проводит первую миниигру в казино - золотой куш. Игрок ставить золото есу выпадает случайный результат
        из списка [0, его золото*2]"""
        # вводится количество золота, которое игрок ставит
        while True:
            gold = input(Style.RESET_ALL + MESSAGE_DIALOGUE + 'Приветствуем вас в игре Золотой куш.\n'
                                                              'Введите количество золота, которое вы ставите\n'
                                                              'Выход ➔ 0\n')
            if gold.isdigit() and gold != '0':
                gold = int(gold)
                if heroes.goldspending(gold):
                    print(HELP_MESSAGE + 'Игра начинается\n'
                                         'Итак выпало...')
                    information.pause()
                    win_gold = random.randint(0, gold * 2)
                    print(Fore.YELLOW + '*' + str(win_gold) + '*')
                    heroes.gold_receive(win_gold)
                    information.pause()
            elif gold == '0':
                information.goodbye()
                break


class Hotel:
    price_sleep = [0, 5, 40, 100, 400, 800, 1200, 1700, 2100, 2600, 3000]

    def dialogue():
        """Основной модуль (эта функция запускается при выборе гостиницы в главном меню), где модулируется поведение
        гостиницы и происходит выбор услуг, а также происходит проверка
        выбранной услуги для оказания её пользователю. Также тут запускается процесс сна где происходит восстановление
        параметров и повышение уровня"""
        while True:
            print(TOWN_MESSAGE + 'Вы находитесь в гостинице')
            ans = input(Style.RESET_ALL + MESSAGE_DIALOGUE + 'Здраствуйте. Воспользоваться нашими услугами вы можете за'
                                                             ' {} монет\n'
                                                             'Согласны?\n'
                                                             'Да ➔ 1\n'
                                                             'Нет ➔ 2\n'.format(price_sleep[1]))
            if ans == '1':
                if heroes.gold_spending(price_sleep[1]):
                    # тратятся деньги, причём индекс затрат равен параметру 'location' который берётся из статистики героя,
                    # важно учесть что он начинается с единицы
                    sleep()
                    information.goodbye()
                    break
            elif ans == '2':
                information.goodbye()
                break

    def sleep():
        """Моделирует поведение сна, запускаются все функции, которые нужно запускать во время сна
        (повышение уровня и восстановление параметров). Этот модуль и есть полная эмуляция поведения сна.
        Его можно использовать без интефейса гостиницы"""
        test_lvl()
        recovery_all()

    def recovery_all():
        """Восстановление потраченных параметров во время сна"""
        need_heal = heroes.full_heart - heroes.heart
        heroes.heart_new(need_heal)
        # если игрок маг то восстанавливается вся магия путём установления нового значения

    def test_lvl():
        """Проверка опыта для поднятия уровня во время сна и поднятие уровня"""
        # если опыта больше чем в массиве с количеством опыта для следующего уровня, то уровень повышается
        # опыт не сбрасывается с повышением, позиция для нужного количества опыта соответствует текущему уровню игрока
        if heroes.exp >= heroes.exp_to_lvl[heroes.lvl]:
            # повышение характеристик
            lvl_up.start()
            # повышение уровня навыка
            lvl_up.choice_skills()


class BattleLocations:
    def dungeon():
        """Запускается при заходе в лес, показывает куда можно пойти, пока сделана только первая локация."""
        while True:
            choice_location = input('Куда вы поёдете?:'
                                    'Лес Смерти => 1\n'
                                    'Вернуться => 2')
            if choice_location == '1':
                print("Вы попадаете в лес Смерти")
                # информация о наличие яда, пока не выполнена первая миссия, потом противоядие станет расходником
                # покупаемым за деньги
                print('Яд Варганиса мешает вам пройти вглубь, но способость героя Мрака позволяет находится у входа\n'
                      'в лес, где концентрации яда минимальна, приличное время и без особых последствий')
                # Три монстра на один уровень игрока
                choice_monster = player.parameter['lvl'] * 3
                # заглушка на шесть монстров для того, чтобы не превысился порог монстров
                if choice_monster > 6:
                    choice_monster = 6
                # рулетка по всем монстрам данной локации
                what_monster = random.randint(1, choice_monster)
                # запуск боя с монстром
                fighting(monsters.monsters[what_monster], effects.dragon_time())
                break
            else:
                break

    def start_message():
        """Стартовое сообщение перед началом боя"""
        print(Style.RESET_ALL + '─' * 50)
        print(Fore.RED + "                 Начинается бой")
        print('─' * 50)

    def fighting(name, what_event):
        """Функция боя. Передаём словарь монстра и проверку на передачу силы Озириса лесу, которая тянется с самого начала
        программы. После действия атаки игра переходит или к награде или к смерти на главном игране"""

        # изменение состояния атаки и здоровья монстра под действием Озириса
        monsters.monster_heart_new(name, name['full_heart'] * what_event)
        monsters.monster_recovery_attack(name, name['full_attack'] * what_event)
        player.defence_save(player.parameter['defence'])
        player.skill_count_fill()
        player.statistics_up_battle1()
        start_message()
        while player.alive() and name['heart'] > 0:
            player.skills_clear()
            information.parameters()
            monster_information(name)
            print('\n⚔  ➔ 1\n'
                  '🏃 ➔ 2')
            display_skills()
            choice = input()
            if choice == '1':
                who_first_attack(name)
                information.pause()
            elif choice == '2':
                if escape(name) == 1:
                    break
            else:
                if choice.isdigit():
                    using_skills(int(choice), name)
        else:
            if name['heart'] <= 0:
                player.statistics_up_kill(1)
                rewards(name, what_event)
            else:
                # в главное меню т.к. мёртвый
                pass

    def who_first_attack(name):
        """Основной сценарий атаки, оба варианта, тут на здоровье внимания можно не обращать. Кто первым бьёт определяет
         проверка ловкости
         Передаётся: словарь монстра"""
        if player.parameter['dexterity'] < name['dexterity']:
            first_hit_monster(name)
        else:
            first_hit_hero(name)