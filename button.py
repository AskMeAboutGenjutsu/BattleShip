import pygame


class Button:
    # Класс кнопки
    def __init__(self, x, y, screen, text):
        self.x = x
        self.y = y
        self.screen = screen
        self.color = (200, 200, 200)
        self.size = (220, 50)
        self.clicked = False
        self.create_rect()
        self.get_text(text)

    def create_rect(self):
        # Создание класса Rect
        self.cell = pygame.Surface(self.size)
        self.cell.fill(self.color)
        self.rect = self.cell.get_rect(center=(self.x, self.y))

    def draw(self):
        # Отрисовка кнопки и проверка на нажатие
        action = False
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] and not self.clicked:
                self.clicked = True
                action = True
        if not pygame.mouse.get_pressed()[0]:
            self.clicked = False

        self.screen.blit(self.cell, self.rect)
        self.screen.blit(self.text, self.text_rect)
        return action

    def get_text(self, text):
        # Создание надписи внутри кнопки
        font = pygame.font.Font('Fonts/FeaturedLight.otf', 30)
        self.text = font.render(text, True, (0, 0, 0))
        self.text_rect = self.text.get_rect(center=(self.x, self.y))




