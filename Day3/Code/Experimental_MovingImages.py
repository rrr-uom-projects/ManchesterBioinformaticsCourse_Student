

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import os 
import inspect
from skimage import io
from PIL import Image as PIL

class WindowSelect(object):

    def __init__(self, artists):
        self.artists = artists
        #self.colors = [a.get_facecolor() for a in self.artists]
        # assume all artists are in the same figure, otherwise selection is meaningless
        self.fig = self.artists[0].figure
        self.ax = self.artists[0].axes

        self.fig.canvas.mpl_connect('button_press_event', self.on_press)
        self.fig.canvas.mpl_connect('button_release_event', self.on_release)
        self.fig.canvas.mpl_connect('motion_notify_event', self.on_motion)

        self.currently_selecting = False
        self.currently_dragging = False
        self.selected_artists = []
        self.offset = np.zeros((1,2))
        self.rect = plt.Rectangle((0,0),1,1, linestyle="--",
                                  edgecolor="crimson", fill=False)
        self.ax.add_patch(self.rect)
        self.rect.set_visible(False)

    def on_press(self, event):
        # is the press over some artist
        isonartist = False
        for artist in self.artists:
            if artist.contains(event)[0]:
                isonartist = artist
        self.x0 = event.xdata
        self.y0 = event.ydata
        if isonartist:
            # add clicked artist to selection
            self.select_artist(isonartist)
            # start dragging
            self.currently_dragging = True
            ac = np.array([a.center for a in self.selected_artists])
            ec = np.array([event.xdata, event.ydata])
            self.offset = ac - ec
        else:
            #start selecting
            self.currently_selecting = True
            self.deseclect_artists()

    def on_release(self, event):
        if self.currently_selecting:

            for artist in self.artists:
                if self.is_inside_rect(*artist.center):
                    self.select_artist(artist)
            self.fig.canvas.draw_idle()
            self.currently_selecting = False
            self.rect.set_visible(False)

        elif self.currently_dragging:
            self.currently_dragging = False


    def on_motion(self, event):
        if self.currently_dragging:
            newcenters = np.array([event.xdata, event.ydata])+self.offset
            for i, artist in enumerate(self.selected_artists):
                artist.center = newcenters[i]
            self.fig.canvas.draw_idle()
        elif self.currently_selecting:
            self.x1 = event.xdata
            self.y1 = event.ydata
            #add rectangle for selection here
            self.selector_on()
            self.fig.canvas.draw_idle()

    def is_inside_rect(self, x, y):
        xlim = np.sort([self.x0, self.x1])
        ylim = np.sort([self.y0, self.y1])
        if (xlim[0]<=x) and (x<xlim[1]) and (ylim[0]<=y) and (y<ylim[1]):
            return True
        else:
            return False

    def select_artist(self, artist):
        artist.set_color('k')
        if artist not in self.selected_artists:
            self.selected_artists.append(artist)

    def deseclect_artists(self):
        for artist,color in zip(self.artists, self.colors):
            artist.set_color(color)
        self.selected_artists = []

    def selector_on(self):
        self.rect.set_visible(True)
        xlim = np.sort([self.x0, self.x1])
        ylim = np.sort([self.y0, self.y1])
        self.rect.set_xy((xlim[0],ylim[0] ) )
        self.rect.set_width(np.diff(xlim))
        self.rect.set_height(np.diff(ylim))


def demo():
    # path of the executing script 
    actual_path = os.path.dirname(os.path.abspath(inspect.stack()[0][1]))

    """
    X. Load the images “lings.jpg” and “lungs2.jpg”
    """

    #name of image
    img_name1 = '/lungs.jpg'
    img_name2 = '/lungs2.jpg'
    img_name3 = '/lungs3.jpg'
    #path to the image
    img_path1 = actual_path + img_name1
    img_path2 = actual_path + img_name2
    img_path3 = actual_path + img_name3
    #import images using imread as a grey scale of values between 0 and 1
    lungs1 = io.imread(img_path1, as_gray=True)
    lungs2 = io.imread(img_path2, as_gray=True)
    lungs3 = io.imread(img_path3, as_gray=True)

    fig, ax = plt.subplots(1,1)
    xlim = [-1000, 1000]
    ylim = [-1000, 1000]
    ax.set(xlim=xlim, ylim=ylim)

    images = [lungs1, lungs2, lungs3]
    
    PIL_img = []
    for i in range(0, len(images), 1):
        PIL_img.append(PIL.fromarray(images[i])) # covert array images to PIL image format
        

    for image in images:
        ax.imshow(image, alpha=0.25, cmap="Greys_r")

    w = WindowSelect(PIL_img)
    plt.show()

if __name__ == '__main__':
    demo()