"""
Write a function that displays the CT image with different lindow levels. The input variables
should be the window and the level.
"""
# Let's load the image lung again but this time, we are going to convert color images to gray-scale 
# We can do this with as_gray=True
part1 = io.imread("/Users/monkiky/Desktop/ManchesterBioinformaticsCourse_Student/Day3/Code/lungs.jpg", as_gray=True)

# Now let's see the window and levels values using:
print(np.min(part1), np.max(part1))


plt.imshow(part1,cmap="Greys_r", vmin=0.0, vmax=0.4)

def displayImageWinLevel(image, window, level):
    plt.imshow(image,cmap="Greys_r", vmin=window, vmax=level)
    plt.show()
#Min value for window and level is 0 and maximum is 1
displayImageWinLevel(image=part1, window=0.2, level=1)



