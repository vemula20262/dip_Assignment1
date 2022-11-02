import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from numpy import array
from numpy.linalg import norm
from scipy import ndimage
from skimage.io import imread

z = imread("7.1.03.tiff")
robert_x = np.array([[1, 0 ],[0,-1 ]])
robert_y = np.array([[ 0, 1 ],[-1,0]])
z = z/511
cnv1 = ndimage.convolve(z,robert_x)
cnv2 = ndimage.convolve(z,robert_y)

output = np.sqrt( np.square(cnv1) + np.square(cnv2))
output = output*511
print(output)
plt.figure(figsize=(6,6))
plt.imshow(output,cmap="gray")
plt.axis("off")


plt.show()
# final_image1 = Image.fromarray(output)
# final_image1.save("robert.tiff")
# final_image1.show()
