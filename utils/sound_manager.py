import pygame

from utils.singleton import Singleton


class SoundManager(Singleton):
    
    def __init__(self) -> None:
        super().__init__()
        pygame.mixer.init(frequency=44100, size=-16, channels=1)
        self.channels =  [pygame.mixer.Channel(i) for i in range(8)]
    
    def is_busy(self, channel_number):
        return self.channels[channel_number].get_busy()
    
    
    def play(self, sound, channel_number, loop=False):
        if 0 <= channel_number < len(self.channels):
            self.channels[channel_number].play(sound, -1 if loop else 0, fade_ms=0)


    def stop(self, channel_number):
        if 0 <= channel_number < len(self.channels):
            self.channels[channel_number].stop()