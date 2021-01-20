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
from numpy.lib.function_base import diff
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
# np.mean = to find a mean for each pixel over the 3 channels
# from print(lung1.shape) --> this image is (569, 600, 3), -1 will take the "3" channels thing
data = np.mean(lung1,-1) 

# data[data >1] = to get rid of the black pixels (0,1) (those around the edges)?
# these black pixels are likely to be air, 
# and we are only interested in the pixels that are more dense (with a value >1)
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
#Q5. Write a function that displays the CT image with different window levels. 
#    The input variables should be the window and the level.
###########################################################
# SInce different structures will have differnt intensity (diff value in that pixel), 
# by having this function, it will allow us to apply different windows, 
# and thus can concentrate of the structures of interesting while excluding other parts

def diff_windows (window, level): 

    fig = plt.figure() # create a new figure called fig

    ax1 = fig.add_subplot(221) # located at the top left in the figure (the 22 in 221 = 2 rowsx 2 columns)
    ax2 = fig.add_subplot(223) # located at the bottom left in the figureas 
    ax3 = fig.add_subplot(224) # located at the bottom right in the figureas 

    ax1.hist(data[data>1].flatten(), bins = 254) # display histogram
    ax2.imshow(data, cmap="Greys_r") # display lung1 image with grey colourmap
    ax3.imshow(data, interpolation = "none", cmap="Greys_r", vmin = level-(window* 0.5), vmax = level+(window* 0.5)) # display image with grey colourmap, but limited with the input window and level

    plt.show()

# to test the function: 
diff_windows(120,60)
# it works :)
 


###########################################################
#Q6. Identify which parts of the histogram relate to which parts of the image. 
#    Record this information in some comments in your code.
###########################################################
'''
we have 4 peaks in the histogram thus there are 4 regions where the pixels are abundant
this may imply that majorities of the different organs/regions in our patients fall with 4 differnt densities
we thus can change the levels and windows to highlight just those areas with different intensities
'''

diff_windows(10,5) # 1st peak = 0-10
diff_windows(20,60) # 2nd peak = 40-60
diff_windows(30,115) #3rd peak = 100-130
diff_windows(10,240) # 4th peak = 245-255

'''
1st peak = dark area indicating the regions of lungs as it fills with air 
2nd peak = this peak indicates soft tissues (the least dense onces) and fats presented eg. in lower abdomen
3rd peak = this peak indicates denser organs such as liver, kidneys; bones start to appear at this threshold as well
4th peak = this peak should show us bones 
'''




from scipy.ndimage import interpolation, rotate
