import sys
import pygame
from button import Button
from field import Field
from arrangementShips import arrangement_of_ships

from player import PlayerAI, Player


class StartGame:
    # Основной класс игры
    def __init__(self):
        pygame.init()
        self.height, self.width = 1200, 650
        self.screen = pygame.display.set_mode((self.height, self.width))
        pygame.display.set_caption('BattleShip')
        pygame.display.set_icon(pygame.image.load('Images/icon.ico'))
        self.bg_color = (96, 96, 96)
        self.fps = 60
        self.clock = pygame.time.Clock()
        self.menu_run = True
        self.load_music()
        self.create_menu_objects()
        self.create_pause_objects()
        self.create_gameover_objects()

    def load_music(self):
        pygame.mixer.music.load('Sounds/main_music.mp3')
        pygame.mixer.music.set_volume(0.1)
        pygame.mixer.music.play(-1)
        self.music_win = pygame.mixer.Sound('Sounds/win.wav')
        self.music_lose = pygame.mixer.Sound('Sounds/lose.wav')

    def create_objects(self):
        self.field_left = Field(self.screen, 50, 50)
        self.field_right = Field(self.screen, 640, 50)
        self.ships_left = arrangement_of_ships(self.screen, 1)
        self.ships_right = arrangement_of_ships(self.screen, 2)
        self.player_right = PlayerAI(self.field_left, self.ships_left, self.screen)
        self.player_left = Player(self.field_right, self.ships_right, self.screen)
        self.shooting = []
        self.next_move = True

    def draw_objects(self):
        self.field_left.draw()
        self.field_right.draw()

        for ship in self.ships_left:
            ship.draw()

        if self.shooting:
            for shot in self.shooting:
                shot.draw()

    def create_menu_objects(self):
        self.button_run = Button(self.height // 2, self.width // 2 + 75, self.screen, 'Play')
        self.button_exit_menu = Button(self.height // 2, self.width // 2 + 225, self.screen, 'Exit')
        self.font = pygame.font.Font('Fonts/FeaturedLight.otf', 150)
        self.name = self.font.render('BATTLESHIP', True, (40, 40, 40))
        self.name_shadow = self.font.render('BATTLESHIP', True, (0, 0, 0))
        self.name_rect = self.name.get_rect(center=(self.height // 2 + 4, 200 + 4))
        self.name_shadow_rect = self.name_shadow.get_rect(center=(self.height // 2 - 4, 200 - 4))
        self.menu_img = pygame.image.load('Images/menu_img.jpg').convert()

    def create_pause_objects(self):
        self.button_continue = Button(self.height // 2, self.width // 2 - 50, self.screen, 'Continue')
        self.button_exit_pause = Button(self.height // 2, self.width // 2 + 50, self.screen, 'Exit')
        self.pause_img = pygame.image.load('Images/pause_img.jpg')

    def create_gameover_objects(self):
        self.button_ok = Button(self.height // 2, self.width // 2 + 170, self.screen, 'Ok')

        self.label_win = self.font.render('You win', True, (139, 0, 255))
        self.label_win_shadow = self.font.render('You win', True, (117, 93, 154))
        self.label_win_rect = self.label_win.get_rect(center=(self.height // 2 + 4, self.width // 2 + 4))
        self.label_win_shadow_rect = self.label_win_shadow.get_rect(center=(self.height // 2 - 4, self.width // 2 - 4))

        self.label_loss = self.font.render('You lose', True, (255, 40, 40))
        self.label_loss_shadow = self.font.render('You lose', True, (72, 6, 7))
        self.label_loss_rect = self.label_loss.get_rect(center=(self.height // 2 + 4, self.width // 2 + 4))
        self.label_loss_shadow_rect = self.label_loss_shadow.get_rect(center=(self.height // 2 - 4, self.width // 2 - 4))

    def menu(self):
        x = 0
        while True:
            self.screen.blit(self.menu_img, (0, 0), (x % self.height // 2, self.width // 2, self.height, self.width))
            x += 1

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            if self.button_run.draw():
                self.create_objects()
                self.menu_run = False
                break

            if self.button_exit_menu.draw():
                sys.exit()

            self.screen.blit(self.name, self.name_rect)
            self.screen.blit(self.name_shadow, self.name_shadow_rect)

            pygame.display.flip()
            self.clock.tick(self.fps)

    def pause(self):
        pygame.mixer.music.pause()
        x = 0
        while True:
            self.screen.blit(self.pause_img, (0, 0), (x % self.height // 2, self.width // 2, self.height, self.width))
            x += 1

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            if self.button_continue.draw():
                pygame.mixer.music.unpause()
                break

            if self.button_exit_pause.draw():
                sys.exit()

            pygame.display.flip()
            self.clock.tick(self.fps)

    def game_over(self):
        pygame.mixer.music.pause()
        x = 0
        if self.win:
            channel = self.music_win.play(-1)
        else:
            channel = self.music_lose.play(-1)
        while True:
            self.screen.blit(self.pause_img, (0, 0), (x % self.height // 2, self.width // 2, self.height, self.width))
            x += 1

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            if self.win:
                self.screen.blit(self.label_win, self.label_win_rect)
                self.screen.blit(self.label_win_shadow, self.label_win_shadow_rect)
            else:
                self.screen.blit(self.label_loss, self.label_loss_rect)
                self.screen.blit(self.label_loss_shadow, self.label_loss_shadow_rect)

            if self.button_ok.draw():
                channel.stop()
                pygame.mixer.music.unpause()
                self.menu_run = True
                break

            pygame.display.flip()
            self.clock.tick(self.fps)

    def check_hp(self):
        if not self.ships_right:
            self.win = True
            self.game_over()

        if not self.ships_left:
            self.win = False
            self.game_over()

        for ship in self.ships_right:
            if ship.HP == 0:
                self.ships_right.remove(ship)
                break

        for ship in self.ships_left:
            if ship.HP == 0:
                self.ships_left.remove(ship)
                break

    def controls_AI(self):
        if not self.next_move:
            if self.player_right.fire():
                self.next_move = False
            else:
                self.next_move = True
            self.shooting.append(self.player_right.shot)

    def controls(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.pause()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 \
                    and 640 <= event.pos[0] <= 1150 and 50 <= event.pos[1] < 560 and self.next_move:
                if self.player_left.fire(*event.pos):
                    self.next_move = True
                else:
                    self.next_move = False
                self.shooting.append(self.player_left.shot)

    def run(self):
        while True:
            if self.menu_run:
                self.menu()

            self.screen.fill(self.bg_color)
            self.draw_objects()

            self.controls_AI()
            self.controls()
            self.check_hp()

            pygame.display.flip()

            self.clock.tick(self.fps)


if __name__ == '__main__':
    app = StartGame()
    app.run()
