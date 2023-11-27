import math

import numpy as np
import pygame

from strategies.wave_strategies_y import (ExponentialSawtoothWave,
                                          InvertedSawtoothWave, SawtoothWave,
                                          SinusoidalWave, SquareWave,
                                          TriangularWave, WaveStrategyY)
from waves.wave import Wave
from waves.wave_config import WaveConfig


class WaveBuilder:
    
    def amplitude(self,  amplitude) -> None:
        pass
    
    def sound_config(self, sampling_rate=44100, duration=1) -> None:
        pass
    
    def frequency_hz(self, frequency_hz) -> None:
        pass
    
    def strategy(self, strategy: WaveStrategyY) -> None:
        pass
    
    def sound(self) -> None:
        pass
    
class ContinuosWaveBuilder(WaveBuilder):
    
    _wave = Wave(0, 0)
    
    def __init__(self) -> None:
        super().__init__()
        self.reset()
        
    def reset(self):
        self._wave = Wave(0, 0)
    
    def getWave(self) -> Wave:
        wave = self._wave
        self.reset()
        return wave
    
    def amplitude(self,  amplitude) -> None:
        self._wave.amplitude = amplitude
    
    def frequency_hz(self, frequency_hz) -> None:
        self._wave.frequency_hz = frequency_hz
        self._wave.angular_frequency = 2 * math.pi * frequency_hz
    
    def strategy(self, strategy: WaveStrategyY) -> None:
        self._wave.strategy = strategy
        
    def sound_config(self, sampling_rate=44100, duration=1) -> None:
        self._wave.sampling_rate = sampling_rate
        self._wave.duration = duration
    
    def sound(self) -> None:
        upgrade = 0 if self._wave.amplitude > 200 else 1000
        sound_array = np.array([int(self._wave.strategy.generate_wave(self._wave.amplitude + upgrade, self._wave.angular_frequency, t, self._wave.sampling_rate)) for t in range(0, int(self._wave.duration * self._wave.sampling_rate))], dtype=np.int16)
        sound_array = sound_array.copy()
        sound_array = np.repeat(sound_array.reshape(self._wave.sampling_rate * self._wave.duration, 1), 2, axis=1)
        self._wave.sound =  pygame.sndarray.make_sound(sound_array)
        
class WaveDirector:
    
    _strategies = {
        "sinosoidal": SinusoidalWave(),
        "cuadrada": SquareWave(),
        "triangular": TriangularWave(),
        "cierra": SawtoothWave(),
        "cierra_inversa": InvertedSawtoothWave(),
        "cierra_exponencial": ExponentialSawtoothWave()
    }
    
    def __init__(self) -> None:
        self._builder = None
        
    def getBuilder(self) -> WaveBuilder:
        return self._builder
    
    def setBuilder(self, builder: WaveBuilder) -> None:
        self._builder = builder
        
    def buildWaveFromConfig(self, waveConfig: WaveConfig):
        self._builder.amplitude(waveConfig.amplitude)
        self._builder.frequency_hz(waveConfig.frequency_hz)
        self._builder.sound_config(waveConfig.sampling_rate, waveConfig.duration)
        self._builder.strategy(self.__findStrategy(waveConfig.strategy_name))
        self._builder.sound()
        return self._builder.getWave()
    
    def __findStrategy(self, strategy_name):
        name = strategy_name.lower()
        return self._strategies.get(name, SinusoidalWave())
        