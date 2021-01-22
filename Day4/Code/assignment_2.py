# -*- coding: utf-8 -*-
"""

Assignment Part 1 (Day 4)
_________________________

Viveck Kingsley - 10811867

Owen Williams - 10806830

_________________________


"""

# Import Libraries
import matplotlib.pyplot as plt
import numpy as np
from skimage import io
from scipy.ndimage import interpolation
from scipy import optimize 
from scipy.optimize import brute
import pydicom

"""
The DICOM files store more information than just what is used to render a JPEG, such as patient information. This additional information needs to be
excluded, and so when importing this file, this is done using the dcmread().pixel_array function. To ensure this has worked, we used print(patient_image).
"""
# Loading Images and Converting each to a pixel_array
patient_image = pydicom.dcmread("/Users/viveckkingsley/ManchesterBioinformaticsCourse_Student/Day4/Code/IMG-0004-00001.dcm").pixel_array
patient_image2 = pydicom.dcmread("/Users/viveckkingsley/ManchesterBioinformaticsCourse_Student/Day4/Code/IMG-0004-00002.dcm").pixel_array
patient_image3 = pydicom.dcmread("/Users/viveckkingsley/ManchesterBioinformaticsCourse_Student/Day4/Code/IMG-0004-00003.dcm").pixel_array
patient_image4 = pydicom.dcmread("/Users/viveckkingsley/ManchesterBioinformaticsCourse_Student/Day4/Code/IMG-0004-00004.dcm").pixel_array

"""
We used two different colourmaps (Greens_r and Purples_r) for the two images (floating and fixed) to provide a clearer distinction between the two for easier visualisation.
"""
# Figure is made, both images plotted onto it, with transparency and saved
fig = plt.figure()
ax = fig.add_subplot(111)
ax.imshow(patient_image, cmap="Greens_r", alpha = 0.5) # image 1 transparency = 0
floating = ax.imshow(patient_image2, cmap="Purples_r", alpha = 0.2)
#plt.savefig("/Users/viveckkingsley/ManchesterBioinformaticsCourse_Student/Day4/Code/unaligned1_2.png")
#plt.show()

"""
VI:
The shift_image function from the previous task was manipulated to only take shift functions - no longer rotations, and also another argument of 'image'
allowing the user to shift an image of choice without having to substitute it into the function code. Plot updating code was also removed, and image is 
returned. 
"""
def shift_image(shifts, image):
     shifting = interpolation.shift(image, (shifts), mode="nearest")
     return shifting
     
"""
patient_image2 was aligned to the fixed image by trial and error using this translation: ([-25, 2], 0)
"""
# shift_image ([-25, 2], patient_image2) - aligned with patient_image1

"""
VII:
The function mean_squared was made to measure the cost function between two arguments, which is, to compare images and assign a cost. 
This is done by comparing the pixel intensities at corresponding positions between the two images.
When the image is compared to itself, the cost = 0, which is as expected, as there is no difference between the images. 
When patient_image and patient_image2 were used, cost = 684.6, indicating there is considerable difference between the images, as expected.
"""

def mean_squared (fixed, floating):
    return np.mean((fixed - floating)**2)
# cost = mean_squared(patient_image, patient_image) This line output 0, meaning the metric found the two arguments were registered perfectly (because they're the same)
# cost = mean_squared(patient_image, patient_image2) This line output 684.6, meaning the images are very different (not registered)!
#print(cost)

"""
The registerImages function is used to calculate the mean squared cost function between the fixed and floating images, when applying a given shift translation. After a translation, 
the cost that this translation has produced, is measured accordingly. The function allows us to change the definitions of fixed and floating images in the arguments. 
This function returns the cost.
"""

def registerImages (shift, fixed_image, floating_image):
    shifting = shift_image(shift, floating_image)
    cost = mean_squared(fixed_image, shifting)
    return cost
    
registering_shift = optimize.brute(registerImages, ((-100, 100), (-100, 100)), args = (patient_image, patient_image2),Ns=20)
print("The optimum shift is{}".format(registering_shift))

"""
registering_shift is the variable used to contain the automated optimisation of brute force (optimize.brute) which moves the floating image across the fixed image until it finds the lowest
cost value. This uses the registerImages function and works within a range between -100 and 100 on both axes, the floating and fixed images as arguments, and an Ns of 20 (grid points). 
"""
#patient_image2 = shift_image([2.9957, -25.0035], patient_image2)
#floating.set_data(patient_image2)
#fig.canvas.draw()
#plt.show()
"""
IX: 

When patient_image2 is translated using shift_image function with the optimum shift values produced by optimisation, patient_image2 aligned with patient_image1
Optimum shift was found to be: [2.99566717, -25.00354501] 

X: 
According to documentation, the ranges (-100, 100), (-100, 100) produces a grid, in which the function runs, and therefore we found that when we increased the range,
the gaps in the grids increased as well, so it seemed less accurate. 
Increasing grid points (Ns) increased accuracy of alignment, but takes much longer, due to higher demand of computational resources.
Given that the optimiser is based on the cost function, and its purpose is to minimise the cost as much as possible, the registration will be based on whatever the
cost function is changed to. Messing around with the cost function (such as making the **2 into **3), produced wildly different results, and image registration
is not optimised at all. 
"""
"""
XI: 
differential_evolution, which also uses the brute force approach of physically moving one image over the other was found to provide very similar optimum shifts as brute force
when we compared the values, and seemed to take the same amount of time.
"""
#from scipy.optimize import differential_evolution 
#optimize.differential_evolution(registerImages, ((-100, 100), (-100, 100)), args = (patient_image, patient_image2),Ns=20)
"""
This floating_list is a nested array, containing the patient_images loaded earlier. 
The loop was created to find the optimum shift between a fixed image (patient_image) and each floating image in turn (patient_image1,2, & 3), with each loop, optimisation values were being
appended into the registration list.  

"""
floating_list=[patient_image2, patient_image3, patient_image4]
registrations=[]
shifted_imagelist=[]
for float_images in floating_list:
    registering_shift = optimize.brute(registerImages, ((-100, 100), (-100, 100)), args = (patient_image, float_images),Ns=20)
    registrations.append(registering_shift)
print("The list of respective registrations for each image is {}".format(registrations)) 
# A list of respective registrations for each image at which they align with the fixed images, was printed to make sure this loop was working correctly. 

"""
XII:
The above loop stores optimum registrations of each loop in a tuple, the function below saves these optimum registrations in a nested array called shifted_imagelist, which can be used for later use. 
"""

for (registration, float_images) in zip(registrations, floating_list):
    shifted_images = shift_image(registration, float_images)
    shifted_imagelist.append(shifted_images)
    
"""
XIII:
A numpy array from the registrations list was made, and called registrations_arr, to make analysis easier, and was saved to the repo.
"""
registrations_arr = np.array(registrations)
np.save("/Users/viveckkingsley/ManchesterBioinformaticsCourse_Student/Day4/Code/registrations.npy", registrations_arr)























