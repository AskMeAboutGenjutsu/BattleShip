import random

from ships import Ship


def allowed_coord(ships, position, size, rot):
    # Определение разрешенных координат для постановке корабля в соответсвиями с правилами игры
    x_list, y_list, allow = [], [], []
    if rot:
        if size == 4:
            x_list = [50, 101, 152, 203, 254, 305, 356]
            y_list = [50, 101, 152, 203, 254, 305, 356, 407, 458, 509]
        elif size == 3:
            x_list = [50, 101, 152, 203, 254, 305, 356, 407]
            y_list = [50, 101, 152, 203, 254, 305, 356, 407, 458, 509]
        elif size == 2:
            x_list = [50, 101, 152, 203, 254, 305, 356, 407, 458]
            y_list = [50, 101, 152, 203, 254, 305, 356, 407, 458, 509]
        elif size == 1:
            x_list = [50, 101, 152, 203, 254, 305, 356, 407, 458, 509]
            y_list = [50, 101, 152, 203, 254, 305, 356, 407, 458, 509]
    else:
        if size == 4:
            x_list = [50, 101, 152, 203, 254, 305, 356, 407, 458, 509]
            y_list = [50, 101, 152, 203, 254, 305, 356]
        elif size == 3:
            x_list = [50, 101, 152, 203, 254, 305, 356, 407, 458, 509]
            y_list = [50, 101, 152, 203, 254, 305, 356, 407]
        elif size == 2:
            x_list = [50, 101, 152, 203, 254, 305, 356, 407, 458, 509]
            y_list = [50, 101, 152, 203, 254, 305, 356, 407, 458]

    for i in x_list:
        if position == 2:
            i += 590
        for j in y_list:
            allow.append((i, j))

    if len(ships) > 0:
        prohibition = []
        for ship in ships:
            prohibition += ship.forbidden_coordinates(rot, size)

        for pr in prohibition:
            if pr in allow:
                allow.remove(pr)

    x, y = random.choice(allow)

    return x, y


def arrangement_of_ships(screen, position):
    # Создание базовых настроек кораблей (поворот и размер)
    rotation = [random.choice((0, 1)) for i in range(6)] + [1] * 4
    size_of_ships = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
    spec = list(zip(size_of_ships, rotation))
    ships = []
    for item in spec:
        x, y = allowed_coord(ships, position, *item)
        ships.append(Ship(x, y, screen, *item))

    return ships
