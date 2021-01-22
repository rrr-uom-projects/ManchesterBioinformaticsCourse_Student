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
image2_array=pydicom.dcmread("IMG-0004-00002.dcm") pixel_array
image3_array=pydicom.dcmread("IMG-0004-00003.dcm")
image3_array=pydi
#when the above is run- should show us the image that is stored inside the DICOM

#Then plot these pixel arrays
fig2 = plt.figure()
ax = fig2.add_subplot(111)
ax.imshow(image1_array, cmap="Greys_r")
plt.show()

#this returns a file, with a DICOM header, number of frames, no. of rows, no. of columns.
#Returns image shown in .dcm file