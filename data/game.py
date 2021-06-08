from colorama import Fore, Style


import data.world.creature as world
import data.battle.battle as battle
import data.shop.blacksmith as blacksmith
import data.shop.casino as casino
import data.shop.hotel as hotel

import random
import time

INVENTORY_MESSAGE = Fore.GREEN + Style.BRIGHT
DIE_MASSAGE = Fore.RED + Style.BRIGHT
HELP_MESSAGE = Fore.CYAN + Style.DIM
TOWN_MESSAGE = Style.DIM + Fore.LIGHTYELLOW_EX
MENU_TOWN_MASSAGE = Fore.LIGHTBLUE_EX
STORY_MESSAGE = Fore.YELLOW + Style.DIM
MESSAGE_DIALOGUE = Fore.GREEN
LVL_UP_MESSAGE = Fore.YELLOW + Style.BRIGHT
MESSAGE_DAMAGE = Fore.GREEN + Style.DIM
MESSAGE_HEAL = Fore.MAGENTA + Style.BRIGHT


class Town:
    """Город"""
    @staticmethod
    def if_lvl_up(player):
        """В городе отображает строку о возможности перейти на новый уровень. Значения берутся из массива опыта exp
        в lvl_up"""
        if player.parameter.test_lvl_up():
            print(INVENTORY_MESSAGE + "Поспите, чтобы повысить ваш уровень\n")

    @staticmethod
    def town_places():
        """Постоянно высвечивается в городе для отображения мест, куда игрок может пойти"""
        print(TOWN_MESSAGE + 'Вы находитесь в городе Аркона, последнем оплоте человечества' + '\n')
        print(MENU_TOWN_MASSAGE + '╍' * 40)
        print('🛖 ➔ 1\n'
              '🛌 ➔ 2\n'
              '🌲 ➔ 3\n'
              '🎲 ➔ 4\n'
              '🏡 ➔ 5')
        print('╍' * 40)


class Game:
    """Основные функциии для игры"""
    def __init__(self):
        self.town = Town()
        self.player = None

    @staticmethod
    def pause():
        """Пауза после отображения текста, чтобы игрок успел прочитать"""
        input(Style.RESET_ALL + HELP_MESSAGE + 'Нажмите Enter\n' + Style.RESET_ALL)

    def goodbye(self):
        """Прощание с игроком в любой ситуации"""
        print(HELP_MESSAGE + 'До свидания' + Style.RESET_ALL)
        self.pause()

    @staticmethod
    def end_game():
        print(DIE_MASSAGE + 'Вы проиграли. Озирис уничтожил мир, а Аркона пала.')

    def about(self):
        """Отображение имени игры и её версии перед её началом, частично копирует README (Github)"""
        version = '0.1.1.6.0'
        print(Fore.MAGENTA + Style.BRIGHT + 'Dream of Eternity')
        print(Fore.MAGENTA + Style.DIM + 'Версия {}'.format(version))
        self.pause()

    def prologue(self):
        """Вывод начальной информации о мире игры перед её началом"""
        print(STORY_MESSAGE + 'Здраствуй, великий герой Мрака, призванный спасти наш мир от великой угрозы.\n'
                              'Опасность возникла внезапно, когда великий дракон Озирис поселился в нашем мире.\n'
                              'Он послал на нас орды монстров, которые грабили и убивали. Прошло время, Озирис '
                              'успокоился '
                              'и настал мир,\n'
                              'но внезапно, всё возобновилось, страдания и смерти снова вернулись. '
                              'Сейчай люди умирают и надежды уже нет.\n'
                              'Использовав последние запасы кристалов пробуждения мы призвали трёх великих'
                              ' геров Страха,\n'
                              'имевщих девять жизней, которые вскоре пали под\n'
                              'натиском дракона и его приспешников, уничтожав их и захватив\n'
                              'их сферы пробуждения Озирис лишь усилил свой напор.\n'
                              'Надежды уже не осталось, но великая жрица Элиза воспользовалась жертвенной магией\n'
                              'для призыва ещё одного героя - тебя. По правде сказать шансов у тебя немного и попытка '
                              'всего одна\n'
                              'Мы не надеямся на твою победу, но возможно благодаря тебе мы'
                              ' сможем прожить чуть дольше\n'
                              'В любом случае, у нас не будет шанса против Озириса, если мы не убьём 10 его верных '
                              'приспешников:\n'
                              'Варганиса - повелителя леса Смерти, Ламура - обитателя пустыни, Сноуфейри - жительницу '
                              'снегов,\n'
                              'Варлиту, захватившую океан, Металику - королеву парящих островов, Гримура, жаждующего '
                              'порчи, Тераэль,\n'
                              'находящуюся в недрах, Виризиса, уничтожившего племя Ваши, Некрола,'
                              ' воскресающего и Ларита,\n'
                              'повелителя Бездны, который помог Озирису уничтожить всё человечесто,'
                              ' и который уничтожил '
                              'источник\n'
                              'Исполнения. Мы, основатели, сделали всё что смогли, прости нас, что обрекаем тебя на '
                              'верную смерть')
        self.pause()

    def choice_class(self):
        """Выбор класса в начале игры для присвоения словаря навыков игроку. Словарь находится в hero_stats"""
        while True:
            print(Style.RESET_ALL + Fore.CYAN + 'Выберите класс:' + Style.RESET_ALL)
            choice = input(Fore.YELLOW + 'Повелитель ➔ 1 (воин, владеющий силой и уничтожающий '
                                         'монстров мечом)\n' + Style.RESET_ALL)
            if choice == '1':
                self.player = world.Overlord(self)
                self.player.parameter.set_name()
                break

    def start_game(self):
        """Функции, включающиеся перед самым запуском игры"""
        self.about()
        self.prologue()

    def setting(self):
        """Выбор класса перед началом игры"""
        self.choice_class()

    @staticmethod
    def not_enough_money():
        print(MESSAGE_DIALOGUE + 'У вас недостаточно денег' + Style.RESET_ALL)
        Game.pause()

    def playing_loop(self):
        """Основной цикл игры, с действиями внутри города и боями"""
        while self.player.parameter.alive():
            self.player.parameter.display()
            self.town.town_places()
            self.town.if_lvl_up(self.player)
            choice = input()
            if choice == '1':
                shop = blacksmith.Blacksmith(self.player, self)
                shop.display()
            elif choice == '2':
                heal = hotel.Hotel(self.player, self)
                heal.dialogue()
            elif choice == '3':
                event = random.randint(1, 5)
                if event == 5:
                    event = 2
                else:
                    event = 1
                fight = battle.Dungeon(event, self)
                fight.dungeon(self.player)
            elif choice == '4':
                start = casino.Casino(self.player, self)
                start.dialogue()
            elif choice == '5':
                self.player.inventory.display()
        else:
            self.end_game()

    def start(self):
        self.start_game()
        self.setting()
        self.playing_loop()


class Location:
    pass
