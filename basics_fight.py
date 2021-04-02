"""Функция, в которой описывается механика боя"""

import hero_stats_great
import random
import monsters_great
import inventory_hero_great
import start_game_great
import addition_fight_great


def forest():
    """Запускается при заходе в лес, показывает куда можно пойти, пока сделана только первая локация."""
    while 1:
        choice_location = input("""Вы входите в лес полный опасностей и приключений.
Со сложностью подземелий растёт и сложность наград
Выберите тропинку:
Лес Смерти => 1
Пустыня => 2
Снежная пустыня => 3
Океан => 4
Небесные острова => 5
Болото => 6
Недра => 7
Джунгли => 8
Кладбище => 9
Бездна => 10
Вернуться => 11\n""")
        if choice_location == '1':
            print("Вы попадаете в лес Смерти")
            if hero_stats_great.statistics['mission'] < 2:
                # информация о наличие яда, пока не выполнена первая миссия, потом противоядие станет расходником
                # покупаемым за деньги
                print('Яд Варганиса мешает вам пройти вглубь, но способость героя Мрака позволяет находится у входа\n'
                      'в лес, где концентрации яда минимальна, приличное время и без особых последствий')
                # Три монстра на один уровень игрока
                choice_monster = hero_stats_great.parameter['lvl'] * 3
                # заглушка на шесть монстров для того, чтобы не превысился порог монстров
                if choice_monster > 6:
                    choice_monster = 6
                # рулетка по всем монстрам данной локации
                what_monster = random.randint(1, choice_monster)
                # запуск боя с монстром
                fight(monsters_great.monsters[what_monster], addition_fight_great.dragon_time())
                break
            else:
                ...
                break
        elif choice_location == '11':
            break
        else:
            print('Другие локации пока не готовы')
            start_game_great.outlast()
            pass


def display_skills_in_fight():
    """Отображает навыки и предметы, которые герой может использовать. Навыки извлекаются из списка"""
    for (number, skills_name) in zip(range(3, 100000000), hero_stats_great.skills_active +
                                     inventory_hero_great.item_for_use):
        if hero_stats_great.skills_active[skills_name] == 'full':
            print(skills_name, '->', number)
        else:
            print(skills_name, '*{}*'.format(hero_stats_great.skills_active[skills_name]), '->', number)


def fight(name, what_event):
    """Функция боя. Передаём словарь монстра и проверку на передачу силы Озириса лесу, которая тянется с самого начала
    программы. После действия атаки игра переходит или к награде или к смерти на главном игране"""
    # изменение состояния атаки и здоровья монстра под действием Озириса
    addition_fight_great.hero_defence_after_fight(name)
    monsters_great.monster_heart_new(name, name['full_heart'] * what_event)
    monsters_great.monster_recovery_attack(name, name['full_attack'] * what_event)
    hero_stats_great.save_defence(hero_stats_great.parameter['defence'])
    hero_stats_great.skill_on()
    hero_stats_great.statistics_battle1()
    # начальное окно для оглашения начала боя, работает один раз
    print("!" * 50, "                 Начинается бой", "!" * 50, sep='\n')
    while hero_stats_great.parameter['heart'] > 0 and name['heart'] > 0:
        hero_stats_great.skills_clear()
        inventory_hero_great.append_items_for_using()
        start_game_great.parameters()
        information_monster(name)
        print('Атака -> 1\n'
              'Побег -> 2')
        display_skills_in_fight()
        choice = input()
        if choice == '1':
            attack(name)
            start_game_great.outlast()
        elif choice == '2':
            if escape(attack_monster(name)) == 1:
                break
            else:
                pass
        else:
            if choice.isdigit():
                using_skills_after_fight(int(choice), name)
            pass
    else:
        if name['heart'] <= 0:
            hero_stats_great.statistics_kill(1)
            rewards(name, what_event)
        else:
            # в главное меню т.к. мёртвый
            pass


def using_skills_after_fight(number_skills, name_monster):
    """Функция, которая даёт возможность использовать выбранный навык. Для каждого навыка свой код и особенность
    применения, для каждого происходит удар"""
    # проверяет какой скилл активировать
    for (number, skills) in zip(range(3, 100000000), hero_stats_great.skills_active):
        if number == number_skills:
            hero_stats_great.activated_skill(skills, name_monster, hero_stats_great.skills_active[skills])
            start_game_great.outlast()


def information_monster(name):
    """Функция выдаёт всю инфрмацию о монстре при достаточной разнице в мудрости: равенство, больше на 5, больше на 10
    Передаётся словарь монстра"""
    print(name['name'])
    if hero_stats_great.parameter['wisdom'] >= name['wisdom']:
        print("Уровень: {}".format(name['lvl']))
    else:
        print("?" * 10)
    if hero_stats_great.parameter['wisdom'] >= name['wisdom'] + 5:
        print("Здоровье: {}\nАтака: {}".format(name['heart'],
                                               name['attack']))
    else:
        print("?" * 10)
    if hero_stats_great.parameter['wisdom'] >= name['wisdom'] + 10:
        print("Защита: {}\nЛовкость: {}".format(name['defence'],
                                                name['dexterity']))
    else:
        print("?" * 10)
    if hero_stats_great.parameter['wisdom'] >= name['wisdom'] + 15:
        print("Особое свойство: {}\n".format(name['property']))
    else:
        print("?" * 10)


def attack(name):
    """Основной сценарий атаки, оба варианта, тут на здоровье внимания можно не обращать. Кто первым бьёт определяет
     проверка ловкости"""
    if hero_stats_great.parameter['dexterity'] < name['dexterity']:
        first_hit_monster(name)
    else:
        first_hit_hero(name)


def first_hit_hero(name):
    """Сценарий удара, если первым бъёт герой, то есть ловкость героя больше, передаётся словарь монстра"""
    heroes_hit(name)
    if name['heart'] > 0:
        monsters_hit(name)


def first_hit_monster(name):
    """Сценарий ударов, если первым бьёт монстр, , то есть ловкость монстра больше, передаётся словарь монстра"""
    monsters_hit(name)
    if hero_stats_great.parameter['heart'] > 0:
        heroes_hit(name)


def attack_monster(name):
    """Функция рассчитывает урон монстра, который он наносит герою, функция также возвращает этот урон,
    но защита монстра блокирует максимум 60%, продумана только"""
    if name['attack'] - hero_stats_great.parameter['defence'] <= int(name['attack'] * 0.4):
        damage = int(name['attack'] * 0.4)
    else:
        damage = name['attack'] - hero_stats_great.parameter['defence']
    if damage < 1:
        damage = 1
    return damage


def attack_hero(name):
    """Функция расчитывает урон, который он наносит герой, но защита монстра блокирует максимум 60%, продумана только
     для одного класса, функция также возвращает этот урон"""
    if 'force' in hero_stats_great.parameter:
        if (hero_stats_great.parameter['attack'] + hero_stats_great.parameter['force'] - name['defence'] <=
                int(hero_stats_great.parameter['attack'] + hero_stats_great.parameter['force'] * 0.4)):
            damage = int(name['attack'] * 0.4)
        else:
            damage = hero_stats_great.parameter['attack'] + hero_stats_great.parameter['force'] - name['defence']
        if damage < 1:
            damage = 1
        return damage
    else:
        print('Не предусмотрено других классов')
        pass


def heroes_hit(name):
    """То как расчитывается урон героя. после чего включаются соответствующие эффекты. в будующем удар героя,
     как и монста будет проходить обработку, передаётся словарь монстра"""
    damage = addition_fight_great.after_damage_hero_in_monster(attack_hero(name))
    monsters_great.monster_spend_heart(name, damage)
    addition_fight_great.past_damage_hero_in_monster(name, damage)


def monsters_hit(name):
    """То как расчитывается урон монстра. урон монстра проходит обработу, после чего наносится по герою, после чего
     включаются соответствующие эффекты, передаётся словарь монстра"""
    damage = addition_fight_great.after_damage_monster_in_hero(attack_monster(name))
    hero_stats_great.heart_spend(damage)
    addition_fight_great.past_damage_monster_in_hero(name)


def escape(attack_monster_to_escape_hero):
    """Побег от монстра, вункция возвращает 1 если побег удался и 0 если не удался"""
    print("Вы пытаетесь сбежать")
    start_game_great.outlast()
    escape_from_monster = random.randint(1, 20)
    if escape_from_monster > 7:
        print("Вы сбежали")
        start_game_great.outlast()
        return 1
    else:
        print("Вам не удалось сбежать")
        print("Монстр нанёс вам {} урона".format(attack_monster_to_escape_hero))
        hero_stats_great.heart_spend(attack_monster_to_escape_hero)
        start_game_great.outlast()
        return 0


def rewards(name, event_dragon):
    """Функция, которая награждает игрока. Передаётся словарь монстра, коэффицент опыта, множитель Озириса, ничего
    не возвращает, изменяет на месте"""
    coefficient_gold, probability_chest, coefficient_exp = addition_fight_great.after_gold_and_exp__monster(name)
    # увеличение золото и опыта под действием Озириса
    addition_fight_great.addition_reward(name)
    hero_stats_great.load_defence()
    hero_stats_great.gold_receive(int(name['gold'] * event_dragon * coefficient_gold))
    hero_stats_great.statistics_gold(int(name['gold'] * event_dragon * coefficient_gold))
    hero_stats_great.exp_receive(int(name['exp'] * coefficient_exp * event_dragon))
    inventory_hero_great.give_chest(1, 100, name['lvl'], probability_chest)
    start_game_great.outlast()
