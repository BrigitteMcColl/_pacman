import pygame as pg


class Sound:
    def __init__(self, bg_music):
        pg.mixer.init()
        pg.mixer.music.load(bg_music)
        pg.mixer.music.set_volume(1.10)
        self.bullet_sound = pg.mixer.Sound('sounds/alien.wav')
        self.bullet_sound.set_volume(0.60)
        self.playing_bg = True
        self.play()
        self.pause_bg()

    def pause_bg(self):
        self.playing_bg = False
        pg.mixer.music.pause()

    def toggle_bg(self):
        self.playing_bg = not self.playing_bg
        self.pause_bg() if not self.playing_bg else self.play()

    def unpause_bg(self):
        self.playing_bg = True
        pg.mixer.music.unpause()

    def play(self):
        self.playing_bg = True
        pg.mixer.music.play(-1, 0.0)

    def stop_bg(self):
        self.playing_bg = False
        pg.mixer.music.stop()