from colorama import Fore, Style
from progress.bar import FillingCirclesBar, FillingSquaresBar


INVENTORY_MESSAGE = Fore.GREEN + Style.BRIGHT
DIE_MASSAGE = Fore.RED + Style.BRIGHT
HELP_MESSAGE = Fore.CYAN + Style.DIM
TOWN_MESSAGE = Style.DIM + Fore.LIGHTYELLOW_EX
MENU_TOWN_MASSAGE = Fore.LIGHTBLUE_EX
STORY_MESSAGE = Fore.YELLOW + Style.DIM
MESSAGE_DIALOGUE = Fore.GREEN
LVL_UP_MESSAGE = Fore.YELLOW + Style.BRIGHT


class Creature:
    """живое создание"""

    def __init__(self):
        self.exp_to_lvl = None
        self.full_heart = 0
        self.heart = 0
        self.full_attack = 0
        self.attack = 0
        self.full_force = 0
        self.force = 0
        self.full_defence = 0
        self.defence = 0
        self.full_dexterity = 0
        self.dexterity = 0
        self.full_wisdom = 0
        self.wisdom = 0
        self.lvl = 0
        self.exp = 0
        self.gold = 0
        self.target = ''
        self.sign = ''

    def recovery_parameter(self):
        """Восстанавливает все параметры, которые изменились по ходу битвы"""
        self.heart = self.full_heart
        self.attack = self.full_attack
        self.force = self.full_force
        self.defence = self.full_defence
        self.dexterity = self.full_dexterity
        self.wisdom = self.full_wisdom

    def alive(self):
        return self.heart > 0

    def progress_exp(self):
        """отображает количество здоровья в виде прогресс-бара"""
        s = '{}{}'.format(Fore.BLUE, '📖')
        lvl = self.lvl
        exp_for_next = self.exp_to_lvl[lvl] - self.exp_to_lvl[lvl-1]
        bar = FillingCirclesBar(s, max=exp_for_next)
        bar.index = self.exp - self.exp_to_lvl[lvl-1]
        bar.update()
        print()

    def progress_hp(self):
        """отображает количество здоровья в виде прогресс-бара"""
        s = '{}{}'.format(Fore.RED, '❤ ')
        bar = FillingSquaresBar(s, max=self.full_heart)
        bar.index = self.heart
        bar.update()
        print()

    def parameters(self):
        """Отражение параметров героя в зависимости от выбранного класса героя"""
        print(Style.RESET_ALL + '─' * 40)
        print(self.target)
        print(Fore.WHITE + Style.BRIGHT + "Уровень {}".format(self.lvl), end='  ')
        print(Fore.MAGENTA + self.sign)
        self.progress_hp()
        self.progress_exp()
        print(Fore.YELLOW + '🪙 {}'.format(self.gold), end='  ')
        print(Fore.BLUE + "⚔ {}".format(self.attack), end='  ')
        print(Fore.LIGHTBLUE_EX + Style.DIM + '👊 {}'.format(self.force), end='  ')
        print(Fore.LIGHTMAGENTA_EX + '🛡 {}'.format(self.defence), end='  ')
        print(Fore.GREEN + '🥾 {}'.format(self.dexterity), end='  ')
        print(Fore.LIGHTBLUE_EX + Style.DIM + '🧠 {}'.format(self.wisdom))
        print('─' * 40 + '\n')

    def gold_spending(self, gold):
        """В фукнцию передаем значение золота, которое тратит игрок, возвращает, получится потратить или нет"""
        # если золота достаточно
        if self.gold >= gold:
            print(Fore.YELLOW + self.target + ' -{}🪙'.format(gold))
            self.gold -= gold
            return 1
        else:
            print(self.target + ' Недостаточно золота')
            return 0

    def gold_receive(self, gold):
        """В функцию подаём значение золота, которое игрок получает"""
        print(self.target + ' +{}🪙'.format(gold))
        self.gold += gold

    def attack_new(self, attack):
        """Новое значение атаки"""
        ans = self.attack - attack
        if ans >= 0:
            print(self.target + ' +{}⚔'.format(ans))
        else:
            print(self.target + ' -{}⚔'.format(-ans))
        self.attack = attack

    def defence_new(self, defence):
        """Герой получает данное количество брони, предыдущее значение нигде не сохраняется"""
        """Новое значение атаки"""
        ans = self.defence - defence
        if ans >= 0:
            print(self.target + ' +{}🛡'.format(ans))
        else:
            print(self.target + ' -{}🛡'.format(-ans))
        self.defence = defence

    def heart_new(self, heart):
        """В функцию подаём значение здоровья, которое становится у игрока. Отображает разницу между прошлым и будующим
        здоровьем"""
        ans = self.heart - heart
        if ans >= 0:
            print(self.target + ' +{}♥'.format(ans))
        else:
            print(self.target + ' -{}♥'.format(-ans))
        self.defence = heart

    def exp_receive(self, exp):
        """В функцию подаём значение опыта, которое игрок получает"""
        self.exp += exp
        print(Fore.BLUE + self.target + ' +{} 📖'.format(exp))

    def heart_upgrade(self, heart):
        """Увеличивает количество максимального здоровья на данную велечину"""
        self.full_heart += heart
        print(self.target + ' +{}💙'.format(heart))
        information.pause()

    def force_upgrade(self, force):
        """Увеличивает количество силы игрока на данную велечину"""
        self.full_force += force
        print(self.target + ' +{}👊'.format(force))
        information.pause()

    def dexterity_upgrade(self, dexterity):
        """Увеличивает количество ловкости игрока на данную велечину"""
        self.full_dexterity += dexterity
        print(self.target + ' +{}🥾'.format(dexterity))
        information.pause()

    def wisdom_upgrade(self, wisdom):
        """Увеличивает количество мудрости игрока на данную велечину"""
        self.full_wisdom += wisdom
        print(self.target + ' +{}🧠'.format(wisdom))
        information.pause()

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

        if inventory.equipment['sword'] != {} and inventory.equipment['sword']['name'] ==\
                'Меч алхимика':
            print('Противник отравлен')
            monsters.monster_spend_heart(name, int(name['heart'] * 0.1))

        if inventory.equipment['sword'] != {} and inventory.equipment['sword']['name'] ==\
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

        if inventory.equipment['armor'] != {} and inventory.equipment['armor']['name']\
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
        if inventory.equipment['armor'] != {} and inventory.equipment['armor']['name'] ==\
                'Доспехи лекаря':
            player.heart_recovery(int(1 * heal_power))

        if inventory.equipment['cloak'] != {} and inventory.equipment['cloak']['name']\
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

        if inventory.equipment['ring'] != {} and inventory.equipment['ring']['name']\
                == 'Кольцо кладоискателя':
            probability_chest += 3

        if inventory.equipment['cloak'] != {} and inventory.equipment['cloak']['name']\
                == 'Плащ мудреца':
            quantity_exp += 10

        # вычисляет количество золото через проценты
        coefficient_gold = int(1 + (quantity_gold/100))
        coefficient_exp = int(1 + (quantity_exp/100))
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


class Thing:
    """Создает все вещи"""
    def __init__(self):
        self.lvl = 0
        self.name = ''
        self.attack = 0
        self.defence = 0
        self.money = 0
        self.rare = 0
        self.property = ''


class Sword(Thing):
    """Класс всех мечей"""


class Armor(Thing):
    """Класс брони"""


class Ring(Thing):
    """Класс кольца"""


class Cloak(Thing):
    """Класс плаща"""


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