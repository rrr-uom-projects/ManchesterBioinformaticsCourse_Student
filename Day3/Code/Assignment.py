"""
Assignment for Day 3
Image Processing in Python

Katherine Winfield (@kjwinfield) and Yongwon Ju (@yongwonju)

This version written on 20 January 2021
"""

import os
import numpy as np
import matplotlib.pyplot as plt
from skimage import io
from skimage.io import imread

#open the image
image = io.imread("lungs.jpg")
plt.imshow(image) #displays the image using matplotlib
#plt.show()
plt.close()

#generate a histogram showing the frequency of different intensities of pixel
image_info = np.mean(image, -1)
plt.hist(image_info[image_info > 1].flatten(), bins=254)
plt.ylabel("Frequency")
plt.xlabel("Light intensity")
plt.show()
plt.close()
'''
The histogram represents the light intensities of each pixel in the x-ray of a patient. The histogram shows four different peaks which encompass the different organs and regions of the body. By changing the window and level, we can filter pixels and show only those that lie in between certain intensities.
- The first peak, between 0 and 10, represents the region next to the patient and also air in the lungs of the patient
- The second peak, between 40 and 60, represents less dense tissue such as fat surrounding the lower abdomen
- The third peak, between 70 and 90, represents more dense organs such as the heart and the liver
- The final peak, at 244-255, represents the bones of the patient
We also note that we find some abnormal tissues in the lungs and near the oesophagus, suggesting that the patient has cancer.
'''

def image_manipulator(window, level):
    plt.imshow(image_info, interpolation='none', cmap="Greys_r",  vmin=(level-(0.5*window)), vmax=(level+ (0.5*window)))
    plt.show()


image_manipulator(40, 110)