import numpy as np
from PIL import Image
from numpy import array
from numpy.linalg import norm
from scipy import ndimage
from skimage.io import imread


img = imread("clock.tiff")
# input = Image.fromarray(img)
# input.show()

# print(img)

r,c = img.shape
mean = 0.3
variace = 0.1
sigma = variace ** 0.5
gaussian = np.random.normal(mean, sigma, (r,c))
gaussian = gaussian.reshape(r,c)
print(gaussian)
final = Image.fromarray(gaussian)
final.show()

gaussian_noise = img + gaussian
gaussian_noise = np.array(gaussian_noise, dtype=np.uint8)
# print(gaussian_noise)
final_image1 = Image.fromarray(gaussian_noise)
final_image1.show()
