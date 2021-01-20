###########################################################
#  Q1. Write some useful information eg.title & names 
#     in some comments at the top of the code
###########################################################
"""
Title = Image processing in Python: assignment 
Date = 1/20/2021 (Day 3)
Names = Jadene Lewis & Long-Ki Chan
Submission Date = 
"""

##### Part 1  ######

###########################################################
#Q2. Import the modules eg. matplotlib.pyplot, numpy and imread from skimage.io
###########################################################

import numpy as np
import matplotlib.pyplot as plt
from skimage import io
from skimage.transform import resize


###########################################################
#Q3. Load the file “lungs.jpg” and display it
###########################################################

#  With the path(location where storing the image) declared
image1_name = '/Users/Longki/ManchesterBioinformaticsCourse_Student/Day3/Code/lungs.jpg' 
lung1 = io.imread(image1_name) 
plt.imshow(lung1) # code to show the image 
plt.show()

print(lung1.shape)
# (569, 600, 3)
# 569 = number of pixels in y axis 
# 600 = number of pixels in x axis 
# 3 = it has 3 channels, red blue and green


###########################################################
#Q4. Plot a histogram of the image
###########################################################
data = np.mean(lung1,-1) 
# np.mean = to find a mean for each pixel over the 3 channels
# from print(lung1.shape) --> this image is (569, 600, 3), -1 will take the "3" channels thing

# data[data >1] = to get rid of the black pixels (0,1) (those around the edges)?
# .flatten() = for flattening the 2D-array to plot the histogram
# bins 
plt.hist(data[data >1].flatten(), bins = 254)
plt.xlabel("Value of Pixels") # this is the intensity - how bright/dark at that particular pixel
plt.ylabel("Number of Pixels") # counting how many pixels in lung1 have the same intensity
plt.show()


# maximum and minimum of values of the array for lung1
print(np.min(lung1), np.max(lung1))
# min = 0; max = 255 for lung1

###########################################################
#Q5. Write a function that displays the CT image with different lindow levels. 
#    The input variables should be the window and the level.
###########################################################
def use_window (window, level): 
    fig = plt.figure() # create a new figure called fig
    

    plt.imshow(data, cmap="Greys_r", vmin=(level - (window/2)), vmax=(level + (window/2)))

# SInce different structures will have differnt intensity (diff value in that pixel), 
# by having this function, it will allow us to apply different windows, 
# and thus can concentrate of the structures of interesting while excluding other parts




from scipy.ndimage import interpolation, rotate
