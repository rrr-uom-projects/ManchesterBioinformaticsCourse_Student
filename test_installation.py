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
    print("python -m pip install matplotlib")

try:
    import jupyter
except:
    print("python -m pip install jupyter")


try:
    import scipy
except:
    print("python -m pip install scipy")