"""
# Day 4 Assignment Part 1
## Name: Jadene and Long-Ki
## Date: 21/01/21
## Title: Image processing in Python
"""

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
from scipy.optimize import brute, differential_evolution

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
costFunction(image1_array, image1_array) #returns 0
costFunction(image1_array, image2_array) #returns 684.6462631225586 - positive and large number

#Define an optimizer
def registerImages(shift, fixed, floating):
    shifted_image = shiftImage(shift, floating)
    return np.mean((fixed - shifted_image)**2)

registerImages([0, -25], image1_array, image2_array) #returns cost value of 92.05199432373047- this is high
    
#To automatically register images:
registering_shift = brute(registerImages, ((-100, 100), (-100, 100)), args=(image1_array, image2_array))
#returns shift that optimally registers images and minimizes cost function
registering_shift #this returns array([  2.99566717, -25.00354501]) #shift that the optimizer(brute) applies to minimize the cost function

#Apply registering_shift to floating using shiftImage function, then plot the result over fixed using transparency
shiftImage(registering_shift, image2_array) #does this register the two images? Yes

#Plot newly shifted floating image on top of fixed, using transparency
shifted_image2 = shiftImage(registering_shift, image2_array)
fig4 = plt.figure()
ax = fig4.add_subplot(111)
ax.imshow(image1_array, cmap = "Greens_r")
ax.imshow(shifted_image2, alpha = 0.5, cmap = "Purples_r")
plt.show()

#Trying out different options/parameters for the brute optimizer to see how it affects registration
help(scipy.optimize.brute)

#1: Changing range (xmin, xmax; ymin, ymax) over which optimizer looks for a solution (to apply shift that minimizes cost function)
registering_shift2 = brute(registerImages, ((-50,50), (-50,50)), args=(image1_array, image2_array))
registering_shift2 #returns array([  3.00393757, -25.00177484])

#Plot this shift using transparency
shifted_image3 = shiftImage(registering_shift2, image2_array)
fig5 = plt.figure()
ax= fig5.add_subplot(111)
ax.imshow(image1_array, cmap = "Greens_r")
ax.imshow(shifted_image3, alpha = 0.5, cmap = "Purples_r")
plt.show()
#How does it affect quality of registration?? Quality still good- need to change coordinates???


#2: Changing the number of evaluation points
registering_shift = brute()

#3: Changing cost function?  (to return a different measure of cost) 
  #a) using normalized correlation as a cost function- measures correlation between two images to see how similar they are. Has minimum of -1 (v dissimilar) and max of 
def correlation_coefficient(image1, image2):
    product = np.mean((image1 - image1.mean()) * (image2 - image2.mean()))
    stds = image1.std() * image2.std()
    if stds == 0:
        return 0
    else:
        product /= stds
        return product
    
correlation_coefficient(image1_array, image1_array) #returns 1.0000000000000002- they are identical
correlation_coefficient(image1_array, image2_array) #returns 0.6234105920017828- partially dissimilar (in coordinates)
 
    #b) define new registerImage function which returns correlation coefficient instead of least squares
def registerImages2(shift, fixed, floating):
    shifted_image = shiftImage(shift, floating)
    return correlation_coefficient(fixed, shifted_image)

registerImages2([0,-25], image1_array, image2_array) #returns 0.9493672548087644 #almost maximized the cost function- because this shift is close to well registering the images

registering_shift3 = brute(registerImages2, ((-100, 100), (-100,100)), args = (image1_array, image2_array)
#this affects registration quality by... (quite slow to process on command line- could not get results yet)
    
#Try different optimisers: eg: differential_evolution
help(differential_evolution)
registering_shift4 = differential_evolution(registerImages, ((-100, 100), (-100,100)), args = (image1_array, image2_array))
#this returns  x: array([  3.0044379, -25.0051985])- the shift that optimizer generates that minimizes cost function and results in well-registered images

shifted_image4 = shiftImage([3.0044379, -25.0051985], image2_array)

#plot shift generated by differential_evolution optimizer
fig6= plt.figure()
ax = fig6.add_subplot(111)
ax.imshow(image1_array, cmap = "Greens_r")
ax.imshow(shifted_image4, alpha=0.5, cmap = "Purples_r")
plt.show() #They appear to be well registered

#Now register all the images
floating_list = [image2_array, image3_array, image4_array]
floating_list

registrations = []
for floating in floating_list:
    registering_shift = brute(registerImages, ((-100,100), (-100,100)), args = (image1_array, floating))
    registrations.append(registering_shift)
 
registrations #returns [array([  2.99566717, -25.00354501]), array([-2.99344658, -0.00466909]), array([  1.99695305, -32.99697562])]

#Make a new loop of shifted images by looping over floating list and using shiftImage() function
shiftedimages = []
index=0
for floating in floating_list:
    #for registration in registrations:
    shifted_image = shiftImage(registration[index], floating)
    shiftedimages.append(shifted_image) 
    index+=1
    
#To display a specific shifted image in shiftedimages list        
ax.imshow(shiftedimages[[0]], cmap="Greys_r") #change 0 to 1 or 2 to look at the other shifted images
plt.show()

#Create a numpy array from the list of registering shifts and save as numpy file
registrations_arr = np.array(registrations)
np.save("registrations.npy", registrations_arr)
