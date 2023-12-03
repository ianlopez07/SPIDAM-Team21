from pydub import AudioSegment
import os
from wavinfo import WavInfoReader
from scipy.io import wavfile
import scipy.io

class File_Handling:

    def __init__(self, file_path):
        file_name, file_extension = os.path.splitext(file_path)
        if file_extension == '.m4a':
            self.wav_filename = file_name + '.wav'
            sound = AudioSegment.from_file(file_path, format='m4a')
            file_handle = sound.export(self.wav_filename, format='wav')
        elif file_extension == '.mp3':
            self.wav_filename = file_name + '.wav'
            sound = AudioSegment.from_file(file_path, format='mp3')
            file_handle = sound.export(self.wav_filename, format='wav')
        elif file_extension == '.wav':
            self.wav_filename = file_path
        else:
            return 'ERROR in converting file. Please submit .m4a, .mp3, or .wav files only'
        audio = AudioSegment.from_file(self.wav_filename, format = '.wav')
        audios = audio.split_to_mono()
        audio_final = audios[0].export(self.wav_filename, format = 'wav')

test = File_Handling('M4a_files\\CS_test_recording.m4a')