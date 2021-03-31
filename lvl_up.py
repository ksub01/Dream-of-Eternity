import hero

passive_skills = ['Демонический облик']
exp = [0, 100, 500, 2500, 7500, 17000, 26000, 52000, 104000, 208000, 512000, 1024000]


def start():
    """Функция, которой герой выбирает какие параметры прокачивать, не сделано для всех классов"""
    hero.get_lvl(1)
    print("Выберите две характеристики для повышения")
    print('Введите первую')
    parametr()
    print('Введите вторую')
    parametr()


def parametr():
    """Вы выбираете характеристику, она повышается. Ничего не возвращает"""
    while 1:
        number_characteristic = int(input('Здоровье + {} -> 1\n'
                                          'Сила + {} -> 2\n'
                                          'Ловкость + {} -> 3\n'
                                          'Мудрость + {} -> 4\n'
                                          ''.format(10 * (hero.parameter['lvl'] - 1),
                                                    2 * (hero.parameter['lvl'] - 1),
                                                    3 * (hero.parameter['lvl'] - 1),
                                                    4 * (hero.parameter['lvl'] - 1))))
        if number_characteristic == 1:
            hero.heart_full_upgrade(10 * (hero.parameter['lvl'] - 1))
            break
        elif number_characteristic == 2:
            hero.force_upgrade(2 * (hero.parameter['lvl'] - 1))
            break
        elif number_characteristic == 3:
            hero.dexterity_upgrade(3 * (hero.parameter['lvl'] - 1))
            break
        elif number_characteristic == 4:
            hero.wisdom_upgrade(4 * (hero.parameter['lvl'] - 1))
            break
        else:
            pass


def choice_skills():  # выбор скила
    """Один из этих словарей, в зависимости от класса, присваивается словарю nav, при старте игры
    Навык характеризуется списком следующим образом 1ая цифра - уровень прокачки навыка от 0 до 3,
    2ая цифра - прокачка эффекта во всех четырёх состояниях навыка: не прокачен, первого уровня, второго,
    третьего. 3ая цифра - то, под каким номером он выводился игроку"""
    while 1:
        display_skills()
        if hero.parameter['name'] == 'Повелитель':
            # переход в меню выбора навыка
            choice_lord_skills()
            break
        else:
            print('Не готово')
            pass


def display_skills():
    """Отображение вкаченных навыков и уровней прокачки для всех классов"""
    if hero.parameter['name'] == 'Повелитель':
        if 'Длань господа' in hero.nav_hero_have:
            hand_of_god = hero.nav_hero_have['Длань господа'][0]
        else:
            hand_of_god = 0
        print('1 Длань господа *{}*: вы наносите мощный удар, который в [5, 10, 15] раз\n'
              'больше вашей атаки. Сила зависит от прокачки. Один раз за бой'.format(hand_of_god))

        if 'Божественное провиденье' in hero.nav_hero_have:
            divine_providence = hero.nav_hero_have['Божественное провиденье'][0]
        else:
            divine_providence = 0
        print('2 Божественное провиденье *{}*: Увеличивает вашу атаку на [5, 10, 20]'
              ''.format(divine_providence))

        if 'Демонический облик' in hero.nav_hero_have:
            demon_outlook = hero.nav_hero_have['Демонический облик'][0]
        else:
            demon_outlook = 0
        print('3 Демонический облик *{}*: Ваша атака увеличивается в 2 раза,\n'
              'но вы возвращаете [50, 40, 30] процентов урона себе'.format(demon_outlook))
    else:
        print('Для других классов не готово')


def choice_lord_skills():
    """Выбор навыка лорда в зависимости от цифры. Передаётся цифра навыка, который игрок хочет вкачать"""
    while 1:
        number = int(input('Какой навык прокачать?\n'))
        if number == 1:
            if upgrade_nav('Длань господа', [0, {1: 5, 2: 10, 3: 15}]) == 1:
                break
            else:
                pass
        elif number == 2:
            if upgrade_nav('Божественное провиденье', [0, {1: 5, 2: 10, 3: 20}]) == 1:
                break
            else:
                pass
        elif number == 3:
            if upgrade_nav('Демонический облик', [0, [50, 40, 30]]) == 1:
                break
            else:
                pass
        else:
            pass


def upgrade_nav(name, grade):
    """Даёт полный интерфейс к прокачке данного навыка, подаётся имя навыка и его прокачка. Возвращает удалась прокачка
    или нет. Тут подавляется прокачка выше 3его уровня
    Возвращает: удалась или не удалась прокачка"""
    # проверяет, есть ли в имеющихся навыках данный навык
    if name in hero.nav_hero_have:
        # проверяет, можно ли его ещё прокачивать
        if hero.nav_hero_have[name][0] < 3:
            hero.upgrade_lvl_nav(name)
            return 1
        else:
            print('Навык {} нельзя больше прокачать'.format(name))
            return 0
    else:
        hero.append_new_nav(name, grade)
        return 1


""" 4. Один раз в день воскрешает с полным здоровьем и увеличивает атаку в [2, 3, 4] раза до конца боя
    5. Даёт возможность защищаться на [65, 70, 75] процентов
    6. Увеличивает эффект мечей в [2, 3, 4] раза
    7. Даёт возможность покупать [1, 2, 3] камня силы на этаж (помогает ломать стену)
    8. С новым уровнем получаешь на [1, 2, 3] сундука больше
    9. Даёт возможность покупать зелья в подзеиелье но в [30, 20, 10] раз дороже
    10. Даёт скидку у торговца грёзами [5, 10, 15]
    11. Добавляет души [обычной, мифической, легендарной] редкости в сундук
    12. Даёт одну из трёх легендарных вещей [камень возвращения, камень воскрешения, 
    13. Высасывание жизни со всех монстров
    14. Увеличивает количество золота
    15. Увеличивает количество опыта
    16. Убивает всех монстров кроме боссов, но снижает максимальное здоровье на [15, 10, 5] процентов
    17. Пропускаешь три удара, но возвращаешь каждому урон равный нанесённому вам, но в [0.5, 0.7, 1] раз больше
    18. Снижает стоимость улучшений мечей
    19. Уменьшает стоимость мечей
    20. Даёт возможность вселять душу в [кольцо, доспехи, плащ]
    21. Цветы для хила
    22. Взгляд бед, уменьшает атаку всех монстров
    23. Доспехи отчаяния. Принимают часть урона
    24. Вместо обычной атаки вы наносите [2, 3, 4]
    25. Вы раскапываете меч каждые [15, 10, 5] уровней
    26. Даёт возможность создавать зелья самому
    27. С вероятностью 10 процентов вы гарантированно в бою получаете сундук
    28. Увеличивает вероятность выпадения души
    29. Два меча
    30. Обмен со здоровьем проивника [1, 2, 3] раза в день
    31. Приносит три меча того же уровня в жертву ради улучшения
    Секретные навыки 8
    32. Подкоп в подземелье
    33. Минимальный уровень у всего оружия
    34. Ошеломление у противников
    35. Покупка всех вещей дороже
    36. Третий меч 
    37. Демонический облик, перевоплащение без опыта и денег
    38. Перемотка времения
    39. 

print("Выберите навык:\n"
          "1.1 Длань господа.\n Ва наносите мощный удар равный"
          "(300, 400, 500)% вашего урона. Уровень: {}".format(hero.nav['Длань господа'][0]))
    print("1.2.1 Сила ветра. Наносит {} быстрых ударов")
    print("1.2.2 Создание доспехов и оружия. Вы можете создавать оружие {} уровня")
    print("1.3.1 Змеиная кожа. Вы восстанавливаете {} урона от нанесённого урона")
    print("2.1 Божественное провиденье. Увеличивает силу и атаку на {}")
    print("2.2.1 Черепаший панцирь. Увеличивает защиту на {}")
    print("2.2.2 Драконья ярость. Преобразует ярость в здоровье {}")
    print("2.3.1 Духовная близость. Увеличение вероятности получение духа монстра {}")
    print("3.1 Демонический облик. Во время действия способности\n"
          " атака увеличивается в 2 раза, вам возвращется весь нанесённый урон{}")
    print("3.2.1 Прозрение. Увеличивает мудрость в {} раза")
    print("3.2.2 Иглы льда. Вас пронзают {} игл. Увеличивает атаку в {} раза")
    ki = input()
    if ki == '1.1' and hero.nav['Длань господа'][hero.nav['Длань господа'][0]] < 3:
        hero.nav['Длань господа'][0] += 1
"""