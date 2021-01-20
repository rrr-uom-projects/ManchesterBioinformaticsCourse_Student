# -*- coding: utf-8 -*-
"""
Assignment Part 1
Naomi/Ali/Keith
The #%% allowed me to run it as a cell (similar to jupyter notebook) and
see it the final graphs in a tab in VScode, wont cause any problem if you delete/if it causes issues
for you.
"""

#%%
#Import necessary modules
import matplotlib.pyplot as plt
import numpy as np
from skimage.io import imread
from scipy.ndimage import interpolation
from scipy.ndimage import rotate

#Load images lungs.jpg and lungs2.jpg
folder_input = '/home/ali/git_repos/ICT_module/ManchesterBioinformaticsCourse_Student/Day3/Code/'
lungs_image = np.mean(imread(folder_input + 'lungs.jpg'), -1)
lungs_image_2 = np.mean(imread(folder_input + 'lungs2.jpg'), -1)

#Co-orindates come in a small list this function takes a horizontal and vertical co-oridnate
def adjust_image(coordinate_list):
    Vertical = coordinate_list[0] #takes the vertical co-ordinate value from the input list
    Horizontal = coordinate_list[1] #takes the horizontl co-ordinate value from the input list
    fig = plt.figure() #set up a figure space
    ax1 = fig.add_subplot(111) #add subplots for each thing - images and histogram
    ax1.imshow(lungs_image, cmap="Greys_r", alpha = 0.5) #alpha shows transparency level
    floating = interpolation.shift(lungs_image_2, (Vertical, Horizontal), mode="nearest")
    ax1.imshow(floating, cmap="Greys_r", alpha = 0.5)
    plt.show()

adjust_image([-10,-33])
#Interpolate the top image whilst keeping the bottom image still to overlap

#plt.imshow(shifted_image,cmap="Greys_r")
#plt.show()
# %%
