"""Место, где находятся все словари монстров"""
from colorama import Fore, Back, Style

MESSAGE_DAMAGE = Fore.RED + Style.DIM
MESSAGE_HEAL = Fore.GREEN + Style.BRIGHT

# основной словарь со всеми монстрами и их характеристиками
monsters = {1: {'name': 'Гоблин Воин', 'full_heart': 50, 'heart': 50, 'full_attack': 2, 'attack': 2, 'defence': 0,
                'dexterity': 5, 'wisdom': 10, 'lvl': 1, 'exp': 5, 'gold': 10,
                'property': 'Убив тысячу, вы получаете меч Горя'},
            2: {'name': 'Гоблин Шаман', 'full_heart': 70, 'heart': 70, 'full_attack': 4, 'attack': 4, 'defence': 0,
                'dexterity': 6, 'wisdom': 12, 'lvl': 1, 'exp': 5, 'gold': 15,
                'property': 'Каждый ход восстанавливает 10 процентов здоровья персонажу с наименьшим здоровьем'},
            3: {'name': 'Гоблин Убийца', 'full_heart': 90, 'heart': 90, 'full_attack': 6, 'attack': 6,
                'defence': 1, 'dexterity': 8, 'wisdom': 10, 'lvl': 1, 'exp': 10, 'gold': 15,
                'property': 'Игнорирует вашу броню'},
            4: {'name': 'Жаба', 'full_heart': 150, 'heart': 150, 'full_attack': 8, 'attack': 8, 'defence': 3,
                'dexterity': 12, 'gold': 0, 'exp': 25, 'wisdom': 14,
                'lvl': 2, 'property': 'С неё не выпадает золота'},
            5: {'name': 'Култист Озириса', 'full_heart': 170, 'heart': 170, 'full_attack': 12,
                'attack': 12, 'defence': 6, 'dexterity': 20, 'gold': 40, 'exp': 60,  'wisdom': 18,
                'lvl': 2, 'property': 'Может своровать надетую вещь с игрока'},
            6: {'name': 'Змея Варганиса', 'full_heart': 220, 'heart': 220, 'full_attack': 20, 'attack': 20,
                'defence': 6, 'dexterity': 25, 'gold': 50, 'exp': 70,  'wisdom': 20,
                'lvl': 2, 'property': 'Отравляет ядом, который каждый удар снимает 20% здоровья от первоначального'},
            }


def monster_heart_new(names, heart):
    """Функция в которой здоровье монстра ЗАДАЁТСЯ после прошлого боя, то есть становится равными второму
     аргументу функции. Запускается перед каждым боем
     Принимает: словарь монстра для цели уставновления и количество нового здоровья"""
    names['heart'] = heart


def monster_recovery_heart(name, heart):
    """Монстр восстанавливает данное количество здоровья
    Принимает: словарь монстра для цели восстановления и количество здоровья,
    которое нужно восстановить"""
    name['heart'] += heart
    print(MESSAGE_HEAL + 'Монстр восстановил {} здоровья'.format(heart))


def monster_spend_heart(name, heart):
    """Монстр теряет данное количество здоровья
    Принимает: словарь монстра для цели восстановления и количество здоровья,
    которое монстр потерял"""
    name['heart'] -= heart
    print(MESSAGE_DAMAGE + 'Монстр потерял {} здоровья'.format(heart))


def monster_recovery_attack(names, attack):
    """Функция в которой атака монстра становится равна второму аргументу функции, под действием некоторых обстоятельств
    Принимает: словарь монстра для цели восстановления и количество атаки,
    которое нужно восстановить"""
    names['attack'] = attack
