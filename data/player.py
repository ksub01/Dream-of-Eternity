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

