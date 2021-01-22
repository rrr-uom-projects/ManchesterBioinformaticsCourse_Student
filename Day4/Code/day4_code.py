"""
ICT in the Clinical Environment - Image Processing in Python: Assignment
Day 4 part 1

Thomas Scott-Adams :  9627185
Jay Miles          : 10806682
"""

# Import required modules
import matplotlib.pyplot as plt
import numpy as np
import pydicom
from scipy.ndimage import interpolation, rotate
from scipy.optimize import brute, differential_evolution
from skimage import io

#Read DICOM files
image1_dcm = pydicom.read_file('IMG-0004-00001.dcm')
image2_dcm = pydicom.read_file('IMG-0004-00002.dcm')
image3_dcm = pydicom.read_file('IMG-0004-00003.dcm')
image4_dcm = pydicom.read_file('IMG-0004-00004.dcm')

#Retrieve and store DICOM image arrays
image1_array = image1_dcm.pixel_array
image2_array = image2_dcm.pixel_array
image3_array = image3_dcm.pixel_array
image4_array = image4_dcm.pixel_array

#Function to apply a specified shift to a specified image
def shift_image(image, shifts):
    shifted_image = interpolation.shift(image, (shifts[0], shifts[1]), mode="nearest")
    return shifted_image

#Function to determine the root-mean-squared cost function metric associated with a shift
def cost_function(fixed_array, floating_array):
    metric = np.sqrt(np.mean((fixed_array - floating_array)**2))
    return metric

#Function to register fixed and floating images and return value of cost function metric
def register_images(shift, fixed, floating):
    shifted_image = shift_image(floating, shift)
    metric = cost_function(fixed, shifted_image)
    return metric

#Function to determine optimal registrations for multiple floating images using brute optimisation
def get_registrations(fixed_image, image_list):
    registrations = []
    for image in image_list:
        registering_shift = brute(register_images, ((-100, 100),(-100,
        100)), args=(fixed_image, image))
        registrations.append(registering_shift)
    registrations_array = np.array(registrations)
    np.save('registrations.npy', registrations_array)
    return registrations, registrations_array

"""
registering_shift = differential_evolution(register_images, ((-100, 100),(-100,100)), args=(fixed, floating))
print(registering_shift['x'])

Use of differential_evolution optimiser as an alternative, this produced very similar results to Brute optimiser.
"""

#Assign floating images
floating_list = [image2_array, image3_array, image4_array]

#Find optimal registrations for each image with respect to image 1
#Unpack the function output into a list of registration shifts and an array
registrations, registration_array = get_registrations(image1_array, floating_list)
print(registrations)

#Apply the optimal shift to each respective image by calling appropriate functions lised above
shifted_images = []
i=0
for image in floating_list:
    shifted_image = shift_image(image, registrations[i])
    best_metric = cost_function(image1_array, shifted_image)
    shifted_images.append(shifted_image)
    i += 1
    print('Best metric' + str(i) + ': ' + str(best_metric))

"""
code from initial steps of part 1 work

figure = plt.figure()
ax = figure.add_subplot(211)
ax.imshow(image1_array, cmap = 'Greys_r')
ax.imshow(shifted_im2, alpha = 0.5)
plt.show()
"""

#The manual shift that registers the first two images is [3, -25]
#The optimal shift to register the two images is [2.99566717, -25.00354501], which gave a cost function metric of 0.5266560909963861