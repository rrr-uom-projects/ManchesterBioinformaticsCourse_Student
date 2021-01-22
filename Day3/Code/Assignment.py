"""
Assignment Part 1 (Day 3)
_________________________

Viveck Kingsley - 10811867

Owen Williams - 10806830

_________________________
"""

# I: 
Importing required libraries
import matplotlib.pyplot as plt
import numpy as np
from skimage import io

 
"""
An image can be saved in the form of pixels with each pixel having an x, y and colour. 
The colour is made up of three channels, red, green, and blue (RGB). However, to modify this image, we will convert this to a 
single colour channel so values are now represented as intensities. This is done by averaging values using the "np.mean, -1"
function (-1 column is the last value in the list - colour channel)
"""
# Loading image, and displaying it
image = np.mean(io.imread("/Users/viveckkingsley/ManchesterBioinformaticsCourse_student/Day3/Code/lungs.jpg"), -1)
plt.imshow(image)
plt.show()

"""
.flatten is used to collapse the image array into one dimension, for example ([w, x], [y, z]) becomes [w, x, y, z].
When images are converted to a single channel, pixel values range from 0 to 255 which represents intensity of the signal.
In the script below [image > 1] is used, because the excessive 0 pixel values are much greater in quantity than the other
values, so when filtered out, an eligible histogram is produced.

254 bins equates the remaining grey values
"""
# Histogram Plotting
plt.hist(image[image > 1].flatten(), bins=254)
plt.xlabel('Intensity')
plt.ylabel('Pixels')
plt.show()

"""
Creating a function to adjust image window level, where level adjusts brightness, and window relates to the number of pixel values
that will be incorporated into the display window (low = less pixels)
Adjusting these parameters in conjunction with each other can allow the user to isolate and visualise a particular tissue type, 
often based on tissue density. 
"""
def window_level(window, level):
    plt.imshow(image, cmap='Greys_r', vmin= level - (window/2), vmax=level+(window/2))
plt.show()
window_level (20,60)

"""
Based on the dark appearance of the lungs, and histogram data, there is a slight peak betwee 20 and 60, which we believe may
be caused by the pixel intensity of the lungs and air. The more frequent intensities observed in the histogram appear between 110 and
140 mainly consitute the majority of tissue, and the last peak at 254 represents the high density bones, appearing white. 
"""