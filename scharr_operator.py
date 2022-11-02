import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from numpy import array
from numpy.linalg import norm
from scipy import ndimage
from skimage.io import imread

z = imread("7.1.03.tiff")
scharr_x = np.array([[3,0,-3 ],[10,0,-10],[3,0,-3]])
scharr_y = np.array([[3,10,3],[0,0,0],[-3,-10,-3]])
z = z/511
cnv1 = ndimage.convolve(z,scharr_x)
cnv2 = ndimage.convolve(z,scharr_y)

output = np.sqrt( np.square(cnv1) + np.square(cnv2))
output = output*511
print(output)
final_image1 = Image.fromarray(output)
final_image1.show()

