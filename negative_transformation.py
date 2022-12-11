import numpy as np
from PIL import Image
from numpy import array
from numpy.linalg import norm
from scipy import ndimage
from skimage.io import imread


img = imread("clock.tiff")
input_image = Image.fromarray(img)
input_image.show()
print(img.shape)
neg_transformed = np.max(img) - img
print(neg_transformed)
final_image1 = Image.fromarray(neg_transformed)

final_image1.show()
