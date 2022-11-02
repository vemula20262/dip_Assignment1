import numpy as np
from PIL import Image
from numpy import array
from numpy.linalg import norm
from scipy import ndimage
from skimage.io import imread

z = imread("7.1.03.tiff")
print(z.shape)
laplacian = np.array([[1, 1, 1], [1, -9, 1], [1, 1, 1]])
z = z / 511
cnv1 = ndimage.convolve(z, laplacian)
# cnv1 = cnv1 * 512
# z = z * 512
output = z - cnv1
output=output*511
print(output)
final_image1 = Image.fromarray(output)
final_image1.save("enhanced_laplacian.tiff")
final_image1.show()
