import matplotlib.pyplot as plt
import matplotlib.image as mpimg

fig = plt.figure()                             # make a figure
ax = fig.add_subplot(2, 2, 1)                  # add the first subplot to the figure
img = mpimg.imread('HarryPotter-Python.jpg')   # you need to download this file to your computer from Files/Labs for Fun
imgplot = plt.imshow(img)                      # make an image plot
ax.set_title('Original')                       # set a title

ax = fig.add_subplot(2, 2, 2)                  # add the second subplot to the figure
lum_img = img[:, :, 0]                         # make a luminosity image (no colors, only brightness)
imgplot = plt.imshow(lum_img)                  
ax.set_title('Luminosity')                     
plt.colorbar()                                 # add a colorbar

ax = fig.add_subplot(2, 2, 3)                  # add the third subplot to the figure
imgplot = plt.imshow(lum_img, cmap="hot")
ax.set_title('Colormap Hot')
plt.colorbar(ticks=[0.1, 0.3, 0.5, 0.7], orientation='horizontal')

ax = fig.add_subplot(2, 2, 4)                  # add the forth subplot to the figure 
plt.hist(lum_img.ravel(), bins=256, range=(0.0, 220.0), fc='k', ec='k') # make a histogram of luminosity values
ax.set_title('Histogram')

plt.show()                                     # make a GUI window to visualize the figure and plots
