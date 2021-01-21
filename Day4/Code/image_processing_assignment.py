# -*- coding: utf-8 -*-
"""
Assignment 2 image processing assignment
Naomi/Ali/Keith
The #%% allowed me to run it as a cell (similar to jupyter notebook) and
see it the final graphs in a tab in VScode, wont cause any problem if you delete/if it causes issues
for you.
"""

#%%
#Import necessary modules
import matplotlib.pyplot as plt
import numpy as np
from skimage.io import imread
from scipy import ndimage
from scipy.ndimage import interpolation, rotate
from scipy.optimize import brute, differential_evolution
import pydicom 

#shiftimage function from previous assignment 
def shiftimage(image,coordinate_list):
    Vertical = coordinate_list[0] #takes the vertical co-ordinate value from the input list
    Horizontal = coordinate_list[1] #takes the horizontl co-ordinate value from the input list
    #Rotational = coordinate_list[2] #takes the rotational co-ordinate from the list
    shifted_image = interpolation.shift(image, (Vertical, Horizontal), mode="nearest") #shifts the image on the x,y as per the input co-ordinates
    #shifted_image = ndimage.rotate(xy_shift, Rotational, reshape=False)#rotates as per the input co-ordinates, reshape stops it squashing the image
    return shifted_image #Changes the lungs_image_3 variable as per the above changes

def mean_squared_error(image1, image2):
	# the 'Mean Squared Error' between the two images is the
	# sum of the squared difference between the two images;
	error = np.sum((image1.astype("float") - image2.astype("float")) ** 2)
	error /= float(image1.shape[0] * image1.shape[1])
	return error # return the MSE, the lower the error, the more "similar" the two images are

def register_images(shift,fixed,floating):
    shifted_image = shiftimage(floating,shift)
    cost_value = mean_squared_error(fixed,shifted_image)
    return cost_value


# Load the images “IMG-0004-00001.dcm”and “IMG-0004-00002.dcm”. 
# get the pixel data from the dicom file as a numpy array using img1_array = img1_dcm.pixel_array

patientImage = pydicom.read_file("IMG-0004-00001.dcm")
patientImage2 = pydicom.read_file("IMG-0004-00002.dcm")
patientImage3 = pydicom.read_file("IMG-0004-00003.dcm")
patientImage4 = pydicom.read_file("IMG-0004-00004.dcm")
#print(patientImage)
#print(patientImage2)

#get the pixel data from the dicom file as a numpy array using img1_array = img1_dcm.pixel_array
img1_array = patientImage.pixel_array 
img2_array = patientImage2.pixel_array
img3_array = patientImage3.pixel_array 
img4_array = patientImage4.pixel_array

floating_list = [img1_array,img2_array,img3_array,img4_array]

registrations = []
for floating in floating_list:
    registering_shift = brute(register_images, ((-10, 10),(-10, 10)), args=(img1_array, floating))
    registrations.append(registering_shift)
print(registrations)
registrations_arr = np.array(registrations)
np.save("registrations.npy",registrations_arr)

shifted_images = []
for i in range(len(floating_list)):
    shifted = shiftimage(floating_list[i], registrations[i])
    shifted_images.append(shifted)
print(shifted_images)
#print(img1_array)
#print(img2_array)

#Display the imagesusing transparency so that you can see they are not registered.Save this as a png with a sensible name.Add it to your repo
fig = plt.figure() #set up a figure space, I had to take this out the function to be able to call it outside of the function
ax = fig.add_subplot(111) #add subplots for each thing - images and histogram
ax.imshow(img1_array, cmap="Greens_r")  #designates the static image on the plot

# registers the image
#shifted = shiftimage(img2_array, [3,-25,0]) registering by eye
#registering_shift = brute(register_images, ((-100, 100),(-100, 100)), args=(img1_array, img2_array)) #registering shift returned coords [  2.99566717 -25.00354501]
#print(registering_shift)

shifted = shiftimage(img2_array, registering_shift)

floating = ax.imshow(shifted, cmap="Purples_r", alpha = 0.5) # and designates the floating image, alpha shows transparency level
#plt.savefig('Patient Image overlay (step5).png') #Saves original image
#plt.show() #Shows plot

#image registration requires a cost function test
#Test = mean_squared_error(img1_array, img1_array) #returns 0 when both images are the same so seems to work
#Test2 = mean_squared_error(img1_array, img2_array) # returns a different value
#print(Test, Test2)

#image register_images function test
#Tester= register_images([1,1,1], img1_array, img2_array)
#print(Tester)



