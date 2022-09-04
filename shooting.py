import pygame


class Shot:
    # Класс выстрела, в зависимости от попадания по кораблю отрисовывается промах или урон
    def __init__(self, screen, hit, x, y):
        self.screen = screen
        if hit:
            self.image = pygame.image.load('Images/damage_img.png')
        else:
            self.image = pygame.image.load('Images/miss_img.png')
        self.rect = self.image.get_rect(topleft=(x, y))

    def draw(self):
        self.screen.blit(self.image, self.rect)