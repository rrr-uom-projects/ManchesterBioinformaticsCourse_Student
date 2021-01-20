"""
Refer to Assignment.pdf for instructions!

Remember - this is assessed. Make sure your code is nicely structured

Comments are not optional

Authors: Rosie Smart and Ruth Keane
Date: 20/01/2021
Title: Image processing in Python Part 1

"""
import matplotlib.pyplot as plt
import numpy as np

from skimage.io import imread


def main(): 
    # Load data and image
    file_data = load_image("lungs.jpg")
    #In histogram, we do not want to include include black space so we use file_data>1
    histogram(file_data[file_data>1])
    #Look at the lower- mid region - soft tissue
    transform_window(file_data, 20, 50)
    #upper-mid region - shows organs
    transform_window(file_data, 40, 110)
    #high end region - shows bone
    transform_window(file_data, 25, 240)
    # Higher intensity shows bones, middle shows soft tissue,
    # with a difference between muscle and organ. The zero values 
    # show air. 
    
    plt.show()
    plt.close()
    
def load_image(file):
    """
    Loads data from file and draws the image. 

    Parameters
    ----------
    file : string
        file you want to load (include directory path if not in current directory)

    Returns
    -------
    file_data : array
        The data loaded from file. 

    """
    #read in the data from file
    file_data = imread(file)
    #display data as an image
    plt.imshow(file_data)
    return file_data

def histogram(file_data):
    """
    Creates a histogram and draws it. 

    Parameters
    ----------
    file_data : array
        The array of data of which you wish to create a histogram

    Returns
    -------
    None.

    """
    #create figure space we wish to draw to
    plt.figure() 
    #Create histogram. Array must first be flattened. 
    plt.hist(file_data.flatten(), bins=255) 
    #Draw figure
    plt.draw() 
    
def transform_window(file_data, window, level):
    """
    Transforms and displays the image using a peicewise function. 

    Parameters
    ----------
    file_data : array
        Data to be transformed.  
    window : float
        Width of the slope. 
    level : float
        Slope midpoint

    Returns
    -------
    None.

    """
    #Will use y=mx+c, calculate m and c:
    y_max = np.max(file_data)
    m = y_max/window
    c = y_max*((1/2)-(level/window))
    
    #Assign y
    #linear function
    y = m*file_data+c
    #Lower values
    y[file_data < (level - (1/2)*window)] = 0
    #upper values
    y[file_data > (level + (1/2)*window)] = y_max
    
    #Plot the transformed image
    plt.figure()
    plt.imshow(y)
    

if __name__ == "__main__": 
    main()