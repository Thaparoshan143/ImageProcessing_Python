
# This script is to isolate the white background i.e RGB image clipping Alpha to RGBA image

import cv2
import numpy as np

tolpercentage = 0.90
tolval = 255*tolpercentage
tolLimit = 80
image_name = 'temp.png'

def shouldClipAlpha(pixel):
    return sum(pixel[0:3]) > tolval and (abs(pixel[0] - 255) < tolLimit and abs(pixel[1] - 255) < tolLimit and abs(pixel[2] - 255) < tolLimit)

# Load image
im = cv2.imread(image_name)
print(im.shape)
im4 = cv2.cvtColor(im, cv2.COLOR_BGR2BGRA)

for i, row in enumerate(im4): 
    for j, pixel in enumerate(row): 
        if shouldClipAlpha(pixel):
            im4[i][j][-1] = 0

cv2.imwrite(image_name.split(".")[0]+"_mask.png", im4)
