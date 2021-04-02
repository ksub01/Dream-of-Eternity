import hero
import items
import function


def hotel():
    print("Вы находитесь в гостинице\n"
          "Здраствуйте. Воспользоваться нашими услугами вы можете за {} монет\n"
          "Согласны?\n"
          "Да => 1\n"
          "Нет => 2\n".format(items.hotel1.gold))
    k = input()
    if k == '1':
        if hero.heroic.gold >= items.hotel1.gold:
            hero.heroic.gold -= items.hotel1.gold
            function.lvlup()
            hero.heroic.heart = hero.heroic.heart_full
        else:
            print("У вас не хватает денег")
    else:
        print("До свидания\n")
