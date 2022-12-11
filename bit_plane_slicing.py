import numpy as np
from PIL import Image
from numpy import array
from numpy.linalg import norm
from scipy import ndimage
from skimage.io import imread


img = imread("clock.tiff")
lst = []
print(img.shape)

for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        lst.append(np.binary_repr(img[i][j], width=8))
eight_bit = []
seven_bit = []
six_bit = []
five_bit = []
four_bit = []
three_bit = []
two_bit = []
one_bit = []

for i in lst:
    eight_bit.append(int(i[0])*128)
    seven_bit.append(int(i[1])*64)
    six_bit.append(int(i[2])*32)
    five_bit.append(int(i[3])*16)
    four_bit.append(int(i[4])*8)
    three_bit.append(int(i[5])*4)
    two_bit.append(int(i[6])*2)
    one_bit.append(int(i[7])*1)

# print(eight_bit)

eight_bit = np.array(eight_bit)
eight_bit = eight_bit.reshape(img.shape[0], img.shape[1])
# print(eight_bit)
final_image1 = Image.fromarray(eight_bit)
final_image1.show()


#eight_bit_img = (np.array([int(i[0]) for i in lst],dtype = np.uint8) * 128).reshape(img.shape[0],img.shape[1])

