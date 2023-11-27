import sys

import pygame

from waves.wave import Wave


class WaveGrid:
    
    def __init__(self, width, height, rows, cols, waves: list[Wave]):
        pygame.init()

        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Visualización de Ondas")

        self.black = (0, 0, 0)
        self.wave_color = (0, 255, 0)

        self.rows = rows
        self.cols = cols

        self.waves = waves[::1]
        self.clock = pygame.time.Clock()
        
        for wave in waves:
            wave.play_sound()

    def draw_grid(self):
        cell_width = self.width // self.cols
        cell_height = self.height // self.rows

        for i in range(1, self.cols):
            pygame.draw.line(self.screen, (30, 30, 30), (i * cell_width, 0), (i * cell_width, self.height), 1)

        for i in range(1, self.rows):
            pygame.draw.line(self.screen, (30, 30, 30), (0, i * cell_height), (self.width, i * cell_height), 1)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            time = pygame.time.get_ticks()

            self.screen.fill(self.black)
            self.draw_grid()

            cell_width = self.width // self.cols
            cell_height = self.height // self.rows

            for i, wave in enumerate(self.waves):
                row, col = divmod(i, self.cols)
                wave.update_wave_points(time, cell_width, cell_height)
                wave.draw_wave(self.screen, self.wave_color, cell_width, cell_height, row, col)

            pygame.display.flip()
            self.clock.tick()