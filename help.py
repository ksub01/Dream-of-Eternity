class GoblinWar:
    def __init__(self):
        self.x = random.randint(0, 17)
        self.y = random.randint(0, 29)
        self.sign = '🐺'
        pass


class GoblinShaman:
    def __init__(self):
        self.x = random.randint(0, 17)
        self.y = random.randint(0, 29)
        self.sign = '🐯'
        pass


def gen_forest():
    """Основная локация для путешествий"""
    global location
    location = [list('🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳'),
                list('🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳'),
                list('🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳'),
                list('🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳'),
                list('🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳'),
                list('🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳'),
                list('🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳'),
                list('🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳'),
                list('🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳'),
                list('🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳'),
                list('🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳'),
                list('🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳'),
                list('🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳'),
                list('🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳'),
                list('🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳'),
                list('🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳'),
                list('🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳'),
                list('🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳🌳')]
    mob = []
    box1 = random.randint(0, 17)
    box2 = random.randint(0, 29)
    for _ in range(100):
        box1 = random.randint(0, 17)
        box2 = random.randint(0, 29)
        location[box1][box2] = Fore.GREEN + '🪨'
    for _ in range(700):
        box1 = random.randint(0, 17)
        box2 = random.randint(0, 29)
        location[box1][box2] = Fore.GREEN + '。'
    for i in range(random.randint(7, 12)):
        mob.append(GoblinWar())
    for i in range(3, 4):
        mob.append(GoblinShaman())
    for i in mob:
        location[i.x][i.y] = i.sign
    for _ in range(3):
        box1 = random.randint(0, 17)
        box2 = random.randint(0, 29)
        while tree(box1, box2):
            box1 = random.randint(0, 17)
            box2 = random.randint(0, 29)
        location[box1][box2] = '💍'
    for _ in range(6, 12):
        box1 = random.randint(0, 17)
        box2 = random.randint(0, 29)
        while tree(box1, box2):
            box1 = random.randint(0, 17)
            box2 = random.randint(0, 29)
        location[box1][box2] = '🪙'
    for _ in range(1):
        box1 = random.randint(0, 17)
        box2 = random.randint(0, 29)
        while tree(box1, box2):
            box1 = random.randint(0, 17)
            box2 = random.randint(0, 29)
        location[box1][box2] = '🪦'

    for _ in range(1):
        box1 = random.randint(0, 17)
        box2 = random.randint(0, 29)
        while tree(box1, box2):
            box1 = random.randint(0, 17)
            box2 = random.randint(0, 29)
        location[box1][box2] = '💎'
    for _ in range(1):
        box1 = random.randint(0, 17)
        box2 = random.randint(0, 29)
        while tree(box1, box2):
            box1 = random.randint(0, 17)
            box2 = random.randint(0, 29)
        location[box1][box2] = '🐗'
    for _ in range(8):
        box1 = random.randint(0, 17)
        box2 = random.randint(0, 29)
        while tree(box1, box2):
            box1 = random.randint(0, 17)
            box2 = random.randint(0, 29)
        location[box1][box2] = '🎁'
    for _ in range(1):
        box1 = random.randint(0, 17)
        box2 = random.randint(0, 29)
        while tree(box1, box2):
            box1 = random.randint(0, 17)
            box2 = random.randint(0, 29)
        location[box1][box2] = '🐉'
    for line in location:
        print(*line)


"""def place(x, y, ob):
    while tree(x, y):
        box1 = random.randint(0, 17)
        box2 = random.randint(0, 29)
        location[box1][box2] = '💍'"""


def tree(x, y):
    """проверяет, что вокруг нет деревьев"""
    for delta_x, delta_y in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
        x2, y2 = x+delta_x, y+delta_y
        if 0 <= x2 <= 17 and 0 <= y2 <= 29 and location[x2][y2] == '🌳':
            return -1
    return 0
