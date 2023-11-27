class WaveConfig:
    
    def __init__(self, amplitude, frequency_hz, strategy_name, sampling_rate, duration) -> None:
        self.strategy_name = strategy_name
        self.amplitude = int(amplitude)
        self.frequency_hz = int(frequency_hz)
        self.sampling_rate = int(sampling_rate)
        self.duration = int(duration)