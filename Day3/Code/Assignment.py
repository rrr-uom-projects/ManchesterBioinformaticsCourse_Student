"""
ICT in the Clinical Environment - Image Processing in Python: Assignment
Day 3 Part 1

Thomas Scott-Adams :  9627185
Jay Miles          : 10806682
"""

# Import required modules
import matplotlib.pyplot as plt
import numpy as np
from skimage import io

read_image = np.mean(io.imread("lungs.jpg"), -1) # Opening file and averaging its array over the last channel

"""
Generating a Figue which includes histogram of image pixel intensities, the original image, 
and a processed version of the image subject to the specified window and level.
"""
def apply_window(window, level):
    
    fig = plt.figure() # Creating figure space

    ax = fig.add_subplot(311)
    ax2 = fig.add_subplot(312)    # Creating subplot spaces with the figure
    ax3 = fig.add_subplot(313)

    ax.hist(read_image[read_image > 1].flatten(), bins=254)                                                           # Add histogram to first subplot
    ax2.imshow(read_image, cmap="Greys_r")                                                                            # Add original image with colourmap to second subplot
    ax3.imshow(read_image, interpolation="none", cmap="Greys_r", vmin=level - (window/2), vmax=level + (window/2))    # Add processed image (see above) to third subplot

    plt.savefig("W"+str(window)+"_L"+str(level)+".png", format = "png")   # Saving png file of figure image into local directory
    plt.show()                                                            # Display figure

apply_window(98, 199) #Call the apply_window function

"""
Histogram Peak from 0 to 10 (window = 10, Level = 5) represents Air (within the lungs). the lungs appeared dark as did the area surrounding the patients body.
Histogram Peak from 25 to 85 (window = 60. level = 55) represents fat, regions where fat tends to be found, begin to appear in grey.
Histogram Peak from 85 to 150 (window = 65, level = 120) represents Muscle and organs. the liver is now clearly visible.
Histogram region from 150 to 247 (windo = 98, level = 199) represents more dense organs such as heart and kidney, as well as bone.
Histogram Peak from 247 to 255 (window = 8, Level = 251) represents bone, as the ribs (in cross-section), right clavicle and other bones are all that is visible.
"""