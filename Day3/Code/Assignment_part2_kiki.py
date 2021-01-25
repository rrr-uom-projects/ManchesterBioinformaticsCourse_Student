###########################################################
#  Q7. start a new stript 
#  Q8. comments at the top of the code
###########################################################
"""
Title = Image processing in Python: assignment 
Date = 1/20/2021 (Day 3)
Names = Jadene Lewis & Long-Ki Chan
Submission deadline = 25/1/2021
"""

##### Part 2  ######

###########################################################
#Q9. Import the modules eg. matplotlib.pyplot, numpy and imread from skimage.io
#    and interpolation and rotate from scipy.ndimage
###########################################################

import numpy as np
import matplotlib.pyplot as plt
from numpy.lib.function_base import diff
from skimage import io
from skimage.transform import resize
from scipy.ndimage import interpolation, rotate



###########################################################
#Q10 & 11. Load and display the images “lungs.jpg” and “lungs2.jpg”
###########################################################

# define variables for lungs2 and lungs3, provide the dictionary where the images can be found
image1_name = '/Users/Longki/ManchesterBioinformaticsCourse_Student/Day3/Code/lungs.jpg' 
image2_name = '/Users/Longki/ManchesterBioinformaticsCourse_Student/Day3/Code/lungs2.jpg' 

lung1 = io.imread(image1_name)  
plt.imshow(lung1) # code to show the image lungs3
plt.show()

lung2 = io.imread(image2_name)  
plt.imshow(lung2) # code to show the image lungs2 
plt.show()



###########################################################
#Q12. XII.	Make a plot where you can see both images on the same axes using transparency.
###########################################################

# medical images likes the one we have, they can just have 1 channel per pixel instead of 3.
# thus here we use mean function from numpy to average out the mean from the 3 channels
mean_fixed_image = np.mean(lung1, -1)  
mean_floating_image = np.mean(lung2, -1)   

fig = plt.figure() # create a new figure as a variable  "fig"
ax = fig.add_subplot(111) # # add some axis; we a 1x1 subplot have

ax.imshow(mean_fixed_image, cmap="Greys_r")  # showing the fixed image (lungs)
floating = ax.imshow(mean_floating_image, cmap="Greys_r", alpha=0.4)
plt.title('Overlaid image of images "lungs" and "lungs2"')
plt.show()
"""
here we put 'lungs2.jpg' in front of background
we set alpha=0.4 for partial transparency. 
increase or decrease alpha value to make front image less or more see through, respectively
"""


 
"""
-----ps. to place the image lungs2 (floating) on top of lungs (background) without a function----
fig = plt.figure() # create a new figure as a variable  "fig"
ax = fig.add_subplot(111) # # add some axis; we a 1x1 subplot have
ax.imshow(mean_fixed_image, cmap="Greys_r")  
sifted_mean_floating_image = interpolation.shift(mean_floating_image, (-15, -40), mode = "nearest")
shifted_floating = ax.imshow(sifted_mean_floating_image, cmap="Greys_r", alpha=0.4)
plt.title ('Aligned Overlaid images of "lungs" and "lungs2"')
plt.show()
"""



###########################################################
#Q13. Write a function that shifts the 2nd image given an input argument called shifts which is a list of shifts horizontally and vertically. 
# When your function is called, the command shiftImage([10,20]) should shift the image down 10 pixels and to the right 20 pixels. 
###########################################################

def shiftImage(shifts):
    global mean_floating_image #this allows the access of mean_floating_image (defined outisde) inside the function
    shifting_image = interpolation.shift(mean_floating_image, shifts, mode="nearest")
    floating.set_data(shifting_image) #set the shifting to floating image
    fig.canvas.draw() #draws update to canvas

###########################################################
#Q14. Evaluate your function by calling it. What does shiftImage([10,20]) do?
###########################################################
fig = plt.figure() # create a new figure as a variable  "fig"
ax = fig.add_subplot(111) # # add some axis; we a 1x1 subplot have
ax.imshow(mean_fixed_image, cmap="Greys_r")  # showing the fixed image (lungs)
floating = ax.imshow(mean_floating_image, cmap="Greys_r", alpha=0.4)
shiftImage([10,20])
plt.title('Overlaid images of "lungs" and shifted "lungs2" by [10,20]')
plt.show()

"""
 this will translate the 10 pixels to the bottom & 20 pixels to the right.
(if negative inpiut --> images will be moved up/to the left)
"""

###########################################################
#Q15. What are the shifts needed to align the images? Make a note of them in some comments.
###########################################################
fig = plt.figure() # create a new figure as a variable  "fig"
ax = fig.add_subplot(111) # # add some axis; we a 1x1 subplot have
ax.imshow(mean_fixed_image, cmap="Greys_r")  # showing the fixed image (lungs)
floating = ax.imshow(mean_floating_image, cmap="Greys_r", alpha=0.4)
shiftImage([-15,-40])
plt.title('Overlaid images of "lungs" and shifted "lungs2" by [-15,-40]')
plt.show()
""" 
shift required for alignements will be (-15, -40)
which means: 
-15 --> move up for 15 pixels  & 
-40 --> 40 pixels to the left
"""

###########################################################
#Q16.Modify your code to include rotations. 
#    Load “lungs3.jpg” and use that as your floating image instead. 
#    What are the shifts/rotations required to align the images now?
###########################################################
""" 16.1 - load image lungs3"""
image3_name = '/Users/Longki/ManchesterBioinformaticsCourse_Student/Day3/Code/lungs3.jpg' 
lung3 = io.imread(image3_name)  
plt.imshow(lung3) # code to show the image lungs3
plt.show()

new_floating_image = np.mean(lung3, -1) # set lungs3.jpg as the new floating image. 

"""16.2 - Modify the function to include rotations."""

def shift_rotate_Image(shifts, rotation):
    global new_floating_image 
    rotating_image = rotate(new_floating_image, rotation, reshape=False) # set reshape to false so the image will not be changing in size
    shifting_image = interpolation.shift(rotating_image, shifts, mode="nearest")
    floating.set_data(shifting_image) 
    fig.canvas.draw() #draws update to canvas

"""16.3 - shifts/rotations required to align the images?"""
# differnt combinations were test; ([-7, -34],-3) as shown below, seems to align 2 images the best

fig = plt.figure() # create a new figure as a variable  "fig"
ax = fig.add_subplot(111) # # add some axis; we a 1x1 subplot have
ax.imshow(mean_fixed_image, cmap="Greys_r")  # showing the fixed image (lungs)
floating = ax.imshow(new_floating_image, cmap="Greys_r", alpha=0.4)
plt.title('overlaid images of "lungs" and "lungs 3"')
plt.show()

fig = plt.figure() # create a new figure as a variable  "fig"
ax = fig.add_subplot(111) # # add some axis; we a 1x1 subplot have
ax.imshow(mean_fixed_image, cmap="Greys_r")  # showing the fixed image (lungs)
floating = ax.imshow(new_floating_image, cmap="Greys_r", alpha=0.4)
shift_rotate_Image([-7, -34],-3)
plt.title('Aligned, overlaid images of "lungs" and "lungs 3"')
plt.show()



###########################################################
#Q17. function to shift the floating image using keyboard presses.
###########################################################
up = 0 
left = 0 
rotations = 0

def eventHandler(event): 
    whichKey = event.key
    global up
    global left
    global rotations
    print(whichKey)
    if whichKey == "up":
        up -= 1 # variable "up" will then get updated --> increased by 1 unit
    elif whichKey =="down":
        up += 1 # variable "up" will then get updated --> decreased by 1 unit
    elif whichKey == "left":
        left -= 1 # variable "left" will then get updated --> move to the left by 1 unit
    elif whichKey == "right":
        left += 1 # variable "left" will then get updated --> move away from the left by 1 unit
    elif whichKey == "a": # key q = clockwise
        rotations -= 1 # variable "rotations" will then get updated 
    elif whichKey == "d": # key s = anticlockwise
        rotations += 1 # variable "rotations" will then get updated 
    shift_rotate_Image([up,left],rotations)
    print (str(left), "unit moved to the left;", str(up), "units moved up;", str(rotations), "degree rotated (clockwise)" )


###########################################################
#Q18. function to shift the floating image using keyboard presses.
###########################################################

#Lungs & Lungs3
fig = plt.figure() 
ax = fig.add_subplot(111) 
ax.imshow(mean_fixed_image, cmap="Greens_r", alpha=0.5)
floating = ax.imshow(new_floating_image, alpha=0.5, cmap="Purples_r")
fig.canvas.mpl_connect('key_press_event', eventHandler) # connects the  “fig” to key presses and call the defined function eventHandler 
plt.title('overlaid images of "lungs" and "lungs 3"')
plt.show()


"""
the above code overlying images lungs1 and lungs3 
by using the key press,
we got a results ([-6,-33],-3) that is pretty much matching compared to the one we found by error and trial; 
by editing the coding, we also got very similar results for lungs1 and lungs2 image as well
"""


