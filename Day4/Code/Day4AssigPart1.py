"""
Ed and Sophie day 4 assignment part 1 of the script.
Some of the code is directly copied and edited from the 
day 3 code.

"""
import os
import matplotlib.pyplot as plt 
import numpy as np
from skimage.io import imread
import scipy.optimize
import pydicom
from scipy.ndimage import interpolation
from scipy.ndimage import rotate
#load modules
cwd = os.getcwd()
#find current working directory
newPath = cwd +"\\Day4\\Code"
#path to folder containing lungs.jpg, this is for windows os, for othe os change to /
os.chdir(newPath)
#Load in both .dcm images
img1 = pydicom.read_file("IMG-0004-00001.dcm")
img2 = pydicom.read_file("IMG-0004-00002.dcm")
#access the object pixel_array from within img1,img2
img1Array = img1.pixel_array
img2Array = img2.pixel_array
#declare a figure and add subplot
fig = plt.figure()
ax = fig.add_subplot(111)
#show both images with the floating images axel named floating so that we can translate it 
ax.imshow(img1Array, alpha = 0.5, cmap = "Greens_r")
floating = ax.imshow(img2Array, alpha = 0.2, cmap = "Purples_r")
#this function is copied over from previous assignment
def shiftImage(shifts, image):
    shiftedImage = interpolation.shift(image, shifts, mode="nearest")
    #shiftRotated = rotate(shiftedImage, rotation)
    return shiftedImage
    
"""   
We tested the function and tried the example below, it worked pretty well
img2Array = shiftImage((0, -30), img2Array)
floating.set_data(img2Array)
fig.canvas.draw()
plt.show()
"""
#This is our inital cost function using meansquares
def meanSquare(image1, image2):
    return np.mean((image1-image2)**2)
#We confirmed that the two identical images have msq 0 to test the function
print(meanSquare(img1Array,img1Array))
print(meanSquare(img1Array, img2Array))
#This finds how close the two images are based on a shift
def registerImages(shift, fixedIm, floatingIm):
    shiftedImage = shiftImage(shift, floatingIm)
    cost = meanSquare(fixedIm, shiftedImage)
    return cost
#Using brute this finds the optimum shift and prints it
registering_shift = scipy.optimize.brute(registerImages, ((-100,100),(-100,100)), args = (img1Array, img2Array))
print("The optimum shift is {}".format(registering_shift))




"""
figLung3, axLung3 = plt.subplots(1,1)
axLung3.imshow(lungImage, alpha = 0.5)
axLung3.title.set_text("Lung 3 overlaid Lung 1")
#set alpha to 0.5 so we can see both images are transparent and we can see the overlap
#named the axes for lungImage3 so we can move the image later on.
floating3 = axLung3.imshow(lungImage3, alpha = 0.2)


def shiftImage(shifts, rotation):
    global lungImage3
    lungImage2 = interpolation.shift(lungImage2, shifts, mode="nearest")
    lungImage2 = rotate(lungImage2, rotation)
    floating2.set_data(lungImage2)
    figLung2.canvas.draw()"""