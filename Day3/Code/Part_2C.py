
import numpy as np
import matplotlib.pyplot as plt
from skimage import io
from skimage.io import imread
from scipy.ndimage import interpolation, rotate
import inspect
import os
# path of the executing script 
actual_path = os.path.dirname(os.path.abspath(inspect.stack()[0][1]))


#name of image
img_name1 = '/lungs.jpg'
img_name3 = '/lungs3.jpg'
#path to the image
img_path1 = actual_path + img_name1
img_path3 = actual_path + img_name3

#import images using imread as a grey scale of values between 0 and 1
lungs1 = io.imread(img_path1, as_gray=True)

lungs3 = io.imread(img_path3, as_gray=True)



fig = plt.figure()
# Lets try to rotate lungs 3 over lungs 1
# This needs the degrees
 ndimage.rotate() rotates in the plane defined by the two axes
lung3_rotate = ndimage.rotate(lungs3, -3, reshape=True)

# We have noticed that lungs3 needs to ve shift a bit to overlap with lungs1
# Let’s do it
lunga3_rotated_shift = interpolation.shift(lung3_rotate, (-25, -45))

# Now we display both images as we did in exercises before.
plt.imshow(lung)
plt.imshow(lunga3_rotated_shift, alpha=0.25)
plt.show()


def eventHandler(event):
    “””
    This function handles deciphering what the user wants us
    to do, the event knows which key has been pressed.
    “””
    up = 0
    down = 1
    
    whichKey = event.key
    if whichKey == “up”:
    up = 1
    print(up)