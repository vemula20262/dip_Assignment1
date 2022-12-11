
import numpy as np
from PIL import Image
from numpy import array
from numpy.linalg import norm
from scipy import ndimage
from skimage.io import imread


img = imread("clock.tiff")
print(img.shape)
c = 255 / np.log(1 + np.max(img))
log_transformed = c * (np.log(img + 1))
log_transformed = np.array(log_transformed, dtype=np.uint8)
print(log_transformed)
final_image1 = Image.fromarray(log_transformed)
# final_image1.save("log_transformed.tiff")
final_image1.show()

