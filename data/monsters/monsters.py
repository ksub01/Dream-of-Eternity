"""Место, где находятся все словари монстров"""
import data.world.creature as world


# сделать генерацию как с объектами


class Monster(world.Creature):
    pass


class GoblinWarrior(Monster):
    """Гоблин воин"""
    def __init__(self, session, factor=1):
        world.Creature.__init__(self, session=session, factor=factor, heart=50, force=2, dexterity=5,
                                wisdom=10,
                                lvl=1, exp=5, gold=10, target='Гоблин Воин',
                                skills=[], feature='Убив тысячу, вы получаете меч Горя',
                                sign='🐺', monster=True)


class GoblinShaman(world.Creature):
    """Гоблин шаман"""
    def __init__(self, session, factor=1):
        world.Creature.__init__(self, factor=factor, heart=70, force=4, dexterity=6, wisdom=12,
                                lvl=1, exp=5, gold=15, target='Гоблин Шаман',
                                skills=[], feature='Каждый ход восстанавливает 10 процентов здоровья союзнику'
                                                    ' с наименьшим здоровьем',
                                sign='🐰', monster=True, session=session)


class GoblinAssassin(world.Creature):
    """Гоблин убийца"""
    def __init__(self, session, factor=1):
        world.Creature.__init__(self, heart=90, force=6, defence=1,
                                dexterity=50, wisdom=10, factor=factor,
                                lvl=1, exp=10, gold=15, target='Гоблин Убийца',
                                skills=[], feature='При ударе игнорирует вашу броню ',
                                sign='🥷', monster=True, session=session, vision=40)


class Toad(world.Creature):
    """Жаба"""
    def __init__(self, session, factor=1):
        world.Creature.__init__(self, heart=150, force=8, defence=3,
                                dexterity=12, wisdom=14,
                                lvl=2, exp=25, target='Жаба',
                                skills=[], feature='С Жабы не выпадает золото ',
                                sign='🐸', monster=True, session=session, factor=factor)


class CultistOsiris(world.Creature):
    """Культист Озириса"""
    def __init__(self, session, factor=1):
        world.Creature.__init__(self, heart=170, force=12, defence=6,
                                dexterity=20, wisdom=18,
                                lvl=2, exp=60, gold=40, target='Культист Озириса',
                                skills=[], feature='Может своровать надетую вещь с игрока',
                                sign='🧕', monster=True, session=session, factor=factor)


class Snake(world.Creature):
    """Змея"""
    def __init__(self, session, factor=1):
        world.Creature.__init__(self, heart=220, force=20, defence=6,
                                dexterity=25, wisdom=20,
                                lvl=2, exp=70, gold=50, target='Змея Варганиса',
                                skills=[], feature='Отравляет ядом, который каждый удар снимает 20% здоровья'
                                                    ' от первоначального',
                                sign='🐍', monster=True, session=session, factor=factor)


forest = [GoblinWarrior, GoblinShaman, GoblinAssassin, Toad, CultistOsiris, Snake]
