"""
A script that imports all of the modules we will need. If this script says you don't have something, you will need to install it using the given command.
"""

try:
    import numpy
except:
    print("Numpy was not found.")
    print("Install it by doing: python -m pip install numpy ")

try:
    import matplotlib
except:
    print("Matplotlib not found, please run:")
    print("python -m pip install matplotlib")

try:
    import jupyter
except:
    print("jupyter not found, please run:")
    print("python -m pip install jupyter")


try:
    import scipy
except:
    print("scipy not found, please run:")
    print("python -m pip install scipy")

try:
    import skimage
except:
    print("scikit image not found, please run:")
    print("python -m pip install scikit-image")

try:
    import pydicom
except:
    print("pydicom not found, please run:")
    print("python -m pip install pydicom")


## below here, optional stuff that will only be used in the extensions

try:
    import pyaudio
except:
    print("pyaudio was not found, if you plan to work on the extension tasks, run this:")
    print("python -m pip install pyaudio wave")

try:
    import colorama
except:
    print("colorama was not found, if you plan to work on the extension tasks, run this:")
    print("python -m pip install colorama")