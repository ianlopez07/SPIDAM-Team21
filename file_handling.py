from pydub import AudioSegment
import os
from wavinfo import WavInfoReader
from scipy.io import wavfile
import scipy.io

# class for handling the audio files
class File_Handling:

    def __init__(self, file_path):
        # find file name/path and its extension
        file_name, file_extension = os.path.splitext(file_path)

        # if statements for converting .m4a and .mp3 files
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
            self.wav_filename = file_path
        else:
            return 'ERROR in converting file. Please submit .m4a, .mp3, or .wav files only'

        # Reduces file to one channel
        audio = AudioSegment.from_file(self.wav_filename, format = '.wav')
        audios = audio.split_to_mono()
        audio_final = audios[0].export(self.wav_filename, format = 'wav')

        # finds and removes the TAG metadata
        with open(self.wav_filename, 'r+b') as file:
            file.seek(-128, os.SEEK_END)
            tag = file.read(3)
            if tag == 'TAG':
                file.write('\x00' * 128-3)
        sys.exit()