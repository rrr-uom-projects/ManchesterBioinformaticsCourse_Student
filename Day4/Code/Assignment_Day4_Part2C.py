#!/usr/bin/env python
# coding: utf-8
 
# Image processing in Python: assignment Day 4
# Igor and Manuel
# Part2
 
 
"""
XXIII.  Testing metric in another ROI
"""
 
# Let’s import needed with the next lines of code.
import numpy as np
import matplotlib.pyplot as plt
from skimage import io
from skimage.io import imread
from scipy.ndimage import interpolation, rotate
from scipy.optimize import brute
import inspect
import os
import pydicom
#to import cv2 please: pip install opencv-python
import cv2
from PIL import Image as PIL


# Now we copy the shiftImages function
 
def shiftImage(shifts, image):
  #shits is an input, which is a list of two values example [value1, value2] that shifts the image.
  # Value1 moves image up or down, value 2 moves image left or right.
  shifted_image = interpolation.shift(image, (shifts[0], shifts[1]), mode="nearest")
  return shifted_image
 
 
# path of the executing script
actual_path = os.path.dirname(os.path.abspath(inspect.stack()[0][1]))
#name of image
img_name1 = '/IMG-0004-00001.dcm'
img_name2 = '/IMG-0004-00002.dcm'
img_name3 = '/IMG-0004-00003.dcm'
img_name4 = '/IMG-0004-00004.dcm'

#path to the image
img_path1 = actual_path + img_name1
img_path2 = actual_path + img_name2
img_path3 = actual_path + img_name3
img_path4 = actual_path + img_name4
 
#import images using pydicom.read_file
img1 = pydicom.read_file(img_path1)
img2 = pydicom.read_file(img_path2)
img3 = pydicom.read_file(img_path3)
img4 = pydicom.read_file(img_path4)
# To get the a numpy.ndarray containing the pixel data from the sataset, we just use ".pixel_array"
img1_array = img1.pixel_array
img2_array = img2.pixel_array
img3_array = img3.pixel_array
img4_array = img4.pixel_array
 

# Load registration
registrations = np.load('registrations.npy')

# Now, we will apply the registration with these four images
floating_list = [img2_array, img3_array, img4_array]

#This for loop modifies the image postion based on the registeres values obtain from the previouse function
shifted_images = floating_list # Here we copy the images from the floating list which will be modified
for i in range(0, len(floating_list), 1): # this loop is designed to get i values from 0 to the number of images in the floating_list 
    shifted_images[i] = shiftImage(registrations[i], floating_list[i]) # i is used here to call the specific image and correspoding registration values 


# Combine frist image with images in the floating list:
floating_list = [img1_array] + floating_list

"""Here we are using a function to diplay images with specified window and level values to identify pixel shreshold for tumour"""
def displayImageWinLevel(image, window, level):
    fig, (ax1, ax2, ax3, ax4) = plt.subplots(1, 4)
    fig.suptitle('Four images side-by-side ')
    ax1.title.set_text('1st timed scan')
    ax2.title.set_text('2nd timed scan')
    ax3.title.set_text('3rd timed scan')
    ax4.title.set_text('4th timed scan')
    ax1.imshow(image[0], cmap="Greys_r", vmin=window, vmax=level)
    ax2.imshow(image[1], cmap="Greys_r", vmin=window, vmax=level)
    ax3.imshow(image[2], cmap="Greys_r", vmin=window, vmax=level)
    ax4.imshow(image[3], cmap="Greys_r", vmin=window, vmax=level)
    plt.savefig("Bone.png", dpi=1200)
    plt.show()
#Min value for window and level is 0 and maximum is 1


#The region that containes the tumour [50:75, 301:326]

croped_img = floating_list
pixMinMax = []
for i in range(0, len(croped_img), 1): # this loop is designed to get i values from 0 to the number of images in the floating_list 
    croped_img[i] = croped_img[i][90:106, 329:345] # crop to the region of interest
    #croped_img[i] = rotate(croped_img[i], -20) # roate the image to a good postion to further remove background in the corner
    #croped_img[i] = croped_img[i][0:30, 0:26] # remove additional background
    pixMinMax.append(cv2.minMaxLoc(np.float32(croped_img[i]))) #get maximum and minimim pixel value and corresponding location
    print(pixMinMax[i]) 
# Get the minimum and maximum pixel value for each of the images 

# The best window and level for tumour is 40 and 68
displayImageWinLevel(image=croped_img, window=40, level=68)

'''METRICS TO EVALUATE TUMOUR REGRESSION'''
pixels = []  #get values for all pixels in image
tumour = [] # get number of pixels that have values above 40
PIL_img = [] #Use another imaging function from PIL module
for i in range(0, len(croped_img), 1):
    PIL_img.append(PIL.fromarray(croped_img[i])) # covert array images to PIL image format
    print(PIL_img[i].size) #Get size information aboout the iage
    pixels.append(PIL_img[i].getdata()) #Get vixel values for all pixels in a list
    tumour.append(sum(i>39 for i in PIL_img[i].getdata())) #Get number of pixels that have a value 40 or higher (this is to remove backround information)
    print(tumour[i]) 


tumour_area = [item/max(tumour)*100 for item in tumour] #Get the tumour area in % 
reg = round(max(tumour_area)-min(tumour_area),1) #calcualte the maximum change in tumour area  and round the number to 1 decimal point
print(tumour_area)

# PLOT THE DATA ON A GRAPH:
x = ["1st scan", "2nd scan", "3rd scan", "4th scan"]
plt.plot(x, tumour_area, '.r-')
plt.ylabel("Bone area/%")
plt.title("Change in intensity at 4 differen times ".format(reg))
plt.savefig("Bone_change.png", dpi=1200)
plt.show()



'''METRIC test showed no change in another area - refer to images called Bone.png and Bone_change.png'''
