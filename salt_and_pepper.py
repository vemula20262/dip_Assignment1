import numpy as np
from PIL import Image
from numpy import array
from numpy.linalg import norm
from scipy import ndimage
from skimage.io import imread


img = imread("clock.tiff")
l,m = img.shape
p = 0.25
s = 1 - p
img =img/511
output = np.zeros((l, m))
for i in range(l):
    for j in range(m):
        random_number = np.random.random()
        if random_number < p:
            output[i, j] = 0
        elif random_number > s:
            output[i, j] = 1
        else:
            output[i, j] = img[i, j]
output = output * 511
output = Image.fromarray(output)
output.show()
