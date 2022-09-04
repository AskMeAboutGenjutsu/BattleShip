import copy
import random
import pygame
from shooting import Shot


class Player:
    # Класс живого игрока
    def __init__(self, field, ships, screen):
        self.ships = ships
        self.screen = screen
        self.field = copy.deepcopy(field.list_cell)
        self.load_sounds()

    def load_sounds(self):
        self.sound_miss = pygame.mixer.Sound('Sounds/miss.wav')
        self.sound_hit = pygame.mixer.Sound('Sounds/hit.wav')
        self.sound_kill = pygame.mixer.Sound('Sounds/kill.wav')

    def fire(self, x, y):
        # Ведение огня живым игроком
        for i, cell in enumerate(self.field):
            if cell and cell.collidepoint(x, y):
                self.field[i] = None
                if self.check_hit(cell.x, cell.y):
                    return True
                else:
                    return False

    def check_hit(self, x, y):
        # Проверка на попадание по кораблю
        for ship in self.ships:
            if ship.rect.collidepoint((x, y)):
                ship.HP -= 1
                self.shot = Shot(self.screen, True, x, y)
                if ship.HP == 0:
                    self.sound_kill.play()
                else:
                    self.sound_hit.play()
                return True
        self.shot = Shot(self.screen, False, x, y)
        self.sound_miss.play()
        return False


class PlayerAI:
    # Класс ИИ
    def __init__(self, field, ships, screen):
        self.ships = ships
        self.screen = screen
        self.field = copy.deepcopy(field.double_list)
        self.list_hit = []
        self.kill = False

    def fire(self):
        # Логика ведения огня ИИ
        while self.list_hit and not self.kill:  #Если ИИ попал, он проверяет соседний клетки
            i, j = self.list_hit[0]

            if self.ship_vertical:
                if i + 1 < len(self.field) and self.field[i + 1][j]:
                    cell = self.field[i + 1][j]
                    self.field[i + 1][j] = None
                    if self.check_hit(cell[0], cell[1]):
                        self.list_hit.append((i + 1, j))
                        self.k += 1
                        return True
                    return False

                if i - 1 >= 0 and self.field[i - 1][j]:
                    cell = self.field[i - 1][j]
                    self.field[i - 1][j] = None
                    if self.check_hit(cell[0], cell[1]):
                        self.list_hit.append((i - 1, j))
                        self.k += 1
                        return True
                    return False
            if self.k < 1:
                self.ship_vertical = False

                if j + 1 < len(self.field[0]) and self.field[i][j + 1]:
                    cell = self.field[i][j + 1]
                    self.field[i][j + 1] = None
                    if self.check_hit(cell[0], cell[1]):
                        self.list_hit.append((i, j + 1))
                        return True
                    return False

                if j - 1 >= 0 and self.field[i][j - 1]:
                    cell = self.field[i][j - 1]
                    self.field[i][j - 1] = None
                    if self.check_hit(cell[0], cell[1]):
                        self.list_hit.append((i, j - 1))
                        return True
                    return False

            self.list_hit.pop(0)
        else:
            # ИИ случайным образом выстреливает по полю
            self.kill = False
            self.ship_vertical = True
            self.k = 0

            self.list_hit = []
            while True:
                i, j = random.randint(0, 9), random.randint(0, 9)
                if self.field[i][j]:
                    cell = self.field[i][j]
                    break
            self.field[i][j] = None
            if self.check_hit(cell[0], cell[1]):
                self.list_hit = [(i, j)]
                return True
            return False

    def check_hit(self, x, y):
        # проверка ИИ на попадание по кораблю
        for ship in self.ships:
            if ship.rect.collidepoint((x, y)):
                ship.HP -= 1
                self.shot = Shot(self.screen, True, x, y)
                if ship.HP == 0:
                    self.ship_sunk(ship)
                return True
        self.shot = Shot(self.screen, False, x, y)
        return False

    def ship_sunk(self, ship):
        # Зануление клеток в радиусе 1 клетки вокруг потопленного корабля
        self.kill = True
        for cell in ship.forbidden_coordinates(1, 1):
            for i, cells in enumerate(self.field):
                if cell in cells:
                    self.field[i][cells.index(cell)] = None


