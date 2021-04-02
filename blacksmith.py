import hero
import items
import time


def buy_def(names, gold, defence):
    if hero.heroic.gold >= gold:
        hero.heroic.gold -= gold
        hero.heroic.defence += defence
        print("Вы купили {}\n".format(names))
        time.sleep(1)
    else:
        print("У вас не хватает денег\n")
        time.sleep(1)


def buy_at(names, gold, attack):
    if hero.heroic.gold >= gold:
        hero.heroic.gold -= gold
        hero.heroic.attack += attack
        print("Вы купили {}\n".format(names))
        time.sleep(1)
    else:
        print("У вас не хватает денег\n")
        time.sleep(1)


def blacksmith():
    while 1:
        print("Здраствуй, хочешь чего нибудь купить?\n"
              "Оружие => 1\n"
              "Броня => 2\n"
              "Зелья => 3\n"
              "Вернуться => 4\n")
        h = input()
        if h == '1':
            print("{} ({} монет) + {} атаки  => 1\n"
                  "{} ({} монет) + {} "
                  "атаки => 2\n"
                  "{} ({} монет) + {} атаки => 3\n"
                  "Вернуться => 4".format(items.stick1.names, items.stick1.gold,
                                          items.stick1.attack, items.drina1.names, items.drina1.gold,
                                          items.drina1.attack, items.sword1.names,
                                          items.sword1.gold, items.sword1.attack))
            c = input()
            if c == '1':
                buy_at(items.stick1.names, items.stick1.gold,
                       items.stick1.attack)
            elif c == '2':
                buy_at(items.list1.names, items.list1.gold,
                       items.stick1.attack)
            elif c == '3':
                buy_at(items.sword1.names, items.sword1.gold,
                       items.sword1.attack)
            else:
                continue
        if h == '2':
            print("{} ({} монет) + {} защита  => 1\n"
                  "{} ({} монет) + {} "
                  "защиты => 2\n"
                  "{} ({} монет) + {} защита  => 3\n"
                  "{} ({} монет) + {} защита  => 4\n"
                  "Вернуться => 5".format(items.cap1.names, items.cap1.gold,
                                          items.cap1.defence, items.list1.names, items.list1.gold,
                                          items.list1.defence, items.tank1.names, items.tank1.gold,
                                          items.tank1.defence, items.door1.names, items.door1.gold,
                                          items.door1.defence,))
            v = input()
            if v == '1':
                buy_def(items.cap1.names, items.cap1.gold,
                        items.cap1.defence)
            elif v == '2':
                buy_def(items.list1.names, items.list1.gold,
                        items.list1.defence)
            elif v == '3':
                buy_def(items.tank1.names, items.tank1.gold, items.tank1.defence)
            elif v == '4':
                buy_def(items.door1.names, items.door1.gold, items.door1.defence)
            else:
                continue
        else:
            break
