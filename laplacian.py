import numpy as np
from PIL import Image
from numpy import array
from numpy.linalg import norm
from scipy import ndimage
from skimage.io import imread

z = imread("7.1.03.tiff")
print(z.shape)
laplacian = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])
z = z / 511
cnv1 = ndimage.convolve(z, laplacian)
# cnv1 = cnv1 * 511
# z = z * 511
output = z - cnv1
output=output*511
print(output)
final_image1 = Image.fromarray(output)
final_image1.save("laplacian.tiff")
final_image1.show()
