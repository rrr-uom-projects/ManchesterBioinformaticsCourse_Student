# Part 1
""" I. Write some useful information like a title and your names in some comments at the top of
the code
II. Import the modules you will need, these include matplotlib.pyplot, numpy and
imread from skimage.io
""" 
import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imread
from scipy.ndimage import interpolation

"""Load the file “CT.jpg” and display it"""
# I cant find the file CT.jpg
# Maybe it is CT_1 in folder Day2?? I dont know
im = io.imread("/Users/monkiky/Desktop/Copy/Day2/Slides/CT_1.bmp",as_gray=True)
fig = plt.figure()

ax = fig.add_subplot(211)
ax2 = fig.add_subplot(212)

ax.imshow(im, interpolation="none", cmap="Greys_r", vmin=0.5, vmax=0.8)
ax2.hist(im.flatten(),bins=255,facecolor="Red",edgecolor="Black")

plt.show()

"""MY CODE BELOW"""

# path of the executing script
actual_path = os.path.dirname(os.path.abspath(inspect.stack()[0][1]))

#name of image
lungs = '/lungs.jpg'







