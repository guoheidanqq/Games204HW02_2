import time
import scipy
from skimage import io
from skimage import data
from matplotlib import pyplot as plt
import numpy as np
from BayerDomainProcessor import *
from RGBDomainProcessor import *
from scipy import interpolate
from matplotlib import pylab
from skimage import color
from RGBDomainProcessor import *
from YUVDomainProcessor import *
from HDR_fusion import *
import os

## 2022 11 12
image = io.imread('./data/chessboard_lightfield.png')
image = image / 255
HEIGHT = image.shape[0]
WIDTH = image.shape[1]
HEIGHT_sub = np.int32(HEIGHT / 16)
WIDTH_sub = np.int32(WIDTH / 16)

img_sub = np.zeros((HEIGHT_sub, WIDTH_sub, 3))
image_sub_list = np.zeros((16, 16, HEIGHT_sub, WIDTH_sub, 3))

for u in range(0, 16):
    for v in range(0, 16):
        image_sub_list[u, v, :, :, :] = image[u::16, v::16, :]

N = 4
plt.figure()
for i in range(0, N):
    for j in range(0, N):
        plt.subplot(N, N, i * N + j + 1)
        plt.imshow(image_sub_list[i, j, :, :, :])
        plt.axis('off')
plt.show()

image_sub_to_show = np.zeros((HEIGHT, WIDTH, 3))
for u in range(0, 16):
    for v in range(0, 16):
        image_sub_to_show[u * HEIGHT_sub:(u + 1) * HEIGHT_sub, \
        v * WIDTH_sub:(v + 1) * WIDTH_sub, :] = \
            image_sub_list[u, v, :, :, :]
plt.imshow(image_sub_to_show)
plt.show()

plt.figure()
plt.imshow(image)
plt.show()

# import numpy as np
# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D
# from matplotlib import cm
# from scipy.interpolate import interpn
# # Set up grid and array of values
# x1 = np.arange(10)
# x2 = np.arange(10)
# arr = x1 + x2[:, np.newaxis]
# # Set up grid for plotting
# X, Y = np.meshgrid(x1, x2)
# # Plot the values as a surface plot to depict
# fig = plt.figure()
# ax = fig.gca(projection='3d')
# surf = ax.plot_surface(X, Y, arr, rstride=1, cstride=1, cmap=cm.jet,
#                        linewidth=0, alpha=0.8)
# fig.colorbar(surf, shrink=0.5, aspect=5)
#
#
# interp_x = 3.5           # Only one value on the x1-axis
# interp_y = np.arange(10) # A range of values on the x2-axis
# # Note the following two lines that are used to set up the
# # interpolation points as a 10x2 array!
# interp_mesh = np.array(np.meshgrid(interp_x, interp_y))
# interp_points = np.rollaxis(interp_mesh, 0, 3).reshape((10, 2))
# # Perform the interpolation
# interp_arr = interpn((x1, x2), arr, interp_points)
# # Plot the result
# ax.scatter(interp_x * np.ones(interp_y.shape), interp_y, interp_arr, s=20,
#            c='k', depthshade=False)
# plt.xlabel('x1')
# plt.ylabel('x2')
# plt.show()
