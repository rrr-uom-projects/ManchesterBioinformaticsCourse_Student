"""
Viveck Kingsley & Owen Williams
"""
# Importing required libraries
import matplotlib.pyplot as plt
import numpy as np
from skimage import io
 
"""
np.mean , -1 takes the average of RGB channels (-1 column)
"""
# Loading image, and displaying it
image = np.mean(io.imread("/Users/viveckkingsley/ManchesterBioinformaticsCourse_student/Day3/Code/lungs.jpg"), -1)
plt.imshow(image)
plt.show()

"""
.flatten is used to collapse the image array into one dimension
[image > 1] is used because the excessive 0 pixel values are much greater in quantity
than the other values, so when filtered out, an eligible histogram is produced
254 bins equates the remaining grey values
"""
# Histogram Plotting
plt.hist(image[image > 1].flatten(), bins=254)
plt.xlabel('Intensity')
plt.ylabel('Pixels')
plt.show()

def window_level(window, level):
    plt.imshow(image, cmap='Greys_r', vmin= level - (window/2), vmax=level+(window/2))
plt.show()
window_level (20,60)

"""
Based on the dark appearance of the lungs, and histogram data, there is a slight peak betwee 20 and 60, which we believe may
be caused by the pixel intensity of the lungs and air. The more frequent intensities observed in the histogram appear between 110 and
140 mainly consitute the majority of tissue, and the last peak at 254 represents the high density bones, appearing white. 
"""