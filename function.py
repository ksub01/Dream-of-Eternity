import hero
import monsters1
import time
import random
import math
version = "0.0.1.6"
rounds1 = [35, 20, 20]


def skills():  # выбор скила
    print("Выберите навыки для прокачки\n"
          "Золотодобытчик: количество золота с мобов увеличиватся на 20%. Прокачено на *{}* => 1\n"
          "Спортсмен: Увеличивает вероятность побега на 1/20 (прокачивается до 15). Прокачено на *{}* => 2\n"
          "Познавший истину: При убийстве есть вероятность поднять защиту на 10%.\nС каждым уровнем вероятность + 10%."
          "*{}* => 3\n"
          "Усиление: Увеличивает силу на 20%. *{}* => 4\n"
          "Восставший из пепла после смерти есть вероятность, что вы поскреснете со всем здоровьем,\n"
          "но не на поле боя, каждый уровень увеличивает вероятность на 1% *{}* => 5"
          "".format(hero.heroic.gold_best, hero.heroic.escape, hero.heroic.freek, hero.heroic.dream, hero.heroic.god))
    tyu = input()
    if tyu == '1':
        hero.heroic.gold_best += 1
    elif tyu == '2':
        hero.heroic.escape += 1
        if hero.heroic.escape >= 15:
            hero.heroic.escape = 15
    elif tyu == '3':
        hero.heroic.freek += 1
    elif tyu == '4':
        hero.heroic.dream += 1
        hero.heroic.full_force = hero.heroic.force + math.ceil(hero.heroic.force * hero.heroic.dream * 2/10)
    else:
        hero.heroic.god += 1


def save():
    f1 = open('text.txt', 'r')
    f2 = open('text2.txt', 'r')
    f3 = open('text3.txt', 'r')
    n1 = f1.readline()
    n2 = f2.readline()
    n3 = f3.readline()
    n1 = n1.splitlines()
    n2 = n2.splitlines()
    n3 = n3.splitlines()
    print("Выберите слот 1 => {} 2 => {} 3 => {}".format(n1, n2, n3))
    tr1 = input()
    if tr1 == '1':
        f11 = open('text.txt', 'w')
        save_all(f11)
    elif tr1 == '2':
        f12 = open('text2.txt', 'w')
        save_all(f12)
    else:
        f13 = open('text3.txt', 'w')
        save_all(f13)


def save_all(f):
    print("Введите имя")
    name = input()
    print("Сохранение успешно")
    last = [name, hero.heroic.lvl, hero.heroic.heart_full, hero.heroic.heart, hero.heroic.attack, hero.heroic.force,
            hero.heroic.full_force,
            hero.heroic.magic, hero.heroic.magic_full, hero.heroic.magic_force, hero.heroic.defence, hero.heroic.gold,
            hero.heroic.speed, hero.heroic.exp, hero.heroic.wisdom, hero.heroic.gold_best,
            hero.heroic.escape, hero.heroic.freek, hero.heroic.dream,
            hero.heroic.god, hero.heroic.win, hero.heroic.rgold,
            hero.heroic.kills, hero.heroic.cush, hero.heroic.battle1, hero.heroic.battle2, hero.heroic.battle3]
    for frog in last:
        f.write(str(frog) + '\n')


def load():
    e1 = open('text.txt', 'r')
    e2 = open('text2.txt', 'r')
    e3 = open('text3.txt', 'r')
    n1 = e1.readline()
    n2 = e2.readline()
    n3 = e3.readline()
    n1 = n1.splitlines()
    n2 = n2.splitlines()
    n3 = n3.splitlines()
    print("Выберите слот 1 => {} 2 => {} 3 => {}".format(n1, n2, n3))
    pou = input()
    if pou == '1':
        full_load(e1)
        e1 = open('text.txt', 'w')
    elif pou == '2':
        full_load(e2)
        e1 = open('text2.txt', 'w')
    else:
        full_load(e3)
        e1 = open('text3.txt', 'w')


def full_load(e):  # поменять
    hero.heroic.lvl = (int(e.readline().strip('\n')))
    hero.heroic.heart_full = (int(e.readline().strip('\n')))
    hero.heroic.heart = (int(e.readline().strip('\n')))
    hero.heroic.attack = (int(e.readline().strip('\n')))
    hero.heroic.force = (int(e.readline().strip('\n')))
    hero.heroic.full_force = (int(e.readline().strip('\n')))
    hero.heroic.magic = (int(e.readline().strip('\n')))
    hero.heroic.magic_full = (int(e.readline().strip('\n')))
    hero.heroic.magic_force = (int(e.readline().strip('\n')))
    hero.heroic.defence = (int(e.readline().strip('\n')))
    hero.heroic.gold = (int(e.readline().strip('\n')))
    hero.heroic.speed = (int(e.readline().strip('\n')))
    hero.heroic.exp = (int(e.readline().strip('\n')))
    hero.heroic.wisdom = (int(e.readline().strip('\n')))
    hero.heroic.gold_best = (int(e.readline().strip('\n')))
    hero.heroic.escape = (int(e.readline().strip('\n')))
    hero.heroic.freek = (int(e.readline().strip('\n')))
    hero.heroic.dream = (int(e.readline().strip('\n')))
    hero.heroic.god = (int(e.readline().strip('\n')))
    hero.heroic.win = (int(e.readline().strip('\n')))
    hero.heroic.rgold = (int(e.readline().strip('\n')))
    hero.heroic.kills = (int(e.readline().strip('\n')))
    hero.heroic.cush = (int(e.readline().strip('\n')))
    hero.heroic.battle1 = (int(e.readline().strip('\n')))
    hero.heroic.battle2 = (int(e.readline().strip('\n')))
    hero.heroic.battle3 = (int(e.readline().strip('\n')))


def lvlup():  # повышение уровня
    if hero.heroic.exp >= math.ceil(hero.heroic.lvl * 50):
        hero.heroic.lvl += 1
        hero.heroic.exp = 0
        rheart1 = int(hero.heroic.heart_full/3)
        rheart2 = int(hero.heroic.heart_full / 2)
        rforce = int(hero.heroic.force/3)
        rspeed1 = int(hero.heroic.speed/10)
        rspeed2 = int(hero.heroic.speed / 5)
        rwisdom = int(hero.heroic.wisdom / 3)
        print("Ваш уровень повышен {} => {}".format(hero.heroic.lvl-1, hero.heroic.lvl))
        print("Выберите навык и повышение характеристик\n"
              "Увеличение здоровья на {}. Увеличение силы на {}. Увеличение скорости на {}. => 1\n"
              "Увеличение скорости на {}. Увеличение мудрости на {}. "
              "Увеличение силы на {}. => 2\n"
              "Увеличение мудрости на {}. "
              "Увеличение здоровья на {}. => 3"
              .format(rheart1, rforce, rspeed1, rspeed2, rwisdom, rforce, rwisdom, rheart2))
        tre = input()
        if tre == '1':
            hero.heroic.heart_full += int(hero.heroic.heart_full/3)
            hero.heroic.force += int(hero.heroic.force / 3)
            hero.heroic.speed += int(hero.heroic.speed / 10)
        elif tre == '2':
            hero.heroic.speed += int(hero.heroic.speed / 5)
            hero.heroic.wisdom += int(hero.heroic.wisdom / 3)
            hero.heroic.force += int(hero.heroic.force / 3)
        else:
            hero.heroic.wisdom += int(hero.heroic.wisdom / 3)
            hero.heroic.heart_full += int(hero.heroic.heart_full/2)
        skills()


def guide():
    print("Эта игра - пошаговая РПГ. В ней существует две локации - город и тропинки. В городе\n"
          "вы лечитесь и прокачиваетесь, а также играете в казино, а на тропинках вы убиваете монстров\n"
          "и становитесь сильнее\n\n"
          "В игре помимо здоровья есть броня, сила, атака. скорость и мудрость\n\n"
          "Броня: каждая единица уменьшает получаемый урон на единицу.\n\n"
          "Сила: каждая единица увеличивает наносимый урон на единицу.\n"
          "Отличается от атаки тем, что повышается только с уровнем\n\n"
          "Атака: каждая единица увеличивает наносимый урон на единицу.\n"
          "Отличается от силы тем, что повышается только у кузнеца\n\n"
          "Скорость: Скорость определяет кто первым нанесёт решающий удар. И то сколько ударов\n"
          "вы нанесёте. За каждые 5 очков превосходства вы или по вас наносится дополнительный "
          "удар\n\n"
          "Мудрость: Позволяет узнать больше "
          "информации о враге\n"
          "В самой игре иногда появляются паузы. Просьба никуда не жать в время их\n"
          "И пожалуй, самое важное, количество боёв на каждой дорожке ограничено. После\n"
          "достижения определённого уровня или количества боёв (смотрите в статистике) дорожка\n"
          "перестаёт быть активной"
          "Введите 1 чтобы продолжить")
    input()


def prestart():  # перед стартом
    print("Misery (название временное)\n"
          "Версия {}".format(version))
    time.sleep(3)
    print("Изменения: По сравнению с {}\nДобавлены сохранения\nКлючевые отличия:\n"
          "Здраствуйте, это альфа - тест игры Misery\n"
          "Да, прошло немало времени прежде чем я могу представить вам этот альфа - тест.\n"
          "Количество альфа - тестеров 3. Игра задумывалась\n"
          "очень хардкорной. И я надеюсь, что вам понравится это увлекательное приключение".format("0.0.1.5"))


def start():    # начало игры
    print("Вы находитесь в городе Стракт.\n"
          "Сходить к кузнецу => 1\n"
          "Отдохнуть в гостинице => 2\n"
          "Пойти в лес на охоту => 3\n"
          "Сыграть в рулетку => 4\n"
          "Статистика => 5\n"
          "Сохранение => 6\n")


def stats():
    print("Убито монстров {}".format(hero.heroic.kills))
    print("Добыто золота {}".format(hero.heroic.rgold))
    print("Раз выиграно в казино {}".format(hero.heroic.cush))
    print("Количество боёв на первой тропинке {}/{}".format(hero.heroic.battle1, rounds1[0]))
    print("Количество боёв на второй тропинке {}/{}".format(hero.heroic.battle2, rounds1[1]))
    print("Количество боёв на третей тропинке {}/{}\n".format(hero.heroic.battle3, rounds1[2]))
    print("Введите 1, чтобы вернуться")
    input()


def parameters():  # вывод характеристик
    if hero.heroic.dream != 0:
        hero.heroic.full_force = hero.heroic.force + math.ceil(hero.heroic.force * hero.heroic.dream * 2 / 10)
    else:
        hero.heroic.full_force = hero.heroic.force
    print("Ваши характеристики:\nЗдоровье {}\n"
          "Атака {}\nСила {}\nБроня {}\nСкорость {}\nМудрость {}\nЗолото"
          " {}\nОпыт {}\nУровень {}\n"
          "".format(hero.heroic.heart, hero.heroic.attack, hero.heroic.full_force,
                    hero.heroic.defence, hero.heroic.speed, hero.heroic.wisdom,
                    hero.heroic.gold,
                    hero.heroic.exp, hero.heroic.lvl))


def information(names, heart, attack, defence, speed, lvl, wisdom):  # информация о противнике
    print("Перед вами появляется {}".format(names))
    if hero.heroic.wisdom >= wisdom:
        print("Уровень {}".format(lvl))
    else:
        print("????????")
    if hero.heroic.wisdom >= wisdom + 5:
        print("Здоровье {}\nАтака {}".format(heart, attack))
    else:
        print("????????")
    if hero.heroic.wisdom >= wisdom + 10:
        print("Защита {}\nСкорость {}\n".format(defence, speed))
    else:
        print("????????")


def monster(names, heart, attack, defence, speed, gold, exp, lvl, wisdom):
    information(names, heart, attack, defence, speed, lvl, wisdom)
    print("Будете ли вы драться?\n\n"
          "Драка => 1\n"
          "Побег до начала боя => 2")
    lar = input()
    if lar == '1':
        fight(names, heart, attack, defence, speed, gold, exp, lvl, wisdom)
    else:
        print("Вы пытаетесь сбежать")
        time.sleep(1)
        f = random.randint(1, 20)
        if f > 12:
            print("Вы сбежали")
            time.sleep(1)
        else:
            print("Вам не удалось сбежать")
            time.sleep(1)
            fight(names, heart, attack, defence, speed, gold, exp, lvl, wisdom)


def fight(names, heart, attack, defence, speed, gold, exp, lvl, wisdom):  # функция атаки
    print("НАЧИНАЕТСЯ БОЙ")
    while hero.heroic.heart > 0 and heart > 0:
        information(names, heart, attack, defence, speed, lvl, wisdom)
        print("Атака => 1 "
              "Побег => 2")
        pir = input()
        der1 = (hero.heroic.attack + hero.heroic.force - defence)  # урон монстру
        der2 = (attack - hero.heroic.defence)  # урон герою
        parameters()
        if pir == '1':
            cou = 0
            cou += 1
            if speed > hero.heroic.speed:
                kr = speed
                kr -= hero.heroic.speed
                kr /= 5
            else:
                kr = hero.heroic.speed
                kr -= speed
                kr /= 5
            if kr < 1:
                kr = 1
            if hero.heroic.speed < speed:
                for t in range(int(kr)):
                    if der2 > 0:
                        der2 = math.floor(der2)
                        hero.heroic.heart -= der2
                        print("Монстр нанёс вам {} урона".format(der2))
                        if hero.heroic.heart <= 0:
                            break
                if der1 > 0 and hero.heroic.heart > 0:
                    der1 = math.floor(der1)
                    heart -= der1
                    print("Вы нанесли монстру {} урона".format(der1))
            else:
                for t in range(int(kr)):
                    if der1 > 0:
                        der1 = math.floor(der1)
                        heart -= der1
                        print("Вы нанесли монстру {} урона".format(der1))
                        if heart <= 0:
                            break
                if der2 > 0 and heart > 0:
                    der2 = math.floor(der2)
                    hero.heroic.heart -= der2
                    print("Монстр нанёс вам {} урона".format(der2))

            if der1 < 0 and der2 < 0:
                print("Вы не можете пробить броню друг друга")
                break
            if der2 <= 0:
                print("Атака монстра ненаносит вреда")
            if der1 <= 0:
                print("Ваша атака не наносит вреда")
        else:
            print("Вы пытаетесь сбежать")
            time.sleep(1)
            f = random.randint(1, 20)
            y = random.randint(1, 20)
            if f > 12 or y <= hero.heroic.escape:
                print("Вы сбежали")
                time.sleep(1)
                break
            else:
                print("Вам не удалось сбежать")
                time.sleep(1)
                if der2 > 0:
                    der2 = math.floor(der2)
                    hero.heroic.heart -= der2
                    print("Монстр нанёс вам {} урона".format(der2))
    if heart <= 0:
        hero.heroic.kills += 1
        rewards(gold, exp)
    if hero.heroic.heart <= 0:
        print("Вы проиграли. Ваши внутренние органы размазаны по стене, а монстры издеваются над вашим трупом")
        input()


def rewards(gold, exp):
    if hero.heroic.gold_best != 0:
        tp = gold + math.ceil(gold * hero.heroic.gold_best * 2 / 10)
        hero.heroic.gold = hero.heroic.gold + tp
        hero.heroic.rgold += hero.heroic.gold + tp
        print("Вы получаете {} золота и {} опыта".format(tp, exp))
    else:
        hero.heroic.gold += gold
        hero.heroic.rgold += hero.heroic.gold
        print("Вы получаете {} золота и {} опыта".format(gold, exp))
    hero.heroic.exp += exp
    if hero.heroic.freek >= 1:
        y = random.randint(1, 10)
        if hero.heroic.freek >= y:
            print("Ваша защита увеличилась на 10%")
            hero.heroic.defence = hero.heroic.defence + (hero.heroic.defence / 10)
    if gold == 1500:  # убрать
        print("Вы победили!")


def forest():  # монстры
    print("Вы входите в лес полный опасностей и приключений."
          " Со сложностью подземелий растёт и сложность наград\n"
          "Выберите тропинку\n"
          "Нубовская => 1\n"
          "Простая => 2\n"
          "Средняя => 3\n"
          "Сложная => 4\n"
          "Очень сложная => 5\n"
          "Божественная => 6\n"
          "Вернуться => 7")
    print("Ваша цель: убийство сильнейшего монстра - Ледяного дракона\n")
    t = input()
    if t == '1' and hero.heroic.battle1 < rounds1[0] and hero.heroic.lvl <= 10:
        print("Вы попадаете в лес полный опасностей и загадок")
        time.sleep(3)
        res = random.randint(1, 20)
        if 1 <= res <= 6:
            monster(monsters1.goblin1.names, monsters1.goblin1.heart, monsters1.goblin1.attack,
                    monsters1.goblin1.defence,
                    monsters1.goblin1.speed, monsters1.goblin1.gold,
                    monsters1.goblin1.exp, monsters1.goblin1.lvl, monsters1.goblin1.wisdom)
            hero.heroic.battle1 += 1
        elif 7 <= res <= 8:
            monster(monsters1.goblin_master1.names, monsters1.goblin_master1.heart, monsters1.goblin_master1.attack,
                    monsters1.goblin_master1.defence,
                    monsters1.goblin_master1.speed, monsters1.goblin_master1.gold,
                    monsters1.goblin_master1.exp, monsters1.goblin_master1.lvl, monsters1.goblin_master1.wisdom)
            hero.heroic.battle1 += 1
        elif 9 <= res <= 13:
            monster(monsters1.goblin_shaman1.names, monsters1.goblin_shaman1.heart, monsters1.goblin_shaman1.attack,
                    monsters1.goblin_shaman1.defence,
                    monsters1.goblin_shaman1.speed, monsters1.goblin_shaman1.gold,
                    monsters1.goblin_shaman1.exp, monsters1.goblin_shaman1.lvl, monsters1.goblin_shaman1.wisdom)
            hero.heroic.battle1 += 1
        elif 14 <= res <= 15:
            monster(monsters1.orc1.names, monsters1.orc1.heart, monsters1.orc1.attack,
                    monsters1.orc1.defence, monsters1.orc1.speed,
                    monsters1.orc1.gold, monsters1.orc1.exp, monsters1.orc1.lvl, monsters1.orc1.wisdom)
            hero.heroic.battle1 += 1
        elif 16 <= res <= 17:
            monster(monsters1.bloody_orc.names, monsters1.bloody_orc.heart, monsters1.bloody_orc.attack,
                    monsters1.bloody_orc.defence, monsters1.bloody_orc.speed,
                    monsters1.bloody_orc.gold,
                    monsters1.bloody_orc.exp, monsters1.bloody_orc.lvl, monsters1.bloody_orc.wisdom)
            hero.heroic.battle1 += 1
        elif 18 <= res <= 19:
            monster(monsters1.shake.names, monsters1.shake.heart, monsters1.shake.attack,
                    monsters1.shake.defence, monsters1.shake.speed,
                    monsters1.shake.gold,
                    monsters1.shake.exp, monsters1.shake.lvl, monsters1.shake.wisdom)
            hero.heroic.battle1 += 1
        else:
            monster(monsters1.gargoyle1.names, monsters1.gargoyle1.heart, monsters1.gargoyle1.attack,
                    monsters1.gargoyle1.defence, monsters1.gargoyle1.speed, monsters1.gargoyle1.gold,
                    monsters1.gargoyle1.exp, monsters1.gargoyle1.lvl, monsters1.gargoyle1.wisdom)
            hero.heroic.battle1 += 1
    elif t == '1' and (hero.heroic.lvl > 10 or hero.heroic.battle1 >= rounds1[0]):
        print("Дорожка больше не доступна")
    if t == '2' and (hero.heroic.lvl < 20 and hero.heroic.battle2 <= rounds1[1]):
        print("Вы оказались в пустыне. Каждый бой снимает вам 50% здоровья")
        time.sleep(3)
        res = random.randint(1, 20)
        if 1 <= res <= 6:
            monster(monsters1.sandsnake1.names, monsters1.sandsnake1.heart, monsters1.sandsnake1.attack,
                    monsters1.sandsnake1.defence,
                    monsters1.sandsnake1.speed, monsters1.sandsnake1.gold,
                    monsters1.sandsnake1.exp, monsters1.sandsnake1.lvl, monsters1.sandsnake1.wisdom)
            hero.heroic.battle2 += 1
        elif 7 <= res <= 8:
            monster(monsters1.scorpio1.names, monsters1.scorpio1.heart, monsters1.scorpio1.attack,
                    monsters1.scorpio1.defence,
                    monsters1.scorpio1.speed, monsters1.scorpio1.gold,
                    monsters1.scorpio1.exp, monsters1.scorpio1.lvl, monsters1.scorpio1.wisdom)
            hero.heroic.battle2 += 1
        elif 9 <= res <= 10:
            monster(monsters1.vulture1.names, monsters1.vulture1.heart, monsters1.vulture1.attack,
                    monsters1.vulture1.defence,
                    monsters1.vulture1.speed, monsters1.vulture1.gold,
                    monsters1.vulture1.exp, monsters1.vulture1.lvl, monsters1.vulture1.wisdom)
            hero.heroic.battle2 += 1
        elif 10 <= res <= 13:
            monster(monsters1.mad_fox1.names, monsters1.mad_fox1.heart, monsters1.mad_fox1.attack,
                    monsters1.mad_fox1.defence, monsters1.mad_fox1.speed,
                    monsters1.mad_fox1.gold, monsters1.mad_fox1.exp, monsters1.mad_fox1.lvl, monsters1.mad_fox1.wisdom)
            hero.heroic.battle2 += 1
        elif 14 <= res <= 15:
            monster(monsters1.mummy1.names, monsters1.mummy1.heart, monsters1.mummy1.attack,
                    monsters1.mummy1.defence, monsters1.mummy1.speed,
                    monsters1.mummy1.gold,
                    monsters1.mummy1.exp, monsters1.mummy1.lvl, monsters1.mummy1.wisdom)
            hero.heroic.battle2 += 1
        elif 16 <= res <= 17:
            monster(monsters1.sand_beetle1.names, monsters1.sand_beetle1.heart, monsters1.sand_beetle1.attack,
                    monsters1.sand_beetle1.defence, monsters1.sand_beetle1.speed,
                    monsters1.sand_beetle1.gold,
                    monsters1.sand_beetle1.exp, monsters1.sand_beetle1.lvl, monsters1.sand_beetle1.wisdom)
            hero.heroic.battle2 += 1
        else:
            monster(monsters1.lord_desert1.names, monsters1.lord_desert1.heart, monsters1.lord_desert1.attack,
                    monsters1.lord_desert1.defence, monsters1.lord_desert1.speed, monsters1.lord_desert1.gold,
                    monsters1.lord_desert1.exp, monsters1.lord_desert1.lvl, monsters1.lord_desert1.wisdom)
            hero.heroic.battle2 += 1
        hero.heroic.heart = hero.heroic.heart - int(hero.heroic.heart/10)*5
    elif t == '2' and (hero.heroic.lvl > 20 or hero.heroic.battle2 > rounds1[1]):
        print("Дорожка больше не доступна")
    if t == '3' and (hero.heroic.lvl < 30 and hero.heroic.battle3 <= rounds1[2]):
        print("Вы оказались среди снега. Каждый ваш шаг даётся с трудом, поэтому вам пришлось снять "
              "броню")
        time.sleep(3)
        r = hero.heroic.defence
        hero.heroic.defence = 0
        time.sleep(3)
        res = random.randint(1, 20)
        if 1 <= res <= 6:
            monster(monsters1.polar_bear1.names, monsters1.polar_bear1.heart, monsters1.polar_bear1.attack,
                    monsters1.polar_bear1.defence,
                    monsters1.polar_bear1.speed, monsters1.polar_bear1.gold,
                    monsters1.polar_bear1.exp, monsters1.polar_bear1.lvl, monsters1.polar_bear1.wisdom)
            hero.heroic.battle3 += 1
        elif 7 <= res <= 8:
            monster(monsters1.snow_leopard1.names, monsters1.snow_leopard1.heart, monsters1.snow_leopard1.attack,
                    monsters1.snow_leopard1.defence,
                    monsters1.snow_leopard1.speed, monsters1.snow_leopard1.gold,
                    monsters1.snow_leopard1.exp, monsters1.snow_leopard1.lvl, monsters1.snow_leopard1.wisdom)
            hero.heroic.battle3 += 1
        elif 9 <= res <= 10:
            monster(monsters1.ice_warlock1.names, monsters1.ice_warlock1.heart, monsters1.ice_warlock1.attack,
                    monsters1.ice_warlock1.defence,
                    monsters1.ice_warlock1.speed, monsters1.ice_warlock1.gold,
                    monsters1.ice_warlock1.exp, monsters1.ice_warlock1.lvl, monsters1.ice_warlock1.wisdom)
            hero.heroic.battle3 += 1
        elif 10 <= res <= 13:
            monster(monsters1.yeti1.names, monsters1.yeti1.heart, monsters1.yeti1.attack,
                    monsters1.yeti1.defence, monsters1.yeti1.speed,
                    monsters1.yeti1.gold, monsters1.yeti1.exp, monsters1.yeti1.lvl, monsters1.yeti1.wisdom)
            hero.heroic.battle3 += 1
        elif 14 <= res <= 15:
            monster(monsters1.scribe1.names, monsters1.scribe1.heart, monsters1.scribe1.attack,
                    monsters1.scribe1.defence, monsters1.scribe1.speed,
                    monsters1.scribe1.gold,
                    monsters1.scribe1.exp, monsters1.scribe1.lvl, monsters1.scribe1.wisdom)
            hero.heroic.battle3 += 1
        elif 16 <= res <= 17:
            monster(monsters1.snow_queen1.names, monsters1.snow_queen1.heart, monsters1.snow_queen1.attack,
                    monsters1.snow_queen1.defence, monsters1.snow_queen1.speed,
                    monsters1.snow_queen1.gold,
                    monsters1.snow_queen1.exp, monsters1.snow_queen1.lvl, monsters1.snow_queen1.wisdom)
            hero.heroic.battle3 += 1
        else:
            monster(monsters1.ice_dragon1.names, monsters1.ice_dragon1.heart, monsters1.ice_dragon1.attack,
                    monsters1.ice_dragon1.defence, monsters1.ice_dragon1.speed, monsters1.ice_dragon1.gold,
                    monsters1.ice_dragon1.exp, monsters1.ice_dragon1.lvl, monsters1.ice_dragon1.wisdom)
            hero.heroic.battle3 += 1
        hero.heroic.defence = r
    # elif t == '3' and (hero.heroic.lvl > 30 or hero.heroic.battle3 >= rounds1[2]):
        # print("Дорожка больше не доступна")


def roulette():  # казино
    while 1:
        print("Здраствуйте. Вы находитесь в казино. Выберите варианты игры\n"
              "Умножь золото => 1 "
              "Выбей оружие => 2 "
              "Стань богом => 3 "
              "Вернуться => 4")
        rt = input()
        if rt == '1':
            print("Правила игры просты.\nЕсли выпадает 1 вы умножаете ваше золото на 10%. "
                  "Если выпадает 2 теряете 10%")
            print("Согласны?\n"
                  "Да => 1 "
                  "Нет => 2")
            re = input()
            if re == '1':
                if hero.heroic.gold >= 10:
                    print("Готовы")
                    print("Итаааак. Выпало")
                    time.sleep(3)
                    y = random.randint(1, 20)
                    if 1 <= y <= 10:
                        print(1)
                        k = int(hero.heroic.gold/10)
                        hero.heroic.gold += k
                        print("Вы получили {} золота".format(k))
                        hero.heroic.cush += 1
                    else:
                        print(2)
                        k = hero.heroic.gold / 10
                        hero.heroic.gold -= k
                        print("Вы потеряли {} золота".format(k))
                else:
                    print("У вас не хватает денег")
                    time.sleep(1)
            if re == '2':
                print("До свидания")
        if rt == '2':
            print("В этой игре вы можете выиграть улучшение на атаку. Причём каждый выигрыш, полученная при\n"
                  "Выигрыше атака повышается вот так 1 - 2 - 3 - 4 - 5 ...\n"
                  "Вероятность выигрыша 1/100\n"
                  "Вам должно выпасть 5\n"
                  "Цена игры 10 золотых "
                  "Согласны "
                  "Да => 1 "
                  "Нет => 2")
            yu = input()
            if yu == '1':
                if hero.heroic.gold >= 10:
                    hero.heroic.gold -= 10
                    print("Начнём игру\n"
                          "Итаак. Вам выпало\n")
                    time.sleep(3)
                    win1 = random.randint(1, 100)
                    print("Вам выпало {}".format(win1))
                    if win1 == 5:
                        print("Вы выиграли"
                              "Ваша атака повышена на {}".format(hero.heroic.win))
                        hero.heroic.win += 1
                        hero.heroic.attack += hero.heroic.win
                        hero.heroic.cush += 1
                    else:
                        print("Вы проиграли")
                else:
                    print("У вас не хватает денег")
                    time.sleep(1)
            else:
                print("До свидания")
        if rt == '3':
            print("Правила просты, если выпадает число 1 вы становитесь богом\n"
                  "Ваши характеристики становятся равными 4832942934793247293\n")
            print("Ставка в этой игре 1 золото\n"
                  "Согласны? Да => 1 Нет => 2\n")
            jr = input()
            if jr == '1':
                if hero.heroic.gold >= 1:
                    hero.heroic.gold -= 1
                    print("Начнём игру")
                    print("Итак, выпало")
                    time.sleep(3)
                    e = random.randint(1, 1000000000000000)
                    if e == 1:
                        print(1)
                        hero.heroic.defence = 4832942934793247293
                        hero.heroic.attack = 4832942934793247293
                        hero.heroic.heart_full = 4832942934793247293
                        hero.heroic.force = 4832942934793247293
                        hero.heroic.magic_full = 4832942934793247293
                        hero.heroic.magic_force = 4832942934793247293
                        hero.heroic.speed = 4832942934793247293
                        hero.heroic.cush += 1
                    else:
                        print(2)
                        print("Вам не повезло")
                else:
                    print("У вас не хватает денег")
                    time.sleep(1)
            else:
                print("До свидания")
        if rt == '4':
            break
