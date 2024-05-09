import numpy as np
import cv2

in_filename = "temp.png"
out_filename = in_filename.split(".")[0] + "_comp.png"
compression_factor = 0.50 # compression factor i.e how much to compress compared to original image 0.9 means 10% compression
iteration_count = 4 # how many iteration before final result of compression
interpolation_method = cv2.INTER_CUBIC
write_all_iteration = True # True if want all the iteration compressed images

img = cv2.imread(in_filename)
curr_width, curr_height = img.shape[1], img.shape[0]
print(curr_width*compression_factor, curr_height*compression_factor)

if iteration_count == 0:
    img = cv2.resize(img, (int(curr_width * compression_factor), int(curr_height * compression_factor)), interpolation=interpolation_method)
else:
    for i in range(0, iteration_count):
        new_width = int(curr_width * (1-((1-compression_factor)*(i+1)/iteration_count)))
        new_height = int(curr_height * (1-((1-compression_factor)*(i+1)/iteration_count)))
        print("Current Iteration : " + str(i+1))
        print(new_width, new_height)
        print("----------------------------------------")
        img = cv2.resize(img, (new_width, new_height), interpolation=interpolation_method)
        
        if write_all_iteration:
            fileName = (in_filename.split(".")[0] + "_iter" + str(i+1) + ".png")
            img = cv2.resize(img, (curr_width, curr_height), interpolation=interpolation_method) # if any resolution is ok comment this line
            cv2.imwrite(fileName, img)


img = cv2.resize(img, (curr_width, curr_height), interpolation=interpolation_method)
cv2.imwrite(out_filename, img)
