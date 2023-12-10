from pydub import AudioSegment
import os
from wavinfo import WavInfoReader
from scipy.io import wavfile
import scipy.io
import taglib

# class for handling the audio files
class File_Handling:

    def __init__(self, file_path):
        # find file name/path and its extension
        file_name, file_extension = os.path.splitext(file_path)

        # if statements for converting .m4a and .mp3 files and removes metadata
        if file_extension == '.m4a':
            self.wav_filename = file_name + '.wav'
            sound = AudioSegment.from_file(file_path, format='m4a')
            file_handle = sound.export(self.wav_filename, format='wav')
        elif file_extension == '.mp3':
            self.wav_filename = file_name + '.wav'
            sound = AudioSegment.from_file(file_path, format='mp3')
            file_handle = sound.export(self.wav_filename, format='wav')

        # defaults for files that are already .wav and other unsupported extensions
        elif file_extension == '.wav':
            self.wav_filename = file_name + 'NEW' + '.wav'
            sound = AudioSegment.from_file(file_path, format = 'wav')
            file_handle = sound.export(self.wav_filename, format = 'wav')
        else:
            print('ERROR in converting file. Please submit .m4a, .mp3, or .wav files only')

        # reduces file to one channel
        audio = AudioSegment.from_file(self.wav_filename, format = '.wav')
        audios = audio.split_to_mono()
        audio_final = audios[0].export(self.wav_filename, format = 'wav')