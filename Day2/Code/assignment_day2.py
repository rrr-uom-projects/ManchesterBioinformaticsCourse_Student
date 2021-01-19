"""
Refer to Practical2_instructions.pdf for a guide

Remember - comments are not optional
"""
print("Hello World")

#Change working directory
os.chdir("C:/Users/jaden/bioinformatics-course/code/ManchesterBioinformaticsCourse_Student/Day2/Code/breathing_data")
os.getcwd()
#importing required packages and modules
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sgnl
import skimage
import os
import io

#Use numpy.loadtxt to load the first csv file.
file = open("p01.csv")
data = np.loadtxt(file, delimited=",")
x,y = np.loadtxt(file, delimiter=",")
x
y
data
#print(data)

#Check the documentation for this function to figure out how to load a csv.
help(np.loadtxt)

#What is the shape of the resulting array?
np.shape(data) 
#What does the shape mean?
#(2, 1107) meaning there are two dimensions and each dimension has 1107 elements

#Try plotting the data using a few different options (e.g. plot, scatter). What
#does each axis in the array refer to? x axis refers to person?; y refers to breathing value?
import matplotlib.pyplot as plt
plt.plot(data)
plt.show()

##Practice code for mapping data values from a CSV file to x and y, respectively
 #with open('p01.csv','r') as csvfile:
    #x = []
    #y = []
    #plots = np.loadtxt(csvfile, delimiter=',')
    #for row in plots:
        #x.append(int(row[0]))
        #y.append(int(row[1]))

#Creating a plot for p01.csv data
plt.plot(x,y, label='Loaded from file!')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graph\nCheck it out')
plt.legend()
plt.show()

#Creating scatterplot for p01.csv data:
plt.scatter(data)
plt.show()





