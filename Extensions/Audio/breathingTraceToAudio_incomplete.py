import numpy as np
import matplotlib.pyplot as plt
import pyaudio
import wave


## Set up some global variables that will be used in a couple of places
global sampling_rate
sampling_rate = 44100

global volume
volume = 0.5 

def frequencyModulate(signal, baseFrequency=2000.0, frequencyRange=1000.0):
    """
    This function takes a signal and frequency modulates it about a given base frequency, using a given frequency range.
    First it shifts the data into the range [-1,1]
    """
    shiftedSignal = 2.0*(signal - np.min(signal))/(np.max(signal) - np.min(signal)) - 1.0
    return None

def HammingWindow(signal, width=16):
    """
    This function returns the Hamming window array suitable for a given signal.
    Try playing with the width parameter to see its effect on the signal
    """
    return None

## You can create some of the other windowing functions from the pythonBasics notebook here and try them as well

def sample(freq, duration=0.01):
    """
    Takes a frequency and produces a sample wave at that frequency using the requested sample rate and duration.
    """
    # sample values must be in range [-1.0, 1.0]
    global sampling_rate  # use the global setting
    thisSample = (np.sin(2*np.pi*np.arange(sampling_rate*duration)*freq/sampling_rate)).astype(np.float32)
    return thisSample

def playSignal(signal, duration=0.01):
    """
    Opens pyaudio and plays the signal using the samples produced from the sample function
    """
    p = pyaudio.PyAudio()
    global sampling_rate  # integer sampling rate in Hz - using global

    stream = p.open(format=pyaudio.paFloat32,
                channels=1, ## Could you figure out how to do it in stereo?
                rate=sampling_rate,
                output=True)

    for i, freq in enumerate(signal): # Note - enumerate iterates through a list and tells you what index it is at as well.
        stream.write(volume*sample(freq))

    stream.stop_stream()
    stream.close()

    p.terminate()


def recordSignal(signal, filename):
    """
    This fuction will take your frequency modulated signal and write it to a .wav file so you can set it as your ringtone
    """
    wavFile = wave.open(filename, 'w')
    wavFile.setnchannels(1)  ## try to figure out how to convert this to a stereo recording and put both partners' breathing traces in it!
    wavFile.setsampwidth(4)
    wavFile.setframerate(sampling_rate)
    for i, freq in enumerate(signal): # Note - enumerate iterates through a list and tells you what index it is at as well.
        wavFile.writeframes(volume*sample(freq))

    wavFile.close()



## Load the raw breathing trace file


## Plot the data

## Generate a frequency modulated signal from your raw data


## Play the raw signal to see what it sounds like

## Record the signal as a .wav (if you want)


## Use a Hamming window to get rid of some of the noise


## Plot the filtered signal with the original to see the effect


## Play the filtered signal - is it better?

## Save the filtered signal



"""
Some other things to try:
- Figure out how to write stereo .wav files, try writing one partner's breathing in each channel
- Try some other windows. Which one is best?
- Try smoothing the signal after filtering by convolving with a Gaussian.
"""

