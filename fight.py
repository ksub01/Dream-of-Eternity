"""Функция, в которой описывается механика боя"""

import hero
import random
import monsters
import inventory
import effects
import information


def dungeon():
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
            if hero.statistics['mission'] < 2:
                # информация о наличие яда, пока не выполнена первая миссия, потом противоядие станет расходником
                # покупаемым за деньги
                print('Яд Варганиса мешает вам пройти вглубь, но способость героя Мрака позволяет находится у входа\n'
                      'в лес, где концентрации яда минимальна, приличное время и без особых последствий')
                # Три монстра на один уровень игрока
                choice_monster = hero.parameter['lvl'] * 3
                # заглушка на шесть монстров для того, чтобы не превысился порог монстров
                if choice_monster > 6:
                    choice_monster = 6
                # рулетка по всем монстрам данной локации
                what_monster = random.randint(1, choice_monster)
                # запуск боя с монстром
                start_fight(monsters.monsters[what_monster], effects.dragon_time())
                break
            else:
                ...
                break
        elif choice_location == '11':
            break
        else:
            print('Другие локации пока не готовы')
            information.pause()
            pass


def display_skills():
    """Отображает навыки и предметы, которые герой может использовать. Навыки извлекаются из списка"""
    for (number, skills_name) in zip(range(3, 100000000), hero.count_active_skills):
        if hero.count_active_skills[skills_name] == 'full':
            print(skills_name, '->', number)
        else:
            print(skills_name, '*{}*'.format(hero.count_active_skills[skills_name]), '->', number)


def start_fight(name, what_event):
    """Функция боя. Передаём словарь монстра и проверку на передачу силы Озириса лесу, которая тянется с самого начала
    программы. После действия атаки игра переходит или к награде или к смерти на главном игране"""
    # изменение состояния атаки и здоровья монстра под действием Озириса
    monsters.monster_heart_new(name, name['full_heart'] * what_event)
    monsters.monster_recovery_attack(name, name['full_attack'] * what_event)
    hero.defence_save(hero.parameter['defence'])
    hero.skill_count_fill()
    hero.statistics_up_battle1()
    inventory.items_in_use()
    # начальное окно для оглашения начала боя, работает один раз
    print("!" * 50, "                 Начинается бой", "!" * 50, sep='\n')
    while hero.parameter['heart'] > 0 and name['heart'] > 0:
        hero.skills_clear()
        information.parameters()
        monster_information(name)
        print('Атака -> 1\n'
              'Побег -> 2')
        display_skills()
        choice = input()
        if choice == '1':
            who_first_attack(name)
            information.pause()
        elif choice == '2':
            if escape(name) == 1:
                break
            else:
                pass
        else:
            if choice.isdigit():
                using_skills(int(choice), name)
            pass
    else:
        if name['heart'] <= 0:
            hero.statistics_up_kill(1)
            rewards(name, what_event)
        else:
            # в главное меню т.к. мёртвый
            pass


def using_skills(number_skills, name_monster):
    """Функция, которая даёт возможность использовать выбранный навык. Для каждого навыка свой код и особенность
    применения, для каждого происходит удар"""
    # проверяет какой скилл активировать
    for (number, skills) in zip(range(3, 100000000), hero.count_active_skills):
        if number == number_skills:
            hero.use_skill(skills, name_monster,
                           hero.count_active_skills[skills])
            information.pause()


def monster_information(name):
    """Функция выдаёт всю инфрмацию о монстре при достаточной разнице в мудрости: равенство, больше на 5, больше на 10
    Передаётся: словарь монстра"""
    print(name['name'])
    if hero.parameter['wisdom'] >= name['wisdom']:
        print("Уровень: {}".format(name['lvl']))
    else:
        print("?" * 10)
    if hero.parameter['wisdom'] >= name['wisdom'] + 5:
        print("Здоровье: {}\nАтака: {}".format(name['heart'],
                                               name['attack']))
    else:
        print("?" * 10)
    if hero.parameter['wisdom'] >= name['wisdom'] + 10:
        print("Защита: {}\nЛовкость: {}".format(name['defence'],
                                                name['dexterity']))
    else:
        print("?" * 10)
    if hero.parameter['wisdom'] >= name['wisdom'] + 15:
        print("Особое свойство: {}\n".format(name['property']))
    else:
        print("?" * 10)


def who_first_attack(name):
    """Основной сценарий атаки, оба варианта, тут на здоровье внимания можно не обращать. Кто первым бьёт определяет
     проверка ловкости
     Передаётся: словарь монстра"""
    if hero.parameter['dexterity'] < name['dexterity']:
        first_hit_monster(name)
    else:
        first_hit_hero(name)


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
    if hero.parameter['heart'] > 0:
        heroes_hit(name)


def attack_monster(name):
    """Функция рассчитывает урон монстра, который он наносит герою, функция также возвращает этот урон,
    но защита монстра блокирует максимум 60%, продумана только
    Передаётся: словарь монстра"""
    if name['attack'] - hero.parameter['defence'] <= int(name['attack'] * 0.4):
        damage = int(name['attack'] * 0.4)
    else:
        damage = name['attack'] - hero.parameter['defence']
    if damage < 1:
        damage = 1
    return damage


def attack_hero(name):
    """Функция расчитывает урон, который он наносит герой, но защита монстра блокирует максимум 60%, продумана только
     для одного класса, функция также возвращает этот урон
     Передаётся: словарь монстра"""
    if 'force' in hero.parameter:
        if (hero.parameter['attack'] +
                hero.parameter['force'] - name['defence'] <=
                int(hero.parameter['attack'] +
                    hero.parameter['force'] * 0.4)):
            damage = int(name['attack'] * 0.4)
        else:
            damage = hero.parameter['attack'] + \
                     hero.parameter['force'] - name['defence']
        if damage < 1:
            damage = 1
        return damage
    else:
        print('Не предусмотрено других классов')
        pass


def heroes_hit(name):
    """То как расчитывается урон героя. после чего включаются соответствующие эффекты. в будующем удар героя,
     как и монста будет проходить обработку, передаётся словарь монстра"""
    # разброс урона 0.8 - 1.2
    damage = int(effects.after_damage_in_monster(attack_hero(name)) * random.randint(8, 12) / 10)
    monsters.monster_spend_heart(name, damage)
    effects.past_damage_in_monster(name, damage)


def monsters_hit(name):
    """То как расчитывается урон монстра. урон монстра проходит обработу, после чего наносится по герою, после чего
     включаются соответствующие эффекты, передаётся словарь монстра"""
    # разброс урона 0.8 - 1.2
    damage = int(effects.after_damage_in_hero(attack_monster(name)) * random.randint(8, 12) / 10)
    hero.heart_spend(damage)
    effects.past_damage_in_hero(name)


def escape(name):
    """Побег от монстра, вункция возвращает 1 если побег удался и 0 если не удался"""
    print("Вы пытаетесь сбежать")
    information.pause()
    escape_from_monster = random.randint(1, 20)
    if escape_from_monster > 6:
        print("Вы сбежали")
        hero.defence_load()
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
    effects.get_items(name)
    hero.gold_receive(int(name['gold'] * event_dragon * coefficient_gold))
    hero.statistics_up_gold(int(name['gold'] * event_dragon * coefficient_gold))
    hero.exp_receive(int(name['exp'] * coefficient_exp * event_dragon))
    inventory.give_chest(1, 100, name['lvl'], probability_chest)
    hero.defence_load()
    information.pause()
