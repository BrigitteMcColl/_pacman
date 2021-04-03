import pygame as pg
import game_functions as gf
import time



class Launch:
    num_aliens = 4
    pg.init()
    title_font = pg.font.SysFont(None, 128)
    countdown_font = pg.font.SysFont(None, 96)
    points_font = pg.font.SysFont(None, 48)
    images = [pg.image.load('images/' + 'rgd' + str(x) + '.png') for x in range(3, 5)]
    images = [pg.image.load('images/' + 'bgd' + str(x) + '.png') for x in range(3, 5)]
    images = [pg.image.load('images/' + 'pgd' + str(x) + '.png') for x in range(3, 5)]
    images = [pg.image.load('images/' + 'ogd' + str(x) + '.png') for x in range(3, 5)]

    rects = []
    for image in images:
        rects.append(image.get_rect())

    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = game.settings
        self.bg_color = self.settings.launch_bg_color
        self.text_color = self.settings.launch_text_color
        self.title_color = self.settings.launch_title_color

    def draw_text(self, msg, font, text_color, bg_color, centerx, centery):
        image = font.render(msg, True, text_color, bg_color)
        rect = image.get_rect()
        rect.centerx, rect.centery = centerx, centery
        self.screen.blit(image, rect)

    def title_draw(self):
        self.draw_text("PacMan", Launch.title_font, self.title_color, self.bg_color,
                        self.screen_rect.centerx, 100)

    def alien_points_text_draw(self, points, x, y):
        self.draw_text(f'{points} points', Launch.points_font, self.title_color, self.bg_color,
                        x, y)

    def countdown_draw(self, count):
        self.draw_text(f"Game beginning in...", Launch.countdown_font, self.text_color, self.bg_color,
                        self.screen_rect.centerx, self.screen_rect.centery - 200)
        self.draw_text(f"{count} s", Launch.countdown_font, self.text_color, self.bg_color,
                        self.screen_rect.centerx, self.screen_rect.centery - 100)

    def alien_draw(self, number):
        r = self.screen.get_rect()
        img = Launch.images[number]
        img = pg.transform.rotozoom(img, 0, 2)
        rect = img.get_rect()
        rect.centerx = r.centerx
        rect.centery = r.centery + number * 150
        self.alien_points_text_draw((number + 1) * 100, rect.centerx + 200, rect.centery);
        self.screen.blit(img, rect)

    def aliens_draw(self):
        for i in range(Launch.num_aliens):
            self.alien_draw(i)

    def show(self):
        finished = False
        count = 10
        while not finished:
            gf.check_launch_events(self.game)
            self.screen.fill(self.settings.launch_bg_color)
            self.title_draw()
            if (count >= 0):
                self.countdown_draw(count)
            self.aliens_draw()

            count -= 1
            finished = count <= -1
            time.sleep(1)
            pg.display.flip()
        self.game.play()
