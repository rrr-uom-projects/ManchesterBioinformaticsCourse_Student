# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 17:24:01 2021

Authors: Rosie Smart and Ruth Keane
Date: 20/01/2021
Title: Image processing in Python Part 2
"""
import matplotlib.pyplot as plt
import numpy as np
import skimage.io
from scipy.ndimage import rotate
from scipy.ndimage import interpolation 

def main():
    Lungs1 = load_image("Lungs.jpg")
    Lungs2 = load_image("Lungs2.jpg")
    

def load_image(file):
    """
    Loads data from file and draws the image. 

    Parameters
    ----------
    file : string
        file you want to load (include directory path if not in current directory)

    Returns
    -------
    file_data : array
        The data loaded from file. 

    """
    #read in the data from file
    file_data = imread(file)
    #display data as an image
    plt.imshow(file_data)
    return file_data

if __name__ == "__main__":
    main()