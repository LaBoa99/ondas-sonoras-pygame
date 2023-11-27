import numpy as np
import math

class WaveStrategyY:
    def generate_wave(self, amplitude, angular_frequency, time, sampling_rate = 1000):
        raise NotImplementedError
    
class SinusoidalWave(WaveStrategyY):
    def generate_wave(self, amplitude, angular_frequency, time, sampling_rate = 1000):
        return int(amplitude * math.sin(angular_frequency * time / sampling_rate))

class SquareWave(WaveStrategyY):
    def generate_wave(self, amplitude, angular_frequency, time, sampling_rate=1000):
        
        # Genera una onda senoidal con la frecuencia ajustada
        sin_value = math.sin(2 * math.pi * angular_frequency  * time / sampling_rate)
        
        # Convierte la onda senoidal en una onda cuadrada
        return int(amplitude * (sin_value >= 0))

class TriangularWave(WaveStrategyY):
    def generate_wave(self, amplitude, angular_frequency, time, sampling_rate=1000):
        # Período de la onda triangular
        # Calcular la fase de la onda
        time = time / 1000.0
        phase = (time * angular_frequency) % (2 * math.pi)
        # Calcular la posición y en la onda triangular
        y = 1
        if phase < math.pi:
            y = amplitude * (2 * phase / math.pi - 1)
        else:
            y = amplitude * (3 - 2 * phase / math.pi)
        return int(y)


class SawtoothWave(WaveStrategyY):
    def generate_wave(self, amplitude, angular_frequency, time, sampling_rate = 1000):
        # La función arctan produce una onda diente de sierra
        return int(amplitude * (2 / math.pi) * math.atan(math.tan(0.5 * angular_frequency * time / sampling_rate)))

class InvertedSawtoothWave(WaveStrategyY):
    def generate_wave(self, amplitude, angular_frequency, time, sampling_rate = 1000):
        # Invertir la onda diente de sierra normal
        return -int(amplitude * (2 / math.pi) * math.atan(math.tan(0.5 * angular_frequency * time / sampling_rate)))
    
class ExponentialSawtoothWave(WaveStrategyY):
    def generate_wave(self, amplitude, angular_frequency, time, sampling_rate=1000):
        # Aplicar una función exponencial a la onda diente de sierra
        expo_factor = 0.0001  # Ajusta este valor según sea necesario
        return int(amplitude * math.exp(-expo_factor * time) * (2 / math.pi) * math.atan(math.tan(0.5 * angular_frequency * time / sampling_rate)))




