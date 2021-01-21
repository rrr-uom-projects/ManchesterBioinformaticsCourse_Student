"""
Refer to Assignment.pdf for instructions!

Remember - this is assessed. Make sure your code is nicely structured

Comments are not optional
"""

# -*- coding: utf-8 -*-
"""
Assignment Part 1
Naomi/Ali/Keith
The #%% allowed me to run it as a cell (similar to jupyter notebook) and
see it the final graphs in a tab in VScode, wont cause any problem if you delete/if it causes issues
for you.
"""

#%%
#import necessary modules
import matplotlib.pyplot as plt
import numpy as np
from skimage import io
from skimage.io import imread
import skimage.viewer
from skimage.filters import threshold_otsu, threshold_local

#import the jpg
#replace filepath with your filepath. 'r' converts to real string, allowing for '\' characters
folder_input = '/home/ali/git_repos/ICT_module/ManchesterBioinformaticsCourse_Student/Day3/Code/'
lungs_image = np.mean(imread(folder_input + 'lungs.jpg'), -1)

#A check to make sure the filepath we want matches the filepath entered (makes the filepath above a variable)
image_filepath = folder_input + 'lungs.jpg'
print(f'image filepath = {image_filepath}')

#print(lungs_image) troubleshooting check
#plot the jpg as a histogram
plt.hist(lungs_image[lungs_image > 1].flatten(), bins = 256)
plt.show()

def lindow (level, window):
    fig = plt.figure() #set up a figure space
    ax1 = fig.add_subplot(221) #add subplots for each thing - images and histogram
    ax2 = fig.add_subplot(222)
    ax3 = fig.add_subplot(223)
    vmin = (level - (window / 2)) #set the minimum threshold
    vmax = (level + (window / 2)) #set the maximum threshold
    ax1.hist(lungs_image[lungs_image > 1].flatten(), bins = 254) #plot original histogram
    ax2.imshow(lungs_image, cmap="Greys_r") #plot original image with grey colourmap
    ax3.imshow(lungs_image, interpolation = "none", cmap = "Greys_r", vmin = vmin, vmax = vmax) #plot the image with minimum and maximum values defined by function
    plt.show()

lindow(5,10) # lindow function for most right hand side peak between 5 and 10 is likely air/background
lindow(60,20) # lindow function for the second most peak likely soft tissue/organs
lindow(120,60) #Muscles organs
lindow(200, 100) #dense organs(?) and bone?
lindow(252, 4) #spots of bone or calcification?
# %%
