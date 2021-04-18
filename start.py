"""Тут содержатся все функции, запускаемые при первом запуске игры"""

from colorama import Fore, Style

import information
import player

STORY_MESSAGE = Fore.YELLOW + Style.DIM


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