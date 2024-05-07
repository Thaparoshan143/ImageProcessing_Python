# script to invert the color value of image 

import cv2
import numpy as np

in_filename = "temp.png"
out_filename = "temp2.png"

MAX = 255

def getInvert(p):
    return [MAX-val for val in p]


img = cv2.imread(in_filename)
dim = img.shape
width, height = dim[0], dim[1]

print(width)
print(height)

img = np.dot(img[...,:3], [0.2989, 0.5870, 0.1140])
cv2.imwrite(out_filename, img)
