###########################################################
#  Q7. start a new stript 
#  Q8. comments at the top of the code
###########################################################
"""
Title = Image processing in Python: assignment 
Date = 1/20/2021 (Day 3)
Names = Jadene Lewis & Long-Ki Chan
Submission Date = 
"""

##### Part 1  ######

###########################################################
#Q9. Import the modules eg. matplotlib.pyplot, numpy and imread from skimage.io
#    and interpolation and rotate from scipy.ndimage
###########################################################

import numpy as np
import matplotlib.pyplot as plt
from numpy.lib.function_base import diff
from skimage import io
from skimage.transform import resize
from scipy.ndimage import interpolation, rotate


###########################################################
#Q10 & 11. Load and display the images “lungs.jpg” and “lungs2.jpg”
###########################################################

# define variables for lungs2 and lungs3, provide the dictionary where the images can be found
image1_name = '/Users/Longki/ManchesterBioinformaticsCourse_Student/Day3/Code/lungs.jpg' 
image2_name = '/Users/Longki/ManchesterBioinformaticsCourse_Student/Day3/Code/lungs2.jpg' 

lung1 = io.imread(image1_name)  
plt.imshow(lung1) # code to show the image lungs3
plt.show()

lung2 = io.imread(image2_name)  
plt.imshow(lung2) # code to show the image lungs2 
plt.show()


###########################################################
#Q12. XII.	Make a plot where you can see both images on the same axes using transparency.
###########################################################
# medical images likes the one we have, they can just have 1 channel per pixel instead of 3.
# thus here we use mean function from numpy to average out the mean from the 3 channels
mean_fixed_image = np.mean(lung1, -1)  
mean_moving_image = np.mean(lung2, -1)   

fig = plt.figure() # create a new figure as a variable  "fig"
ax = fig.add_subplot(111) # # add some axis; we a 1x1 subplot have

# showing the fixed image (lungs)
ax.imshow(mean_fixed_image, cmap="Greys_r")  
# puts 'lungs2.jpg' in front of background
# we set alpha=0.5 for partial transparency. 
# increase or decrease alpha value to make front image less or more see through, respectively
floating = ax.imshow(mean_moving_image, alpha=0.5, cmap="Greys_r")

plt.show()
