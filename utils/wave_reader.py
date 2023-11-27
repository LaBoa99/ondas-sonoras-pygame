from utils.singleton import Singleton

import os
import json

from waves.wave_config import WaveConfig

class WaveReader(Singleton):
      
    def __init__(self) -> None:
        super().__init__()
        self.basepath = ""
        self.filepath = ""
        
    def setBasePath(self, basepath):
        self.basepath = os.path.join(basepath)
        
    def setFilePath(self, filepath):
        self.filepath = os.path.join(self.basepath, filepath)
        
    def read(self) -> list[WaveConfig]:
        if not (len(self.basepath) and len(self.filepath)):
            return []
        
        waves = []
        with open(self.filepath, 'r', encoding='utf-8') as file:
            data = json.load(file)
            if "waves" in data:
                for waveRaw in data["waves"]:
                    waveConfig = WaveConfig(
                        amplitude=waveRaw["amplitude"],
                        frequency_hz=waveRaw["frequency_hz"],
                        strategy_name=waveRaw["strategy_name"],
                        sampling_rate=waveRaw["sampling_rate"],
                        duration=waveRaw["duration"]
                    )
                    waves.append(waveConfig)
        return waves
                