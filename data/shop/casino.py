from colorama import Fore, Style
import random

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


class Casino:
    def __init__(self, player, session):
        self.session = session
        self.player = player

    def dialogue(self):
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
                self.start_game(self.gold_jackpot)
                break
            elif choice == '2':
                break

    def start_game(self, game):
        """Запускает игру заданную в рулетке, то есть даёт полный интерфейс, взаимодёствее перед игрой
        Передаётся: функция игры, в которую игрок хочет играть"""
        while True:
            what = input(HELP_MESSAGE + 'Играть => 1\n' + 'Нет => 2\n')
            if what == '1':
                game()
            elif what == '2':
                self.session.goodbye()
                break

    def gold_jackpot(self):
        """Проводит первую миниигру в казино - золотой куш. Игрок ставить золото есу выпадает случайный результат
        из списка [0, его золото*2]"""
        # вводится количество золота, которое игрок ставит
        while True:
            gold = input(Style.RESET_ALL + MESSAGE_DIALOGUE + 'Приветствуем вас в игре Золотой куш.\n'
                                                              'Введите количество золота, которое вы ставите\n'
                                                              'Выход ➔ 0\n')
            if gold.isdigit() and gold != '0':
                gold = int(gold)
                if self.player.parameter.gold_spending(gold):
                    print(HELP_MESSAGE + 'Игра начинается\n'
                                         'Итак выпало...')
                    self.session.pause()
                    win_gold = random.randint(0, gold * 2)
                    print(Fore.YELLOW + str(win_gold))
                    self.player.parameter.increase('gold', win_gold)
                    self.session.pause()
            elif gold == '0':
                self.session.goodbye()
                break
