"""Тут содержатся все функции, запускаемые при первом запуске игры"""

import hero
import information


def about():
    """Отображение имени игры и её версии перед её началом"""
    version = "0.1.1.2 - отредактирована бОльшая часть кода для удобочитаемости, убраны вылеты при неправильной цифре"
    print("Dream of Eternity\n"
          "Версия {}".format(version))


def prologue():
    """Вывод начальной информации о мире игры перед её началом"""
    information.pause()
    # вся информация
    print('Здраствуй, великий герой Мрака, призванный спасти наш мир от великой угрозы.\n'
          'Опасность возникла внезапно, когда великий дракон Озирис поселился в нашем мире.\n'
          'Он послал на нас орды монстров, которые грабили и убивали. Прошло время, Озирис успокоился и настал мир,\n'
          'но внезапно, всё возобновилось, страдания и смерти снова вернулись. '
          'Сейчай люди умирают и надежды уже нет.\n'
          'Использовав последние запасы кристалов пробуждения мы призвали трёх великих геров Страха,\n'
          'имевщих девять жизней, которые вскоре пали под\n'
          'натиском дракона и его приспешников, уничтожав их и захватив\n'
          ' их сферы пробуждения Озирис лишь усилил свой напор.\n'
          'Надежды уже не осталось, но великая жрица Элиза воспользовалась жертвенной магией\n'
          'для призыва ещё одного героя - тебя. По правде сказать шансов у тебя немного и попытка всего одна\n'
          'Мы не надеямся на твою победу, но возможно благодаря тебе мы сможем прожить чуть дольше\n'
          'В любом случае, у нас не будет шанса против Озириса, если мы не убьём 10 его верных приспешников:\n'
          'Варганиса - повелителя леса Смерти, Ламура - обитателя пустыни, Сноуфейри - жительницу снегов,\n'
          'Варлиту, захватившую океан, Металику - королеву парящих островов, Гримура, жаждующего порчи, Тераэль,\n'
          'находящуюся в недрах, Виризиса, уничтожившего племя Ваши, Некрола, воскресающего и Ларита,\n'
          'повелителя Бездны, который помог Озирису уничтожить всё человечесто, и который уничтожил источник\n'
          'Исполнения. Мы, основатели, сделали всё что смогли, прости нас, что обрекаем тебя на верную смерть')
    input('Нажмите Enter\n')


def guide():
    """Вывод информации о том, как играть для новичков, эта информация выводится перед началом игры"""
    ans = input("Хотите пройти обучение? Да => 1 Нет => 2\n")
    if ans == '1':
        print("Пока пусто")
        information.pause()
    else:
        pass


def choice_class():
    """Выбор класса в начале игры для присвоения словаря навыков игроку. Словарь находится в hero_stats"""
    while 1:
        # выбор класса
        class2 = input("Выберите класс:\n"
                       "Повелитель => 1 (воин, владеющий силой и уничтожающий монстров мечом)\n"
                       "Ловец тени => 2 (вор, владеющий воровством и кинжалами)\n"
                       "Мудрец => 3 (маг, последний носитель благословения в мире)\n\n")
        if class2 == '1':
            # присвоение словаря
            hero.parameter_choice(hero.parameter_lord)
            break
        elif class2 == '2':
            # присвоение словаря
            hero.parameter_choice(hero.parameter_shadow_catcher)
            break
        elif class2 == '3':
            # присвоение словаря
            hero.parameter_choice(hero.parameter_sage)
            break
        else:
            pass
