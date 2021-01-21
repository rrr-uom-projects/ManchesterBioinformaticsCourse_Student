"""
Refer to Assignment.pdf for instructions!

Remember - this is assessed. Make sure your code is nicely structured

Comments are not optional

Authors: Rosie Smart and Ruth Keane
Date: 21/01/2021
Title: Assignment 2 part 1 
"""

import matplotlib.pyplot as plt
import numpy as np
import skimage.io 
from skimage.io import imread
from scipy.ndimage import rotate
from scipy.ndimage import interpolation 
from scipy.optimize import brute
from scipy.optimize import differential_evolution
import pydicom 

def shiftImage(the_shifts,image): 
    """
    Shifts image in the xy plane. 

    Parameters
    ----------
    the_shifts : list
        Desired shifts in xy plane
    image : array
        Image to be shifted
    Returns
    -------
    None.

    """
    # Shift image using interpolation
    # Shifts are those from function arguments, move image in xy plane
    image = interpolation.shift(image, shift = the_shifts)
    return image

def costFunction(fixed_image, floating_image):
    """

    Parameters
    ----------
 
    Returns
    -------
    None.

    """
    #find number of pixels
    
    number_of_pixels=fixed_image.shape[0]*fixed_image.shape[1]
    number_of_pixels_2=floating_image.shape[0]*floating_image.shape[1]
    if number_of_pixels != number_of_pixels_2:
        print("Please use images with the same number of pixels")
        quit()
    value = (1/number_of_pixels) * np.sum((fixed_image-floating_image)**2)
    return value

def registerImages(shifts,fixed_image,floating_image):
    """

    Parameters
    ----------

    Returns
    -------
    None.

    """
    shifted_image = shiftImage(shifts,floating_image)
    cost=costFunction(fixed_image,shifted_image)
    return cost


def main():
    image1_dcm = pydicom.read_file("IMG-0004-00001.dcm",)
    image1_array=image1_dcm.pixel_array
    image2_dcm = pydicom.read_file("IMG-0004-00002.dcm")
    image2_array=image2_dcm.pixel_array
    image3_dcm = pydicom.read_file("IMG-0004-00003.dcm",)
    image3_array=image3_dcm.pixel_array
    image4_dcm = pydicom.read_file("IMG-0004-00004.dcm")
    image4_array=image4_dcm.pixel_array
 
    fig=plt.figure()
    ax1 = fig.add_subplot(111)
    ax2 = fig.add_subplot(111)
    ax1.imshow(image1_array,cmap="Greys_r")
    ax2.imshow(image2_array,alpha=0.5,cmap="Greys_r")
    plt.savefig("Unregistered_image.png")    
    
    registering_shift= brute(registerImages, ((-100,100),(-100,100)),args=(image1_array,image2_array),Ns=20)
    #registering shift is [  2.99566717 -25.00354501]
    shifted_image_array=shiftImage(registering_shift,image2_array)
    fig2=plt.figure()
    ax1 = fig2.add_subplot(111)
    ax2 = fig2.add_subplot(111)
    ax1.imshow(image1_array,cmap="Greys_r")
    ax2.imshow(shifted_image_array,alpha=0.5,cmap="Greys_r")
    plt.savefig("Registered_image_brute_20.png")    
    registering_shift= brute(registerImages, ((-100,100),(-100,100)),args=(image1_array,image2_array),Ns=40)
    #At  a higher number of evaluation point, the registering shift is [  2.99889995 -25.0045823 ]. Very similar result. Takes a while.
    # More precise but takes longer
    shifted_image_array=shiftImage(registering_shift,image2_array)
    fig2=plt.figure()
    ax1 = fig2.add_subplot(111)
    ax2 = fig2.add_subplot(111)
    ax1.imshow(image1_array,cmap="Greys_r")
    ax2.imshow(shifted_image_array,alpha=0.5,cmap="Greys_r")
    plt.savefig("Registered_image_brute_40.png")    

    registering_shift= brute(registerImages, ((-5,5),(-5,5)),args=(image1_array,image2_array),Ns=20)
    #registering shift is [  3.00046965 -24.99650448]
    #smaller range may take less time but less likely to include the true answer
    shifted_image_array=shiftImage(registering_shift,image2_array)
    fig2=plt.figure()
    ax1 = fig2.add_subplot(111)
    ax2 = fig2.add_subplot(111)
    ax1.imshow(image1_array,cmap="Greys_r")
    ax2.imshow(shifted_image_array,alpha=0.5,cmap="Greys_r")
    plt.savefig("Registered_image_brute_small_range.png")  

    registering_shift= differential_evolution(registerImages, ((-100,100),(-100,100)),args=(image1_array,image2_array))
    #registering shift is [  3.00558153 -24.99568951], but does take longer to run that brute 
    print(registering_shift.x)
    shifted_image_array=shiftImage(registering_shift.x,image2_array)
    fig2=plt.figure()
    ax1 = fig2.add_subplot(111)
    ax2 = fig2.add_subplot(111)
    ax1.imshow(image1_array,cmap="Greys_r")
    ax2.imshow(shifted_image_array,alpha=0.5,cmap="Greys_r")
    plt.savefig("Registered_image_differential_evolution.png")    


    floating_list = [image2_array, image3_array, image4_array]

    registrations = []
    for floating in floating_list:
        registering_shift= brute(registerImages, ((-100,100),(-100,100)),args=(image1_array,floating),Ns=20)
        registrations.append(registering_shift)
    index=0
    for floating in floating_list:
        shifted_image_array=shiftImage(registrations[index],floating)
        fig=plt.figure()
        ax1 = fig.add_subplot(111)
        ax2 = fig.add_subplot(111)
        ax1.imshow(image1_array,cmap="Greys_r")
        ax2.imshow(shifted_image_array,alpha=0.5,cmap="Greys_r")
        index=index+1
        plt.savefig(str(index+1)+"registered_images.png")  

    registrations_array = np.array(registrations)
    np.save("registrations_array.npy",registrations_array)  

if __name__ == "__main__": 
    main()