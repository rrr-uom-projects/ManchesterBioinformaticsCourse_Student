"""
Refer to Assignment.pdf for instructions!

Remember - this is assessed. Make sure your code is nicely structured

Comments are not optional
"""

"""We are Nermeen and Helena group. This is the first part of Day3 tasks. For this task, we need to load lungs.jpg image and plot 

a histogram image. This allows us to identify the distribution of the values of the lungs.jpg image."""

#Import the required libraries.
import numpy as np #this library deals with the image as an array of numbers
import matplotlib.pyplot as plt #this is used to plot the figures
from skimage import io #this is used for image processing


#Load the image
image= io.imread('lungs.jpg')
#You can use the following two lines to see your image before moving on (just remove the #).
#plt.imshow(image)
#plt.show()

#To plot the figure we use matplotlib
data = np.mean(io.imread("lungs.jpg"), -1) #this will take the mean of all channels. -1 refers to the channels
plt.hist(data[data > 1].flatten(), bins=254)#flatten converts the image into a 
#1D array then a histogram is plotted with 254 bins to reflect each possible gray value
#[data > 1] is used because there LOADS of pixels with the value 0

plt.show()
#print the image after modification
print(np.min(image), np.max(image))
#Here you can display your histogram
plt.imshow(image, cmap="Greys_r", vmin=0.0, vmax=1.0)
#To see your original image before modificaiton
plt.show()

"""
Explaining the histogram - the histogram shows the number of pixels of each 
possible gray value (intensity). y axis = number of pixels, x axis = possible pixel values (intensity)
The x axis goes from 1 to 255 where 1 = almost-black and 255 = white
"""

def level_transform (window, level):
    



