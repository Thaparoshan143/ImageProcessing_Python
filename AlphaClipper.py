# This script is to isolate the white background i.e RGB image clipping Alpha to RGBA image

import cv2
import numpy as np

tolpercentage = 0.75
image_name = 'temp.png'

# Load image
im = cv2.imread(image_name)
im4 = cv2.cvtColor(im, cv2.COLOR_BGR2BGRA)
print(im4.shape)
img = np.array(im4)
img[:,:, -1] = np.where((img[:,:,0]>(255*tolpercentage)) & (img[:,:,1]>(255*tolpercentage))  & (img[:,:,2]>(255*tolpercentage)) , 0, img[:,:, -1])
print(img)
im4 = img
cv2.imwrite(image_name.split(".")[0]+"_mask.png", im4)