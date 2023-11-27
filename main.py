import os
from builder.wave_builder import ContinuosWaveBuilder, WaveDirector

from utils.sound_manager import SoundManager
from utils.wave_reader import WaveReader
from waves.wave_grid import WaveGrid

if __name__ == "__main__":
    sound_manager = SoundManager()
    waveReader = WaveReader()
    waveReader.setBasePath(os.path.dirname(__file__))
    waveReader.setFilePath("wave.json")
    
    waveConfigs = waveReader.read()
    
    director = WaveDirector()
    director.setBuilder(ContinuosWaveBuilder())
    
    waves = []
    for i, waveConfig in enumerate(waveConfigs):
        wave = director.buildWaveFromConfig(waveConfig)
        wave.id = i
        waves.append(wave)
    
    wave_grid = WaveGrid(1080, 720, 2, 3, waves)
    wave_grid.run()
