#gausian blur
import cv2
import numpy as np
from PIL import Image
from skimage.io import imread
import  math
img = imread("clock.tiff")
def kernel(k,sig):

  a=np.linspace(-(k-1)/2.,(k-1)/2.,k)
  x,y=np.meshgrid(a,a)
  mask= np.exp( -(np.square(x)+np.square(y))/2*np.square(sig) )/(math.sqrt(2)*math.pi*np.square(sig))
  return mask

mask=kernel(5,1)

im_out=cv2.filter2D(img,-1,mask)
final_image1 = Image.fromarray(im_out)
final_image1.show()
# cv2_imshow(im_out)