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
img3 = pydicom.read_file("IMG-0004-00003.dcm")
img4 = pydicom.read_file("IMG-0004-00004.dcm")
#access the object pixel_array from within img1,img2
img1Array = img1.pixel_array
img2Array = img2.pixel_array
img3Array = img3.pixel_array
img4Array = img4.pixel_array
#All floating images in a list
floatingList = [img2Array, img3Array, img4Array]
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
registeringShift = scipy.optimize.brute(registerImages, ((-100,100),(-100,100)), Ns = 20, args = (img1Array, img2Array))

print("The optimum shift is {}".format(registeringShift))

#We tried to use shgo but it didnt optimize
#registering_shift_shgo = scipy.optimize.shgo(registerImages, ((-100,100),(-100,100)), args = (img1Array, img2Array))
#print("The optimum shift is {}".format(registering_shift_shgo))

img2Array = shiftImage(registeringShift, img2Array)
floating.set_data(img2Array)
fig.canvas.draw()
plt.show()

"""Q9: From registering shift it was found that the optimum
shift is [2.99566717, -25.00354501]
Q10:Changing the ranges in the optimizers (without changing the number of grid points, default = 20)
increases the distance between grid points, leading to larger gaps between points, so less accurate.
Increasing the gridpoints will result in a more accurate estimate, but it
will be more computationaly expensive and so slower. The number of gridpoints
to evaluate is Ns**len(x) where Ns is the number of gridpoints and x is the argument in the
function you are testing. So for our function, len(shifts) = 2, so the number of gridpoints
it needs to evaluate is Ns**2. We tried with Ns = 4 and the optimum shift was  [  2.99627115 -24.99393613], and then 
we tried it with Ns = 40 and shift was [  2.99889995 -25.0045823 ] but took a lot longer. 

If you change the cost function the output will be dependant on what cost
function is measuring. The optimizer will look to MINIMISE the cost function
so the cost function must minimise
"""
#empty list to store return from brute
registrations = []
for floating in floatingList:
    registeringShift = scipy.optimize.brute(registerImages, ((-100,100),(-100,100)), args = (img1Array, floating))  
    registrations.append(registeringShift)
#print registrations for a sense check
print("The list of respective registrations for each image is {}".format(registrations))
#empty list to store shifted images arrays
shiftedImageList = []
for (registration, floating) in zip(registrations, floatingList):
    shiftedImage = shiftImage(registration, floating)
    shiftedImageList.append(shiftedImage)
#save numpy file to use later
registrationsArray = np.array(registrations)
np.save("registrations.npy", registrationsArray)

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