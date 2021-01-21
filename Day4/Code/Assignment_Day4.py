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
import os 

#load the images
patient_image_1  = pydicom.read_file("IMG-0004-00001.dcm").pixel_array
patient_image_2  = pydicom.read_file("IMG-0004-00002.dcm").pixel_array


fig = plt.figure()                                # create figure
ax = fig.add_subplot(111)                         # set the axes
ax.imshow(patient_image_1, cmap="Greys_r")        # put fixed image into the background of the figure

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

def cost_function(image1, image2):
    return np.sqrt(np.mean((image1 - image2)**2)) 

print('The cost function for image 1 and image 1', cost_function(patient_image_1, patient_image_1))
print('The cost function for image 1 and image 2', cost_function(patient_image_1, patient_image_2))

def registerImages(shift, fixed, floating):
    shifted_image = shift_image(shift, floating)
    return cost_function(fixed, shifted_image)

# Testing the registerImages for images 1 and 2
print('The cost function for image 1 and image 1 after moving the second image by vector (1,5)',(registerImages((1,5),patient_image_1, patient_image_1))) # 13.39009454626844
print('The cost function for image 1 and image 1 after moving the second image by vector (0,0)',(registerImages((0,0),patient_image_1, patient_image_1))) # 0.0
print('The cost function for image 1 and image 2 after moving the second image by vector (0,0)',(registerImages((0,0),patient_image_1, patient_image_2))) # 26.16574598826792
print('The cost function for image 1 and image 2 after moving the second image by vector (1,7)',(registerImages((1,7),patient_image_1, patient_image_2))) # 28.295148572489556

# Testing the brute force algorithm to find the shift needed to move image 2 to image 1
# registering_shift = brute(registerImages, ((-100, 100),(-100, 100)), args=(patient_image_1, patient_image_2))
# print(registering_shift) #  [  2.99566717 -25.00354501]
registering_shift = [2.99566717, -25.00354501]
# print((registerImages(registering_shift ,patient_image_1, patient_image_2))) # 45.86745180818286

# Added a function to shift DICOM image
# floating = ax.imshow((shift_image(registering_shift, patient_image_2, -5)), alpha=0.3)
# plt.show()


'''
How does changing the ranges over which the optimizer runs affect the quality of the registration?
when given only positive ranges, it made the images not overlap at all, as that was the "best" position,
once it had the option of moving both directions on the axis the output could overlay the images
How does changing the number of evaluation points affect the registration? What is the downside of trying a lot of points?
Trying a lot of points would mean the code takes longer to run
How does changing the cost function affect the registration?
Efficiency, speed, a better cost function could return a closer image match
'''

# -------------------------------------------------------------------------------------------
# Testing the differential_evolution  algorithm to find the shift needed to move image 2 to image 1
# registering_shift = differential_evolution(registerImages, ((-100, 100),(-100, 100)), args=(patient_image_1, patient_image_2))
# print(registering_shift) #  [  2.99566717 -25.00354501]
# print((registerImages(registering_shift ,patient_image_1, patient_image_2))) # fun: 0.5266560909963861

# floating = ax.imshow((shift_image(registering_shift, patient_image_2, -5)), alpha=0.3)
# plt.show()

floating_list = []

image_files = os.listdir()
for file in image_files:
    if file.endswith('.dcm'):
        floating_list.append(pydicom.read_file(file).pixel_array)

registrations = []
for i in range(len(floating_list)):
    if i == 0: 
        registrations.append([0,0])
    else :
        registering_shift = brute(registerImages, ((-100, 100),(-100, 100)), args=(floating_list[0], floating_list[i]))
        registrations.append(registering_shift)

print(registrations)
registrations_arr = np.array(registrations) 
np.save('registrations.npy', registrations_arr)




