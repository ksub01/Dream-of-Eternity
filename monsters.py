"""Место, где находятся все словари монстров"""
import world
from colorama import Fore, Style


class GoblinWarrior(world.Creature):
    """Гоблин воин"""
    def __init__(self):
        super().__init__()
        self.full_heart = 50
        self.full_force = 2
        self.full_dexterity = 5
        self.full_wisdom = 10
        self.lvl = 1
        self.exp = 5
        self.gold = 10
        self.target = 'Гоблин Воин'
        self.name = 'Гоблин Воин'
        self.skills = []
        self.property = 'Убив тысячу, вы получаете меч Горя'
        self.sign = '🐺'
        self.recovery_parameter()


class GoblinShaman(world.Creature):
    """Гоблин шаман"""
    def __init__(self):
        super().__init__()
        self.full_heart = 70
        self.full_force = 4
        self.full_dexterity = 6
        self.full_wisdom = 12
        self.lvl = 1
        self.exp = 5
        self.gold = 15
        self.target = 'Гоблин Шаман'
        self.name = 'Гоблин Шаман'
        self.skills = []
        self.property = 'Каждый ход восстанавливает 10 процентов здоровья союзнику с наименьшим здоровьем'
        self.sign = '🐺'
        self.recovery_parameter()


class GoblinAssassin(world.Creature):
    """Гоблин убийца"""
    def __init__(self):
        super().__init__()
        self.full_heart = 90
        self.full_force = 6
        self.full_defence = 1
        self.full_dexterity = 8
        self.full_wisdom = 10
        self.lvl = 1
        self.exp = 10
        self.gold = 15
        self.target = 'Гоблин Убийца'
        self.name = 'Гоблин Убийца'
        self.skills = []
        self.property = 'При ударе игнорирует вашу броню '
        self.sign = '🥷'
        self.recovery_parameter()


class Toad(world.Creature):
    """Жаба"""
    def __init__(self):
        super().__init__()
        self.full_heart = 150
        self.full_force = 8
        self.full_defence = 3
        self.full_dexterity = 12
        self.full_wisdom = 14
        self.lvl = 2
        self.exp = 25
        self.target = 'Жаба'
        self.name = 'Жаба'
        self.skills = []
        self.property = 'С Жабы не выпадает золота'
        self.sign = '🐸'
        self.recovery_parameter()


class CultistOsiris(world.Creature):
    """Культист Озириса"""
    def __init__(self):
        super().__init__()
        self.full_heart = 170
        self.full_force = 12
        self.full_defence = 6
        self.full_dexterity = 20
        self.full_wisdom = 18
        self.lvl = 2
        self.gold = 40
        self.exp = 60
        self.target = 'Культист Озириса'
        self.name = 'Культист Озириса'
        self.skills = []
        self.property = 'Может своровать надетую вещь с игрока'
        self.sign = '🧕'
        self.recovery_parameter()


class Snake(world.Creature):
    """Змея"""
    def __init__(self):
        super().__init__()
        self.full_heart = 220
        self.full_force = 20
        self.full_defence = 6
        self.full_dexterity = 25
        self.full_wisdom = 20
        self.lvl = 2
        self.gold = 50
        self.exp = 70
        self.target = 'Змея Варганиса'
        self.name = 'Змея Варганиса'
        self.skills = []
        self.property = 'Отравляет ядом, который каждый удар снимает 20% здоровья от первоначального'
        self.sign = '🐍'
        self.recovery_parameter()

