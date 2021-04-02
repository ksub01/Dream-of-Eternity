import monsters1
import hero
import function
import blacksmith
import hotel
import random
import items
import math
import time


function.prestart()
print("\nХотите пройти обучение? Да => 1 Нет => 2 Загрузить игру => 3")
re = input()
if re == '1':
    function.guide()
if re == '3':
    function.load()
while hero.heroic.heart > 0:
    function.parameters()
    function.start()
    if hero.heroic.exp >= math.ceil(hero.heroic.lvl * 50):
        print("Поспите, чтобы повысить ваш уровень\n")
    b = input()
    if b == '1':
        blacksmith.blacksmith()
    if b == '2':
        hotel.hotel()
    if b == '3':
        function.forest()
    if b == '4':
        function.roulette()
    if b == '5':
        function.stats()
    if b == '6':
        function.save()
    if hero.heroic.heart <= 0:
        if random.randint(1, 100) <= hero.heroic.god:
            hero.heroic.heart = hero.heroic.heart_full
            print("Вы, как феникс, восстали из пепла")
            time.sleep(2)
input()
