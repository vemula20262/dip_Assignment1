import numpy as np
from PIL import Image
from numpy import array
from numpy.linalg import norm
from scipy import ndimage
from skimage.io import imread


img = imread("clock.tiff")
img1 = imread("clock.tiff")
r,c = img.shape
range_1 =10
range_2 = 60

for i in range(r):
    for j in range(c):
        if img[i,j] >= range_1 and img[i,j] <= range_2:
            img1[i,j] = 255
        else:
            img1[i,j] = 0
# for the intensity slicing the in other process just dont write the else part

output = Image.fromarray(img1)
output.show()
