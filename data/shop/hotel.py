from colorama import Fore, Style


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


class Hotel:
    def __init__(self, player, session):
        self.player = player
        self.session = session

    price_sleep = [0, 5, 40, 100, 400, 800, 1200, 1700, 2100, 2600, 3000]

    def dialogue(self):
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
                                                             'Нет ➔ 2\n'.format(self.price_sleep[1]))
            if ans == '1':
                if self.player.parameter.gold_spending(self.price_sleep[1]):
                    self.sleep()
            self.session.goodbye()
            break

    def sleep(self):
        """Моделирует поведение сна, запускаются все функции, которые нужно запускать во время сна
        (повышение уровня и восстановление параметров). Этот модуль и есть полная эмуляция поведения сна.
        Его можно использовать без интефейса гостиницы"""
        self.test_lvl()
        self.recovery_all()

    def recovery_all(self):
        """Восстановление потраченных параметров во время сна"""
        need_heal = self.player.parameter.full_heart['value'] - self.player.parameter.heart['value']
        self.player.parameter.increase('heart', need_heal)

    def test_lvl(self):
        """Проверка опыта для поднятия уровня во время сна и поднятие уровня"""
        # если опыта больше чем в массиве с количеством опыта для следующего уровня, то уровень повышается
        # опыт не сбрасывается с повышением, позиция для нужного количества опыта соответствует текущему уровню игрока
        if self.player.parameter.test_lvl_up():
            self.player.parameter.lvl_up()
