import pygame


class Field:
    # Класс поля
    def __init__(self, screen, x, y):
        self.screen = screen
        self.size = (50, 50)
        self.x = x
        self.y = y
        self.color = (255, 255, 255)
        self.create_cell()
        self.get_text()

    def create_cell(self):
        # Создание классов Rect для всех клеток поля
        self.cell = pygame.Surface(self.size)
        self.cell.fill(self.color)

        self.list_cell = []
        for i in range(10):
            for j in range(10):
                rect = self.cell.get_rect(topleft=(self.x + j * 51, self.y + i * 51))
                self.list_cell.append(rect)

        self.double_list = [[(cell.x, cell.y) for cell in self.list_cell[i:i + 10]] for i in range(0, len(self.list_cell), 10)]

    def draw(self):
        # Отрисовка поля
        for cell in self.list_cell:
            self.screen.blit(self.cell, cell)
        for i in range(10):
            self.screen.blit(self.letters[i], (self.double_list[0][i][0] + 16, 17))
            if i == 9:
                self.screen.blit(self.nums[i], (self.double_list[i][0][0] - 39, self.double_list[i][0][1] + 14))
            else:
                self.screen.blit(self.nums[i], (self.double_list[i][0][0] - 33, self.double_list[i][0][1] + 14))

    def get_text(self):
        # Создание надписей (координат в классической игре)
        letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        nums = [str(x) for x in range(1, 11)]
        font = pygame.font.SysFont('couriernew', 25)
        self.letters = [font.render(letter, True, self.color) for letter in letters]
        self.nums = [font.render(num, True, self.color) for num in nums]
