"""
Refer to Assignment.pdf for instructions!

Remember - this is assessed. Make sure your code is nicely structured

Comments are not optional

Authors: Rosie Smart and Ruth Keane
Date: 21/01/2021
Title: Assignment 2 part 1 
"""
# import required functions
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
    image : array
        Shifted image

    """
    # Shift image using interpolation
    # Shifts are those from function arguments, move image in xy plane
    image = interpolation.shift(image, shift = the_shifts)
    return image

def costFunction(fixed_image, floating_image):
    """
    calculations mean squared error value metric for two images
    Parameters
    fixed image : array
        Fixed image
    floating image : array
        Shifted image    
    Returns
    -------
    image : array
        Shifted image
    ----------
    Returns
    value : float
        Mean squared error calculated between the two image
    -------
    None.

    """
    #find number of pixels in fixed image (numbers of rows multiplied by number of columns)
    number_of_pixels=fixed_image.shape[0]*fixed_image.shape[1]
    #find number of pixels in floating image (numbers of rows multiplied by number of columns)
    number_of_pixels_2=floating_image.shape[0]*floating_image.shape[1]
    #Determines whether images have the same numper of pixels- if not, ends script early with a warning
    if number_of_pixels != number_of_pixels_2:
        print("Please use images with the same number of pixels")
        quit()
    # calculates mean squared error between fixed and floating images. 
    #fixed_image - floating_image gives an array of differences between fixed and floating images.
    #np.sum sums over the whole of the squared differences
    value = (1/number_of_pixels) * np.sum((fixed_image-floating_image)**2)
    return value

def registerImages(shifts,fixed_image,floating_image):
    """
    Shifts floating_image with shift shifts and calculates mean squared error to asses how well the images are registered.
    Parameters
    shifts : list
        shifts floating_image in xy direction by shifts
    fixed_image : array
        image to stay fixed
    floating_image : array
        image to be shifted
    ----------

    Returns
    -------
    cost : float
        mean squared error between fixed image and shifted image
    None.

    """
    #shifts image
    shifted_image = shiftImage(shifts,floating_image)
    #calculates mean squared error
    cost=costFunction(fixed_image,shifted_image)
    return cost

def testing_registration(image1_array,image2_array):
    """
    Tests for image registration using different optimisation parameters
    Parameters
    image1_array : array
        image which will stay fixed
    image2_array : array
        image which will be shifted
    ----------

    Returns
    -------
    cost : float
        mean squared error between fixed image and shifted image
    None.

    """        
    ### brute force algorithm with default parameters
    registering_shift = brute(registerImages, ((-100,100),(-100,100)),args=(image1_array,image2_array),Ns=20)
    #registering shift is [  2.99566717 -25.00354501]
    #shift image by optimal shift 
    shifted_image_array = shiftImage(registering_shift,image2_array)
    #visualise this image on top of fixed image
    fig2 = plt.figure()
    ax1 = fig2.add_subplot(111)
    ax2 = fig2.add_subplot(111)
    ax1.imshow(image1_array,cmap="Greys_r")
    ax2.imshow(shifted_image_array,alpha=0.5,cmap="Greys_r")
    plt.savefig("Registered_image_brute_20.png")    

    ### brute force algorithmwith more points in grid (Ns parameter)
    registering_shift = brute(registerImages, ((-100,100),(-100,100)),args=(image1_array,image2_array),Ns=40)
    #At  a higher number of evaluation point, the registering shift is [  2.99889995 -25.0045823 ].
    # More precise but takes longer
    # shifts image by optimum value
    shifted_image_array=shiftImage(registering_shift,image2_array)
    # fisualises shifts and rotated image
    fig2=plt.figure()
    ax1 = fig2.add_subplot(111)
    ax2 = fig2.add_subplot(111)
    ax1.imshow(image1_array,cmap="Greys_r")
    ax2.imshow(shifted_image_array,alpha=0.5,cmap="Greys_r")
    plt.savefig("Registered_image_brute_40.png")    

    ### brute force algorithm with reduced shift limits
    registering_shift= brute(registerImages, ((-5,5),(-5,5)),args=(image1_array,image2_array),Ns=20)
    #registering shift is [  3.00046965 -24.99650448]
    #smaller range takes less time but less likely to include the true answer
    #shifts image to this optimal shift
    shifted_image_array=shiftImage(registering_shift,image2_array)
    #visualise fixed and shifted image
    fig2=plt.figure()
    ax1 = fig2.add_subplot(111)
    ax2 = fig2.add_subplot(111)
    ax1.imshow(image1_array,cmap="Greys_r")
    ax2.imshow(shifted_image_array,alpha=0.5,cmap="Greys_r")
    plt.savefig("Registered_image_brute_small_range.png")  

    ### differential evolution algorithm
    registering_shift= differential_evolution(registerImages, ((-100,100),(-100,100)),args=(image1_array,image2_array))
    #registering shift is [  3.00558153 -24.99568951], but does take longer to run that brute 
    #shifts image to this optimum
    shifted_image_array=shiftImage(registering_shift.x,image2_array)
    #visualises fixed and rotates at this optimum
    fig2=plt.figure()
    ax1 = fig2.add_subplot(111)
    ax2 = fig2.add_subplot(111)
    ax1.imshow(image1_array,cmap="Greys_r")
    ax2.imshow(shifted_image_array,alpha=0.5,cmap="Greys_r")
    plt.savefig("Registered_image_differential_evolution.png")    
 

def main():
    """Main script where functions are called"""
    ### import dicom files using pydicom package
    image1_dcm = pydicom.read_file("IMG-0004-00001.dcm",)
    # access the pixels from the dicom object
    image1_array=image1_dcm.pixel_array
    image2_dcm = pydicom.read_file("IMG-0004-00002.dcm")
    image2_array=image2_dcm.pixel_array
    image3_dcm = pydicom.read_file("IMG-0004-00003.dcm",)
    image3_array=image3_dcm.pixel_array
    image4_dcm = pydicom.read_file("IMG-0004-00004.dcm")
    image4_array=image4_dcm.pixel_array


    ### At this point, testing_registration can be called to produce registered images made from different algorithm parameters.
    # This is an optional stage and the images have already been saved as png files
    #testing_registration(image1_array,image2_array)


    ### Plot image 2 and image 1 on one plot (second image is translucent)
    fig=plt.figure()
    ax1 = fig.add_subplot(111)
    ax2 = fig.add_subplot(111)
    ax1.imshow(image1_array,cmap="Greys_r")
    ax2.imshow(image2_array,alpha=0.5,cmap="Greys_r")
    plt.savefig("Unregistered_image.png")    


    ### This section registers images 2, 3 and 4 to image 1
    #Make a list of different images which will be registered
    floating_list = [image2_array, image3_array, image4_array]
    #Make an empty array to store optimal registrations
    registrations = []
    # Loops through images to be registered    
    for floating in floating_list:
        #finds optimal shift for each of the images
        # use .x to access the values from the differential_evolution output
        registering_shift= differential_evolution(registerImages, ((-200,200),(-200,200)),args=(image1_array,floating)).x
        #store shift in registrations
        registrations.append(registering_shift)
    
    # Loop through images to be registered, applying optimal shift and plotting registered image on top of original image. Saves this figure.
    index=0
    for floating in floating_list:
        #accesses the optimal shift for each image (in registrations) using index. Shifts the image by this value.
        shifted_image_array=shiftImage(registrations[index],floating)
        #Makes plot
        fig=plt.figure()
        ax1 = fig.add_subplot(111)
        ax2 = fig.add_subplot(111)
        ax1.imshow(image1_array,cmap="Greys_r")
        ax2.imshow(shifted_image_array,alpha=0.5,cmap="Greys_r")
        #index is used to set the name of the figure (images are 2-4)
        plt.savefig(str(index+2)+"registered_images.png")  
        #increase index
        index=index+1
    #Convert optimal registrations into an array
    registrations_array = np.array(registrations)
    #Save array into a numpy file
    np.save("registrations_array.npy",registrations_array)  

if __name__ == "__main__": 
    main()