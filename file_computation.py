import numpy as np
from scipy.io import wavfile
import wave

class File_Comp:
    def __init__(self, file):
        self.file_path = file

    def return_time(self):
        samplerate, data = wavfile.read(self.file_path)
        return round(data.shape[0] / samplerate, 2)

    def high_resonance(self) -> float:
        wav_file = wave.open(self.file_path, 'rb')
        audio_data = np.frombuffer(wav_file.readframes(wav_file.getnframes()), dtype = np.int16)
        freq_spec = np.fft.fft(audio_data)
        sample_rate = wav_file.getframerate()
        freqs = np.fft.fftfreq(len(freq_spec), d = 1/sample_rate)
        peak_index = np.argmax(np.abs(freq_spec))
        return round(freqs[peak_index], 2)