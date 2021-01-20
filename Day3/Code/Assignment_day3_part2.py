"""
ICT in the Clinical Environment - Image Processing in Python: Assignment
Day 3 Part 2

Thomas Scott-Adams :  9627185
Jay Miles          : 10806682
"""

# Import required modules
import matplotlib.pyplot as plt
import numpy as np
from skimage import io
from scipy.ndimage import interpolation, rotate

read_image1 = np.mean(io.imread("lungs.jpg"), -1) # Opening file and averaging its array over the last channel
read_image2 = np.mean(io.imread("lungs2.jpg"), -1) # Opening file and averaging its array over the last channel
read_image3 = np.mean(io.imread("lungs3.jpg"), -1)

fig = plt.figure() # Creating figure space

ax = fig.add_subplot(111)

ax.imshow(read_image1, cmap="Greys_r")                                                         # Add histogram to first subplot
floating = ax.imshow(read_image3, alpha = 0.5)                                                                           # Add original image with colourmap to second subplot



                  

def shift_image(shifts, rotation):
    global read_image3
    shifted_image = interpolation.shift(read_image3, (shifts[0], shifts[1]), mode="nearest")
    read_image3 = interpolation.rotate(shifted_image, rotation, reshape=False)


    floating.set_data(read_image3)
    fig.canvas.draw()

# shift_image([10,20], 0) image moves down by 10 pixels and right by 20 pixels
# shift_image([-17,-40], 0) this provides optimal alignment between lung1 and lung2
# shift_image([-5,-34], -3) this provides optimal alignment between lung1 and lung3



def eventHandler(event):
    up = 0
    whichKey = event.key
    print(whichKey)
    if whichKey == "up":
    #    up = 1
    #print (up)
        shift_image([-1,0], 0)

fig.canvas.mpl_connect('key_press_event', eventHandler)

plt.show()