# -*- coding: utf-8 -*-
"""
"""

# Import Libraries
import matplotlib.pyplot as plt
import numpy as np
from skimage import io
from scipy.ndimage import interpolation
from scipy import optimize 
from scipy.optimize import brute
import pydicom

patient_image = pydicom.dcmread("/Users/viveckkingsley/ManchesterBioinformaticsCourse_Student/Day4/Code/IMG-0004-00001.dcm").pixel_array
patient_image2 = pydicom.dcmread("/Users/viveckkingsley/ManchesterBioinformaticsCourse_Student/Day4/Code/IMG-0004-00002.dcm").pixel_array
patient_image3 = pydicom.dcmread("/Users/viveckkingsley/ManchesterBioinformaticsCourse_Student/Day4/Code/IMG-0004-00003.dcm").pixel_array
patient_image4 = pydicom.dcmread("/Users/viveckkingsley/ManchesterBioinformaticsCourse_Student/Day4/Code/IMG-0004-00004.dcm").pixel_array

fig = plt.figure()
ax = fig.add_subplot(111)
ax.imshow(patient_image, cmap="Greens_r", alpha = 0.5) # image 1 transparency = 0
floating = ax.imshow(patient_image2, cmap="Purples_r", alpha = 0.2)
#plt.savefig("/Users/viveckkingsley/ManchesterBioinformaticsCourse_Student/Day4/Code/unaligned1_2.png")
#plt.show()
"""
def shift_image(shifts, r):
    global image3
    shifting = interpolation.shift(image3, (shifts[0], shifts[1]), mode="nearest") 
    image3 = interpolation.rotate(shifting, r, reshape=False)
    floating.set_data(image3)
    fig.canvas.draw()
"""


def shift_image(shifts, image):
     shifting = interpolation.shift(image, (shifts), mode="nearest")
     return shifting
     
#shift_image([-25, 2], patient_image2)
# shift_image ([-25, 2], patient_image2) - aligned with patient_image1

def mean_squared (fixed, floating):
    return np.mean((fixed - floating)**2)
    

# cost = mean_squared(patient_image, patient_image) This line output 0, meaning the metric found the two arguments were registered perfectly (because they're the same)
# cost = mean_squared(patient_image, patient_image2) This line output 684.6, meaning the images are very different (not registered)!
#print(cost)

def registerImages (shift, fixed_image, floating_image):
    shifting = shift_image(shift, floating_image)
    cost = mean_squared(fixed_image, shifting)
    return cost
    
registering_shift = optimize.brute(registerImages, ((-100, 100), (-100, 100)), args = (patient_image, patient_image2),Ns=20)
print("The optimum shift is{}".format(registering_shift))
# Optimum shift: 2.9957 -25.0035 of patient_image2 to patient_image
"""
IX: 
patient_image2 = shift_image([2.9957, -25.0035], patient_image2)
floating.set_data(patient_image2)
fig.canvas.draw()
plt.show()

When patient_image2 is translated using shift_image function with the optimum shift values produced by optimisation, patient_image2 aligned with patient_image1
Optimum shift was found to be: [2.99566717, -25.00354501] 

X: 
According to documentation, the ranges (-100, 100), (-100, 100) produces a grid, in which the function runs, and therefore we found that when we increased the range,
and therefore gaps in the grids, so it seemed less accurate. 
Increasing grid points (Ns) increased accuracy of alignment, but takes much longer, due to higher demand of computational resources.
Given that the optimiser is based on the cost function, and its purpose is to minimise the cost as much as possible, the registration will be based on whatever the
cost function is changed to. Messing around with the cost function (such as making the **2 into **3), produced wildly different results, and image registration
is not optimised at all. 
"""
"""
XI: 
differential_evolution was found to provide the same optimum shifts as brute force, and seemed to take the same amount of time.
"""

floating_list=[patient_image2, patient_image3, patient_image4]
registrations=[]
shifted_imagelist=[]
for float_images in floating_list:
    registering_shift = optimize.brute(registerImages, ((-100, 100), (-100, 100)), args = (patient_image, float_images),Ns=20)
    registrations.append(registering_shift)
print("The list of respective registrations for each image is {}".format(registrations))

for (registration, float_images) in zip(registrations, floating_list):
    shifted_images = shift_image(registration, float_images)
    shifted_imagelist.append(shifted_images)

registrations_arr = np.array(registrations)
np.save("/Users/viveckkingsley/ManchesterBioinformaticsCourse_Student/Day4/Code/registrations.npy", registrations_arr)
"""
XII:
After registering the two images, the other three patient images were loaded in, and pixel arrays of the images were put into a 
list called floating_list, as seen in line 80. A for loop was constructed to loop over the patient images, and register them to the 
fixed patient_image. After registration, optimum shifts for each image were calculated using registering_shift, and stored in registrations list. 
A new list of shifted images was also made (shifted_images), by looping over the floating list with the registrations and floating list providing
required arguments for the shift_image function. 
XIII:
A numpy array from the registrations list was mad, and called registrations_arr, to make analysis easier, and was saved to the repo.
"""





















