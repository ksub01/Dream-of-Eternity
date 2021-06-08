import data.items.items as items
import data.world.creature as world
import data.game as game
from colorama import Fore, Style


class Blacksmith:
    def __init__(self, player, visit):
        self.player = player
        self.game = visit

    def get_item(self, item):
        """Проверяет, хватает ли у игрока денег, если да, то добавляет данный предмет в инвентарь.
        Принимает: предмет и модификатор цены"""
        if self.player.parameter.gold['value'] >= int(item.cost['value']):
            self.player.parameter.gold_spending(int(item.cost['value']))
            self.player.inventory.get_thing(item)
            print('Спасибо за покупку\n')
            self.game.pause()
        else:
            self.game.not_enough_money()

    def sell(self):
        self.player.inventory.show_things()
        print('Выберите вещь, которую вы хотите продать')
        try:
            thing = self.player.inventory.choose_thing()[0]
            print('Вы точно хотите продать {} за {}🪙?'.format(thing.name['value'], thing.cost['value'] // 2))
            ch = input('Да -> 1\nНет -> 2\n')
            if ch == '1':
                self.player.parameter.increase('gold', thing.cost['value'] // 2)
                self.game.pause()
                self.player.inventory.remove_thing(thing)
            else:
                self.game.goodbye()
        except IndexError:
            print('Данной вещи нет в инвентаре')
            self.game.pause()

    def display(self):
        """Основной интерфейс кузнеца"""
        while 1:
            number_type = self.showcase()
            if number_type != '7' and number_type != '6':
                store = items.Goods()
                key = {'1': 'sword', '2': 'armor', '3': 'cloak', '4': 'ring'}
                cls = {'1': world.Sword, '2': world.Armor, '3': world.Cloak, '4': world.Ring}
                # выбираем нужный список вещей в магазине из данной категории и из другого модуля
                list_items = getattr(store, key[number_type])
                # передаем список предметов и класс предмета
                self.display_items(list_items, cls[number_type])
                print('Купить -> 1\nУйти -> 2\n')
                c = input()
                if c == '1':
                    print('Какой из?')
                    choice_thing = input()
                    if choice_thing.isdigit():
                        # передаем вещь и класс
                        self.buy_thing(list_items[int(choice_thing)], cls[number_type])
                else:
                    print('Простите')
                    self.game.pause()
            elif number_type == '6':
                self.sell()
            else:
                break

    @staticmethod
    def showcase():
        """Отображает отделы магазина, запрашивает и возвращает выбранный отдел"""
        choice = input(
            Style.RESET_ALL +
            "Здраствуй, хочешь чего нибудь купить?\n" + Fore.GREEN +
            "Оружие => 1\n"
            "Броня => 2\n"
            "Плащи => 3\n"
            "Кольца => 4\n"
            "Зелья => 5\n"
            "Продать вещи => 6\n"
            "Вернуться => 7\n")
        return choice

    def display_items(self, list_items: list[dict], cls: type):
        for pos in range(1, len(list_items)):
            thing = cls(list_items[pos])
            if self.player.parameter.lvl['value'] >= thing.lvl['value']:
                print(Fore.GREEN + '-'*80)
                thing.display(pos)
                print(Fore.GREEN + '-'*80)
                print()

    def buy_thing(self, item: dict, cls: type):
        print(Fore.BLUE + 'Ваше золото: {}🪙 Вещь стоит {}🪙'.format(self.player.parameter.gold['value'], item['cost']))
        print(Fore.GREEN + 'Вы точно хотите купить {}?'.format(item['name']))
        choice = input('Да -> 1 Нет -> 2\n' + Style.RESET_ALL)
        if choice == '1':
            self.get_item(cls(item))


if __name__ == '__main__':
    pass