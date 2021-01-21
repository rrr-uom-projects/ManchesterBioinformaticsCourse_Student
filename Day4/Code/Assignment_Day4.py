"""
Assignment for Day 4
Image Processing in Python
This script overlays two images.

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
# Import the bit of matplotlib that can draw rectangles
import matplotlib.patches as patches

#load the images
patient_image_1  = pydicom.read_file("IMG-0004-00001.dcm").pixel_array
# patient_image_1 = np.mean(im1.pixel_array, -1)
patient_image_2  = pydicom.read_file("IMG-0004-00002.dcm").pixel_array
# patient_image_2 = np.mean(im2.pixel_array, -1)

# print(patient_image_1)
# print(patient_image_2)

# #display image 2 overlaid onto image 1 with transparency
# fig2 = plt.figure()
# ax = fig2.add_subplot(111)
# ax.imshow(im1.pixel_array, cmap='Greys_r')
# ax.imshow(im2.pixel_array, alpha=0.3, cmap='Greys_r')
# plt.title('Images 1 and 2 overlaid')
# plt.show()
# plt.savefig('images_1_and_2_overlaid.png') #saves the figure as a .png file

# #create figure space:
# fig = plt.figure()                      # create figure
# ax = fig.add_subplot(111)               # set the axes
# plt.title('Images overlaid')

# #shift image function:

def shift_image(vector, image, rotation=0):
    '''
    Function to translate and rotate second image and overlay it on the figure space 

    Parameters: 

                vertical    - transation in the y axis
                horizontal  - translation in the x axis
                rotation    - rotation clockwise

    Returns:    
    
                null
    '''

    translated_image = ndimage.rotate(image, rotation, reshape=False) # rotates the image
    rotated_image    = interpolation.shift(translated_image, (vector[0], vector[1]), mode="nearest") # translates the image in the x and y axis

    
    return rotated_image

print(shift_image([20, 20], patient_image_1 , -5))

