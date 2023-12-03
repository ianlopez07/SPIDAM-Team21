from wavinfo import WavInfoReader
from scipy.io import wavfile
import scipy.io

path = 'test_wavs/16bit4chan.wav'

info = WavInfoReader(path)

adm_metadata = info.adm
ixml_metadata = info.ixml
#print(f"metadataadm= {info.adm}")
#print(f"metadataixml = {info.ixml}")

wav_fname = 'test_wavs/16bit4chan.wav'
samplerate, data = wavfile.read(wav_fname)
print(f"number of channels = {data.shape[len(data.shape) - 1]}")
length = data.shape[0] / samplerate
print(f"length = {length}s")

##print(f"number of channels = {data.shape[-1]}")
##length = data.shape[0]/samplerate
##print(f"length = {length}s")

#fs, data = wavfile.read('test_wavs/16bit2chan.wav')
#print(f"number of channels = {data.shape[-1]}")
#wavfile.write("test_wavs/16bit2chan.wav", fs, data[0])
#print(f"number of channels = {data.shape[-1]}")


