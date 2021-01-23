# Day 4 Assignment
## Name: Jadene and Long-Ki
## Date: 21/01/21
## Title: Image processing in Python

## PART 1 ##

# Import relevant modules and libraries
import os
import numpy as np
import matplotlib.pyplot as plt
import scipy 
from scipy.ndimage import interpolation, rotate 
import os
import skimage.io 
import skimage
from skimage import io
import io 
import matplotlib.image as mpimg 
import pydicom 
import scipy.optimize

#Set working directory
os.chdir("C:/Users/jaden/bioinformatics-course/code/ManchesterBioinformaticsCourse_Student/Day4/Code")
os.getcwd()

###Load images
#image1_dcm = skimage.io.imread("IMG-0004-00001.dcm", as_gray=True)
#image2_dcm = skimage.io.imread("IMG-0004-00002.dcm", as_gray=True)
#image3_dcm = skimage.io.imread("IMG-0004-00003.dcm", as_gray=True)
#image4_dcm = skimage.io.imread("IMG-0004-00004.dcm", as_gray=True)
#
#plt.imshow(image1_dcm)
#plt.imshow(image2_dcm)
#plt.imshow(image3_dcm)
#plt.imshow(image4_dcm)

#Load and Convert to numpy array
image1_array = pydicom.dcmread("IMG-0004-00001.dcm").pixel_array #returns DICOM object and inside is a pixel array
image2_array=pydicom.dcmread("IMG-0004-00002.dcm").pixel_array
image3_array=pydicom.dcmread("IMG-0004-00003.dcm").pixel_array
image4_array=pydicom.dcmread("IMG-0004-00004.dcm").pixel_array
#when the above is run- should show us the image that is stored inside the DICOM

image1 = plt.imshow(image1_array, cmap = "Greys_r")
image2 = plt.imshow(image2_array, cmap = "Greys_r")
image3= plt.imshow(image3_array, cmap = "Greys_r")
image4 = plt.imshow(image4_array, cmap = "Greys_r")

help(scipy.ndimage.interpolation)

#Then plot these pixel arrays using transparency
fig1 = plt.figure()
ax = fig1.add_subplot(111)
plt.title("Overlaid images with transparency")
ax.imshow(image1_array, cmap="Greys_r")
ax.imshow(image2_array, alpha = 0.5, cmap = "Greys_r")
ax.imshow(image3_array, alpha = 0.5, cmap = "Greys_r")
ax.imshow(image4_array, alpha = 0.5, cmap = "Greys_r")
plt.savefig("fig1.png") #saves figure as PNG file to current working directory 
plt.show()
#this returns a file, with a DICOM header, number of frames, no. of rows, no. of columns.
#Returns image shown in .dcm file
#NB: .dcmread() function is only function required to know from pydicom, to read dcm files. Unless you want to write a dcm file

#Overlay of image 1 and 2
fig2 = plt.figure()
ax = fig2.add_subplot(111)
plt.title("Overlaid images 1 & 2")
ax.imshow(image1_array, cmap = "Greens_r")
#ax.imshow(interpolation.shift(image2_array, (0, -25)), alpha = 0.5, cmap = "Purple_r")
ax.imshow(image2_array, alpha = 0.5, cmap = "Purples_r")
plt.show()

#Overlay of image 1 and 3

#Modified previous shiftImage function
def shiftImage(shifts, image):
    shifted_image = interpolation.shift(image, shifts)
    #fig3 = plt.figure()
    #ax = fig3.add_subplot(111)
    #plt.title("Overlaid images 1 & 2")
    #ax.imshow(image1_array, cmap = "Greens_r")
    #ax.imshow(shifted_image, cmap = "Purples_r", alpha = 0.5)
    plt.imshow(shifted_image, cmap="Greys_r")
    return shifted_image
    #plt.show()

#shift required to register the images: (0, -25) = no movement in y axis and 25 movements left in the x axis.
shiftImage([0, -25], image1_array)
plt.show()

#Define a cost function (mean squared error)- measures performance of registration of images (how well/poorly registered the images are after applying our shift)
#Cost function quantifies the error between predicted and expected values and presents it in the form of a single real number
#We want the cost function to be minimized- in this case the returned value is called COST (or loss/error). Goal is to find the values of model parameters for which cost function returns as small number as possible
#Transformation that gives smallest value of cost function is considered to be the one that gives the best alignment
def costFunction(image1, image2):
    return np.mean((image1 - image2)**2) #this calculates the mean squared error (average of the squared difference between the two input arrays)
#The squaring means that larger mistakes result in more error than smaller mistakes, meaning that the model is punished for making larger mistakes.

#To check that this cost function works
costFunction(image1_array, image2_array) #returns 0
costFunction(image1_array, image2_array) #returns 684.6462631225586 - positive and large number

#Define an optimizer
def registerImages(shift, fixed, floating):
    shifted_image = shiftImage(shifts, floating)
    return np.mean((fixed - shifted_image)**2)

registerImages([10, -25], image1_array, image2_array)
    
#To automatically register images:
registering_shift = brute(registerImages, ((-100, 100), (-100, 100)), args=(image1_array, image2_array))
#returns shift that optimally registers images and minimizes cost function

#Apply floating to registering_shift using shiftImage function, then plot the result over fixed using transparency
shiftImage(shift returned from registering shift, image) #does this register the two images?

from scipy.optimize import brute
help(brute)    
help(np.mean)
    
    