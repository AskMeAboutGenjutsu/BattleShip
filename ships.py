import pygame


class Ship:
    # Класс корабля
    def __init__(self, x, y, screen, size, rotation):
        self.x = x
        self.y = y
        if rotation:
            self.size = (51 * size-1, 50)
        else:
            self.size = (50, 51 * size-1)
        self.rotation = rotation
        self.size_int = size
        self.screen = screen
        self.choice_color()
        self.create_cell()
        self.create_hp()

    def create_cell(self):
        # Создание класса Rect
        self.cell = pygame.Surface(self.size)
        self.cell.fill(self.color)
        self.rect = self.cell.get_rect(topleft=(self.x, self.y))

    def choice_color(self):
        # Выбор цвета корабля в зависимости от его размера
        if self.size_int == 4:
            self.color = (255, 255, 0)
        elif self.size_int == 3:
            self.color = (255, 0, 255)
        elif self.size_int == 2:
            self.color = (0, 255, 255)
        elif self.size_int == 1:
            self.color = (255, 0, 0)

    def draw(self):
        # Отрисовка корабля
        self.screen.blit(self.cell, self.rect)

    def create_hp(self):
        # Выбор очков здоровья корабля в зависимости от его размера
        for i in range(1, 5):
            if self.size_int == i:
                self.HP = self.size_int
                break

    def forbidden_coordinates(self, next_rotation, next_size):
        # Определение запрещенных координат вокруг корабля
        # в зависимости от поворота и размера самого корабля и следующего корабля
        x_list, y_list = [], []
        if self.size_int == 4:
            if next_size == 3:
                if self.rotation and next_rotation:
                    x_list = [self.x, self.x + 51, self.x + 102, self.x + 153, self.x + 204,
                              self.x - 51, self.x - 102, self.x - 153]
                    y_list = [self.y, self.y + 51, self.y - 51]
                elif self.rotation and not next_rotation:
                    x_list = [self.x, self.x + 51, self.x + 102, self.x + 153, self.x + 204,
                              self.x - 51]
                    y_list = [self.y, self.y + 51, self.y - 51, self.y - 102, self.y - 153]
                elif not self.rotation and next_rotation:
                    x_list = [self.x, self.x + 51, self.x - 51, self.x - 102, self.x - 153]
                    y_list = [self.y, self.y + 51, self.y + 102, self.y + 153, self.y + 204, self.y - 51]
                else:
                    x_list = [self.x, self.x + 51, self.x - 51]
                    y_list = [self.y, self.y + 51, self.y + 102, self.y + 153, self.y + 204,
                              self.y - 51, self.y - 102, self.y - 153]
            elif next_size == 2:
                if self.rotation and next_rotation:
                    x_list = [self.x, self.x + 51, self.x + 102, self.x + 153, self.x + 204,
                              self.x - 51, self.x - 102]
                    y_list = [self.y, self.y + 51, self.y - 51]
                elif self.rotation and not next_rotation:
                    x_list = [self.x, self.x + 51, self.x + 102, self.x + 153, self.x + 204,
                              self.x - 51]
                    y_list = [self.y, self.y + 51, self.y - 51, self.y - 102]
                elif not self.rotation and next_rotation:
                    x_list = [self.x, self.x + 51, self.x - 51, self.x - 102]
                    y_list = [self.y, self.y + 51, self.y + 102, self.y + 153, self.y + 204, self.y - 51]
                else:
                    x_list = [self.x, self.x + 51, self.x - 51]
                    y_list = [self.y, self.y + 51, self.y + 102, self.y + 153, self.y + 204,
                              self.y - 51, self.y - 102]
            elif next_size == 1:
                if self.rotation and next_rotation:
                    x_list = [self.x, self.x + 51, self.x + 102, self.x + 153, self.x + 204,
                              self.x - 51]
                    y_list = [self.y, self.y + 51, self.y - 51]
                else:
                    x_list = [self.x, self.x + 51, self.x - 51]
                    y_list = [self.y, self.y + 51, self.y + 102, self.y + 153, self.y + 204, self.y - 51]
        elif self.size_int == 3:
            if next_size == 3:
                if self.rotation and next_rotation:
                    x_list = [self.x, self.x + 51, self.x + 102, self.x + 153,
                              self.x - 51, self.x - 102, self.x - 153]
                    y_list = [self.y, self.y + 51, self.y - 51]
                elif self.rotation and not next_rotation:
                    x_list = [self.x, self.x + 51, self.x + 102, self.x + 153,
                              self.x - 51]
                    y_list = [self.y, self.y + 51, self.y - 51, self.y - 102, self.y - 153]
                elif not self.rotation and next_rotation:
                    x_list = [self.x, self.x + 51, self.x - 51, self.x - 102, self.x - 153]
                    y_list = [self.y, self.y + 51, self.y + 102, self.y + 153, self.y - 51]
                else:
                    x_list = [self.x, self.x + 51, self.x - 51]
                    y_list = [self.y, self.y + 51, self.y + 102, self.y + 153,
                              self.y - 51, self.y - 102, self.y - 153]
            elif next_size == 2:
                if self.rotation and next_rotation:
                    x_list = [self.x, self.x + 51, self.x + 102, self.x + 153,
                              self.x - 51, self.x - 102]
                    y_list = [self.y, self.y + 51, self.y - 51]
                elif self.rotation and not next_rotation:
                    x_list = [self.x, self.x + 51, self.x + 102, self.x + 153,
                              self.x - 51]
                    y_list = [self.y, self.y + 51, self.y - 51, self.y - 102]
                elif not self.rotation and next_rotation:
                    x_list = [self.x, self.x + 51, self.x - 51, self.x - 102]
                    y_list = [self.y, self.y + 51, self.y + 102, self.y + 153, self.y - 51]
                else:
                    x_list = [self.x, self.x + 51, self.x - 51]
                    y_list = [self.y, self.y + 51, self.y + 102, self.y + 153,
                              self.y - 51, self.y - 102]
            elif next_size == 1:
                if self.rotation and next_rotation:
                    x_list = [self.x, self.x + 51, self.x + 102, self.x + 153,
                              self.x - 51]
                    y_list = [self.y, self.y + 51, self.y - 51]
                elif not self.rotation and next_rotation:
                    x_list = [self.x, self.x + 51, self.x - 51]
                    y_list = [self.y, self.y + 51, self.y + 102, self.y + 153, self.y - 51]
        elif self.size_int == 2:
            if next_size == 2:
                if self.rotation and next_rotation:
                    x_list = [self.x, self.x + 51, self.x + 102,
                              self.x - 51, self.x - 102]
                    y_list = [self.y, self.y + 51, self.y - 51]
                elif self.rotation and not next_rotation:
                    x_list = [self.x, self.x + 51, self.x + 102,
                              self.x - 51]
                    y_list = [self.y, self.y + 51, self.y - 51, self.y - 102]
                elif not self.rotation and next_rotation:
                    x_list = [self.x, self.x + 51, self.x - 51, self.x - 102]
                    y_list = [self.y, self.y + 51, self.y + 102, self.y - 51]
                else:
                    x_list = [self.x, self.x + 51, self.x - 51]
                    y_list = [self.y, self.y + 51, self.y + 102,
                              self.y - 51, self.y - 102]
            elif next_size == 1:
                if self.rotation and next_rotation:
                    x_list = [self.x, self.x + 51, self.x + 102,
                              self.x - 51]
                    y_list = [self.y, self.y + 51, self.y - 51]
                elif not self.rotation and next_rotation:
                    x_list = [self.x, self.x + 51, self.x - 51]
                    y_list = [self.y, self.y + 51, self.y + 102, self.y - 51]
        elif self.size_int == 1:
            x_list = [self.x, self.x + 51, self.x - 51]
            y_list = [self.y, self.y + 51, self.y - 51]

        prohibition = []
        for x in x_list:
            for y in y_list:
                if 50 <= y < 560 and (50 <= x < 560 or 640 <= x < 1150):
                    prohibition.append((x, y))

        return prohibition
