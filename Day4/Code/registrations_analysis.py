"""
Assignment for Day 4
Image Processing in Python
This script performs registratios analysis.

Katherine Winfield (@kjwinfield) and Yongwon Ju (@yongwonju)

This version written on 21 January 2021
"""

'''
Import libraries 
'''
import numpy as np
import matplotlib.pyplot as plt
from skimage import io
from skimage.io import imread
from scipy import ndimage
from scipy.ndimage import interpolation, rotate
from scipy.optimize import brute, differential_evolution
import pydicom