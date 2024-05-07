# combines multiple image into one from given folder

import cv2
import numpy as np
import os
from math import floor

folder = "/res/" # folder containing the images to combine
out_file_name = "temp.png" 
stack_axis = 1 # 0 for vertical, 1 for horizontal
log_enable = True 
should_resize = False #  all image of same dimension ?
BG_CLIP_COLOR = [255, 255, 255] # if resize diable which color to put in bg 
# BG_CLIP_COLOR = [0,0,0] 

file_name_list = list()
image_list = list()
image_width_list = list()
image_height_list = list()

for file_name in os.listdir(os.getcwd() + folder):
    file_name_list.append(os.getcwd() + folder + file_name)
    img = cv2.imread(os.getcwd() + folder + file_name)
    dim = img.shape 
    w, h = dim[1], dim[0]
    if log_enable:
        print("File Name : " + file_name)
        print("Width : " + str(w) + " | Height : " + str(h))
        print("---------------------------------------------")

    image_width_list.append(w)
    image_height_list.append(h)

    image_list.append(img)

min_width = int(max(image_width_list))
min_height = int(max(image_height_list))

if log_enable:
    print("Resizing all image to same dim")
    print("New Dim - Width : " + str(min_width) + " | Height : " + str(min_height))

for ind, img in enumerate(image_list):
    if stack_axis == 0:
        if should_resize:
            image_list[ind] = cv2.resize(img, (min_width, image_height_list[ind]),  interpolation = cv2.INTER_AREA)
        else:
            if image_width_list[ind] - min_width < 0:
                border_width = int(floor(abs(min_width-image_width_list[ind])/2))

                if (int(abs(min_width-image_width_list[ind]))/2).is_integer():
                    image_list[ind] = cv2.copyMakeBorder(image_list[ind], 0, 0, border_width, border_width, cv2.BORDER_CONSTANT, value=BG_CLIP_COLOR) 
                else:
                    image_list[ind] = cv2.copyMakeBorder(image_list[ind], 0, 0, border_width+1, border_width, cv2.BORDER_CONSTANT, value=BG_CLIP_COLOR) 


    elif stack_axis == 1:
        if should_resize:
            image_list[ind] = cv2.resize(img, (image_width_list[ind], min_height), interpolation= cv2.INTER_AREA)
        else:
            if abs(image_height_list[ind] - min_height) > 0:
                border_height = int(floor(abs(min_height-image_height_list[ind])/2))

                if (int(abs(min_height-image_height_list[ind]))/2).is_integer():
                    image_list[ind] = cv2.copyMakeBorder(image_list[ind], border_height, border_height, 0, 0, cv2.BORDER_CONSTANT, value=BG_CLIP_COLOR)
                else:
                    print("Is float scaling " + str(ind))
                    image_list[ind] = cv2.copyMakeBorder(image_list[ind], border_height+1, border_height, 0, 0, cv2.BORDER_CONSTANT, value=BG_CLIP_COLOR)
            

image_list = tuple(image_list)

combined_img = np.concatenate(image_list, axis=stack_axis)

cv2.imwrite(out_file_name, combined_img)
