# Import the bit of matplotlib that can draw rectangles
import matplotlib.patches as patches

# Create a new figure
fig2 = plt.figure(2)
ax = fig2.add_subplot(111)# Stick a subplot into the figure
thePlot = ax.imshow(lungs_1, cmap="Greys_r") # Display the fixed image (your image name may be different)

# Start with a box drawn in the centre of the image
origin = (lungs_1.shape[0]/2, lungs_1.shape[1]/2)
rectParams = [origin[0], origin[1], 10, 10]

# Draw a rectangle in the image

global rect
rect = patches.Rectangle((rectParams[1], rectParams[0]),rectParams[2], rectParams[3],linewidth=1, edgecolor='r',facecolor='none')

ax.add_patch(rect)

# Event handlers for the clipbox
global initPos
initPos = None



def onPress(event):
    """
    This function is called when you press a mouse button inside the figure window
    """
    global rect
    if event.inaxes == None:
        return# Ignore clicks outside the axes
    contains, attr = rect.contains(event)
    if not contains:
        return# Ignore clicks outside the rectangle

    global initPos # Grab the global variable to update it
    initPos = [rect.get_x(), rect.get_y(), event.xdata, event.ydata]

def onMove(event):
    """
    This function is called when you move the mouse inside the figure window
    """
    global initPos
    global rect
    if initPos is None:
        return# If you haven't clicked recently, we ignore the event

    if event.inaxes == None:
        return# ignore movement outside the axes

    x = initPos[2]
    y = initPos[3]
    dx = event.xdata - initPos[2]
    dy = event.ydata - initPos[3]
                                    # This code does the actual move of the rectangle
    rect.set_x(initPos[0] + dx)
    rect.set_y(initPos[1] + dy)

    rect.figure.canvas.draw()

def onRelease(event):
    """
    This function is called whenever a mouse button is released inside the figure window
    """
    global initPos
    initPos = None # Reset the position ready for next click

def keyboardInterface(event):
    """
    This function handles the keyboard interface. It is used to change the size of the
    rectangle.
    """
    global rect
    if event.key == "right":
        # Make the rectangle wider
        w0 = rect.get_width()
        rect.set_width(w0 + 1)
    elif event.key == "left":
        # Make the rectangle narrower
        w0 = rect.get_width()
        rect.set_width(w0 - 1)
    elif event.key == "up":
        # Make the rectangle shorter
        h0 = rect.get_height()
        rect.set_height(h0 - 1)
    elif event.key == "down":
        # Make the rectangle taller
        h0 = rect.get_height()
        rect.set_height(h0 + 1)
################################################################################
# The functions below here will need to be changed for use on Windows!
    elif event.key == "ctrl+right":
        # Make the rectangle wider - faster
        w0 = rect.get_width()
        rect.set_width(w0 + 10)
    elif event.key == "ctrl+left":
        # Make the rectangle narrower - faster
        w0 = rect.get_width()
        rect.set_width(w0 - 10)
    elif event.key == "ctrl+up":
        # Make the rectangle shorter - faster
        h0 = rect.get_height()
        rect.set_height(h0 - 10)
    elif event.key == "ctrl+down":
        # Make the rectangle taller - faster
        h0 = rect.get_height()
        rect.set_height(h0 + 10)

    rect.figure.canvas.draw()# update the plot window

cid1 = fig2.canvas.mpl_connect('button_press_event', onPress)
cid2 = fig2.canvas.mpl_connect('motion_notify_event', onMove)
cid3 = fig2.canvas.mpl_connect('button_release_event', onRelease)
cid4 = fig2.canvas.mpl_connect('key_press_event', keyboardInterface)

plt.show()



indices = [int(rect.get_y()), int(rect.get_y() + rect.get_height()), int(rect.get_x()), int(rect.get_x() + rect.get_width())]
print(indices)