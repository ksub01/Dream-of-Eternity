"""Основной модуль запуска программы, подготовка к запуску, настройка и игровой цикл"""
import start
import information
import town
import blacksmith
import fight
import hotel
import sages
import casino
import inventory
import hero


"""
import telebot
bot = telebot.TeleBot('1696360118:AAG6Z-R627A2GefoHgk8mmmjmbee5xS8f4o')

def out_message(text):
    @bot.message_handler(content_types=['text'])
    def get_text_messages(message):
        bot.send_message(message.from_user.id, text)
        
"""

"""
# параметры RGB цветов
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (125, 125, 125)
LIGHT_BLUE = (64, 128, 255)
GREEN = (0, 200, 64)
YELLOW = (225, 225, 0)
PINK = (230, 50, 230)


# значение FPS в игре
FPS = 120

# инициализация всего pygame
pygame.init()


# шрифт и его размер
shrift = pygame.font.SysFont('arial', 36)

# создание объекта поверхности экрана и установление его параметра
screen = pygame.display.set_mode((1920, 1080), pygame.RESIZABLE)

# создание таймера для отмера FPS
clock = pygame.time.Clock()

# название окна игры
pygame.display.set_caption('Dream Of Eternity')

# если надо до цикла отобразить объекты на экране
pygame.display.update()




def display_parameter_hero_in_screen(cou):
    #""Отображает все параметры героя в окне
    # параметры первого прямоугольника
    r1 = (10, 10, 250, 460)
    r2 = (260, 10, 1645, 980)
    # рисует прямоугольник
    pygame.draw.rect(screen, YELLOW, r1, 8)
    pygame.draw.rect(screen, YELLOW, r2, 8)
    # создание поверхности с текстом
    strok1 = "Ваши характеристики"
    # "Ваше здоровье {}/{}".format(hero_stats_and_action_with_parameter.parameter['heart'], hero_stats_and_action_with_parameter.parameter['full_heart'])
    text1 = shrift.render(strok1, 1, (255, 255, 255))
    text2 = shrift.render('Здоровье: ' + str(hero_stats_and_action_with_parameter.parameter['heart_full'] + cou), 1, (255, 255, 255))
    text3 = shrift.render('Hello Привет', 1, (255, 255, 255))
    text4 = shrift.render('Hello Привет', 1, (255, 255, 255))
    text5 = shrift.render('Hello Привет', 1, (255, 255, 255))
    text6 = shrift.render('Hello Привет', 1, (255, 255, 255))
    text7 = shrift.render('Hello Привет', 1, (255, 255, 255))
    text8 = shrift.render('Hello Привет', 1, (255, 255, 255))
    text9 = shrift.render('Hello Привет', 1, (255, 255, 255))
    text10 = shrift.render('Hello Привет', 1, (255, 255, 255))
    text11 = shrift.render('Hello Привет', 1, (255, 255, 255))
    # добавление поверхности на экран
    screen.blit(text1, (20, 20))
    screen.blit(text2, (20, 60))
    screen.blit(text3, (20, 100))
    screen.blit(text4, (20, 140))
    screen.blit(text5, (20, 180))
    screen.blit(text6, (20, 220))
    screen.blit(text7, (20, 260))
    screen.blit(text8, (20, 300))
    screen.blit(text9, (20, 340))
    screen.blit(text10, (20, 380))
    screen.blit(text11, (20, 420))
"""


def start():
    """Функции, включающиеся перед самым запуском игры"""
    start.information()
    start.prologue()
    start.guide()


def setting():
    """Загрузка и выбор класса перед началом игры"""
    ans = input("Хотите ли вы загрузить игру или хотите начать новую? Начать новую => 1 Загрузить => 2\n")
    if ans == '1':
        pass
    else:
        pass
    start.choice_class()


def playing_loop():
    """Основной цикл игры, с вычвелчивание города и боями"""

    while hero.parameter['heart'] > 0:
        """Основной цикл игры, город, место, где вы выбираете место куда пойти"""
        information.display_parameters()
        town.places()
        town.display_lvl_up()
        choice = input()
        if choice == '1':
            blacksmith.dialogue()
        elif choice == '2':
            hotel.dialogue()
        elif choice == '3':
            fight.dungeon()
        elif choice == '4':
            casino.dialogue()
        elif choice == '5':
            inventory.start_inventory()
        elif choice == '6':
            sages.dialogue()
        else:
            pass
    else:
        if hero.parameter['heart'] <= 0:
            print("Вы проиграли. Озирис уничтожил мир, а Аркона пала.")




"""
cou = 1
while 1:
    # задержка
    clock.tick(FPS)
    # цикл обработки событий
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            # удаляет pygame
            pygame.quit()
            # закрывает окно
            sys.exit()
    display_parameter_hero_in_screen(cou)
    # обновление экрана
    pygame.display.update()
    cou += 1


"""


start()
setting()
playing_loop()
