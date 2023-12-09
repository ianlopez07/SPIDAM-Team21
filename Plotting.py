import matplotlib.pyplot as plt
import numpy as np
import wave
from scipy.io import wavfile

#Plots Waveform


def wave_form(path):

    raw = wave.open(path)

    # reads all the frames
    # -1 indicates all or max frames
    signal = raw.readframes(-1)
    signal = np.frombuffer(signal, dtype="int16")

    # gets the frame rate
    f_rate = raw.getframerate()

    # to Plot the x-axis in seconds
    # you need get the frame rate
    # and divide by size of your signal
    # to create a Time Vector
    # spaced linearly with the size
    # of the audio file
    time = np.linspace(
    0,  # start
        len(signal) / f_rate,
        num=len(signal)
    )

    # using matplotlib to plot
    # creates a new figure
    plt.xlim(1.025, 1.0325)
##plt.ylim(-1, 1)
    plt.figure(1)

    # title of the plot
    plt.title("Sound Wave")

    # label of x-axis
    plt.xlabel("Time")

    # actual plotting
    plt.plot(time, signal)

    # shows the plot
    # in new window
    plt.show()

    # you can also save
    # the plot using
    # plt.savefig('filename')


def reverb_high(path):

    sample_rate, data = wavfile.read(path)
    spectrum, freq, t, im = plt.specgram(data, Fs=sample_rate, NFFT=1024, cmap=plt.get_cmap('autumn_r'))

    def find_target_frequency(freq):
        for x in freq:
            if x > 5000:
                break
        return x

    def frequency_check():
        # identify a frequency to check
        # print (freq)
        global target_frequency
        target_frequency = find_target_frequency(freq)
        index_of_frequency = np.where(freq == target_frequency)[0][0]
        # find sound data for a particular frequency
        data_for_frequency = spectrum[index_of_frequency]
        # change a digital sgnal for all values in decibels
        data_in_db_fun = 10 * np.log10(data_for_frequency)
        return data_in_db_fun

    data_in_db = frequency_check()
    plt.figure(2)
    plt.plot(t, data_in_db, linewidth=1, alpha=0.7, color='#004bc6')
    plt.xlabel('Time (s)')

    plt.ylabel('Power (dB)')

    # find a index of a max value
    index_of_max = np.argmax(data_in_db)
    value_of_max = data_in_db[index_of_max]
    plt.plot(t[index_of_max], data_in_db[index_of_max], 'go')

    # slice our array from a max value
    sliced_array = data_in_db[index_of_max:]
    value_of_max_less_5 = value_of_max - 5

    # find a nearest value of less 5db
    def find_nearest_value(array, value):
        array = np.asarray(array)
        idx = (np.abs(array - value)).argmin()
        return array[idx]

    value_of_max_less_5 = find_nearest_value(sliced_array, value_of_max_less_5)
    index_of_max_less_5 = np.where(data_in_db == value_of_max_less_5)
    plt.plot(t[index_of_max_less_5], data_in_db[index_of_max_less_5], 'yo')

    # slice array from a max-5dB
    value_of_max_less_25 = value_of_max - 25
    value_of_max_less_25 = find_nearest_value(sliced_array, value_of_max_less_25)
    index_of_max_less_25 = np.where(data_in_db == value_of_max_less_25)
    plt.plot(t[index_of_max_less_25], data_in_db[index_of_max_less_25], 'ro')

    rt20 = (t[index_of_max_less_5] - t[index_of_max_less_25])[0]
    # print(f'rt20= {rt20}')
    rt60 = 3 * rt20
    # plt.xlim(0, ((round(abs(rt60), 2)) * 1.5))
    plt.grid()

    plt.show()

    print(f'The RT60 reverb time a freq {int(find_target_frequency(freq))}Hz is {round(abs(rt60), 2)} seconds')


def reverb_mid(path):
    sample_rate, data = wavfile.read(path)
    spectrum, freq, t, im = plt.specgram(data, Fs=sample_rate, NFFT=1024, cmap=plt.get_cmap('autumn_r'))

    def find_target_frequency(freq):
        for x in freq:
            if x > 1000:
                break
        return x

    def frequency_check():
        # identify a frequency to check
        # print (freq)
        global target_frequency
        target_frequency = find_target_frequency(freq)
        index_of_frequency = np.where(freq == target_frequency)[0][0]
        # find sound data for a particular frequency
        data_for_frequency = spectrum[index_of_frequency]
        # change a digital sgnal for all values in decibels
        data_in_db_fun = 10 * np.log10(data_for_frequency)
        return data_in_db_fun

    data_in_db = frequency_check()
    plt.figure(2)
    plt.plot(t, data_in_db, linewidth=1, alpha=0.7, color='#004bc6')
    plt.xlabel('Time (s)')

    plt.ylabel('Power (dB)')

    # find a index of a max value
    index_of_max = np.argmax(data_in_db)
    value_of_max = data_in_db[index_of_max]
    plt.plot(t[index_of_max], data_in_db[index_of_max], 'go')

    # slice our array from a max value
    sliced_array = data_in_db[index_of_max:]
    value_of_max_less_5 = value_of_max - 5

    # find a nearest value of less 5db
    def find_nearest_value(array, value):
        array = np.asarray(array)
        idx = (np.abs(array - value)).argmin()
        return array[idx]

    value_of_max_less_5 = find_nearest_value(sliced_array, value_of_max_less_5)
    index_of_max_less_5 = np.where(data_in_db == value_of_max_less_5)
    plt.plot(t[index_of_max_less_5], data_in_db[index_of_max_less_5], 'yo')

    # slice array from a max-5dB
    value_of_max_less_25 = value_of_max - 25
    value_of_max_less_25 = find_nearest_value(sliced_array, value_of_max_less_25)
    index_of_max_less_25 = np.where(data_in_db == value_of_max_less_25)
    plt.plot(t[index_of_max_less_25], data_in_db[index_of_max_less_25], 'ro')

    rt20 = (t[index_of_max_less_5] - t[index_of_max_less_25])[0]
    # print(f'rt20= {rt20}')
    rt60 = 3 * rt20
    # plt.xlim(0, ((round(abs(rt60), 2)) * 1.5))
    plt.grid()

    plt.show()

    print(f'The RT60 reverb time a freq {int(find_target_frequency(freq))}Hz is {round(abs(rt60), 2)} seconds')


def reverb_low(path):
    sample_rate, data = wavfile.read(path)
    spectrum, freq, t, im = plt.specgram(data, Fs=sample_rate, NFFT=1024, cmap=plt.get_cmap('autumn_r'))

    def find_target_frequency(freq):
        for x in freq:
            if x > 250:
                break
        return x

    def frequency_check():
        # identify a frequency to check
        # print (freq)
        global target_frequency
        target_frequency = find_target_frequency(freq)
        index_of_frequency = np.where(freq == target_frequency)[0][0]
        # find sound data for a particular frequency
        data_for_frequency = spectrum[index_of_frequency]
        # change a digital sgnal for all values in decibels
        data_in_db_fun = 10 * np.log10(data_for_frequency)
        return data_in_db_fun

    data_in_db = frequency_check()
    plt.figure(2)
    plt.plot(t, data_in_db, linewidth=1, alpha=0.7, color='#004bc6')
    plt.xlabel('Time (s)')

    plt.ylabel('Power (dB)')

    # find a index of a max value
    index_of_max = np.argmax(data_in_db)
    value_of_max = data_in_db[index_of_max]
    plt.plot(t[index_of_max], data_in_db[index_of_max], 'go')

    # slice our array from a max value
    sliced_array = data_in_db[index_of_max:]
    value_of_max_less_5 = value_of_max - 5

    # find a nearest value of less 5db
    def find_nearest_value(array, value):
        array = np.asarray(array)
        idx = (np.abs(array - value)).argmin()
        return array[idx]

    value_of_max_less_5 = find_nearest_value(sliced_array, value_of_max_less_5)
    index_of_max_less_5 = np.where(data_in_db == value_of_max_less_5)
    plt.plot(t[index_of_max_less_5], data_in_db[index_of_max_less_5], 'yo')

    # slice array from a max-5dB
    value_of_max_less_25 = value_of_max - 25
    value_of_max_less_25 = find_nearest_value(sliced_array, value_of_max_less_25)
    index_of_max_less_25 = np.where(data_in_db == value_of_max_less_25)
    plt.plot(t[index_of_max_less_25], data_in_db[index_of_max_less_25], 'ro')

    rt20 = (t[index_of_max_less_5] - t[index_of_max_less_25])[0]
    # print(f'rt20= {rt20}')
    rt60 = 3 * rt20
    # plt.xlim(0, ((round(abs(rt60), 2)) * 1.5))
    plt.grid()

    plt.show()

    print(f'The RT60 reverb time a freq {int(find_target_frequency(freq))}Hz is {round(abs(rt60), 2)} seconds')
