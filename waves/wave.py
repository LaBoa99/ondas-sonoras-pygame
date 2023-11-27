import math
import pygame

from utils.sound_manager import SoundManager


class Wave:
    def __init__(self, amplitude, frequency_hz, id=0):
        self.amplitude = amplitude
        self.frequency_hz = frequency_hz
        self.angular_frequency = 2 * math.pi * frequency_hz
        self.wave_points = []
        self.duration = 1
        self.sampling_rate = 44100
        self.sound = None
        self.strategy = None
        self.soundManager = SoundManager()

    def update_wave_points(self, time, cell_width, cell_height):
        y = self.strategy.generate_wave(self.amplitude, self.angular_frequency, time)
        y = cell_height // 2 - y
        x = time % cell_width - 10
        if x <= 0:
          self.wave_points = []
        if x >= 0 and  x <= cell_width - 10:
            self.wave_points.append((x, y))
        if len(self.wave_points) > cell_width:
            self.wave_points = self.wave_points[-cell_width:]

    def draw_wave(self, screen, color, cell_width, cell_height, i, j):
        scaled_wave_points = [(x + j * cell_width, y + i * cell_height) for x, y in self.wave_points]
        size = len(scaled_wave_points)
        if size > 2:
            if scaled_wave_points[-1][0] < scaled_wave_points[0][0]:
                pygame.draw.lines(screen, color, False, scaled_wave_points[:-2], 2)
            else:
                pygame.draw.lines(screen, color, False, scaled_wave_points, 2)

    def play_sound(self, loop=False):
        if self.sound:
            self.soundManager.play(self.sound, self.id, True)

    def stop_sound(self):
        if self.sound:
            self.sound_manager.stop(self.sound_key)
