import numpy as np
import os
import cv2

def compress_image_in_iteration(infilename, outfilename, inter_method, comp_factor, iter_count, should_write_all):
    img = cv2.imread(infilename)
    curr_width, curr_height = img.shape[1], img.shape[0]
    print(curr_width*comp_factor, curr_height*comp_factor)

    if iter_count == 0 or comp_factor == 1:
        img = cv2.resize(img, (int(curr_width * comp_factor), int(curr_height * comp_factor)), interpolation=inter_method)
    else:
        for i in range(0, iter_count):
            new_width = int(curr_width * (1-((1-comp_factor)*(i+1)/iter_count)))
            new_height = int(curr_height * (1-((1-comp_factor)*(i+1)/iter_count)))
            if log_enable:
                print("Current Iteration : " + str(i+1))
                print(new_width, new_height)
                print("----------------------------------------")
            img = cv2.resize(img, (new_width, new_height), interpolation=inter_method)
            
            if should_write_all:
                fileName = (infilename.split(".")[0] + "_iter" + str(i+1) + ".png")
                img = cv2.resize(img, (curr_width, curr_height), interpolation=inter_method) # if any resolution is ok comment this line
                cv2.imwrite(fileName, img)

    img = cv2.resize(img, (curr_width, curr_height), interpolation=inter_method)
    cv2.imwrite(outfilename, img)
    return True

in_filename = "temp.png"
out_filename = in_filename.split(".")[0] + "_comp.png"
compression_factor = 0.95 # compression factor i.e how much to compress compared to original image 0.9 means 10% compression
iteration_count = 3 # how many iteration before final result of compression
interpolation_method = cv2.INTER_CUBIC
write_all_iteration = False # True if want all the iteration compressed images
is_folder = True # will overwrite other and write repective image with _comp at end in new folder
folder_path = "renders" # will be irrelevent if is only one file and is_folder is false
contains_subfolder = False # true if the folder path is the root and contains sub directory that contains the main images to compress
log_enable = False
ignore_file_list = ['.DS_Store'] # will ignore this file and folders
accept_file_extensions = ['png'] # will only accept file with this listed extension

if is_folder:
    out_folder_path = os.getcwd() + "/" + folder_path + "_compressed"
    if contains_subfolder:
        sub_dir_list = [item for item in os.listdir(folder_path) if item not in ignore_file_list]
        if log_enable:
            print(sub_dir_list)

        for dir in sub_dir_list:
            dir_path = out_folder_path + "/" + dir
            os.makedirs(dir_path, exist_ok=True)
            file_list = [item for item in os.listdir(folder_path + "/" + dir) if item not in ignore_file_list and item.split(".")[-1] in accept_file_extensions]
            if log_enable:
                print(file_list)

            for file in file_list:
                infilename = os.getcwd() + "/" + folder_path + "/" + dir + "/" + file
                outfilename = dir_path + "/" + file
                if log_enable:
                    print(outfilename)
                compress_image_in_iteration(infilename, outfilename, interpolation_method, compression_factor, iteration_count, write_all_iteration)
    else:
        dir_path = out_folder_path
        file_list = [item for item in os.listdir(folder_path) if item not in ignore_file_list and item.split(".")[-1] in accept_file_extensions]
        os.makedirs(dir_path, exist_ok=True)
        
        for file in file_list:
            infilename = os.getcwd() + "/" + folder_path + "/" + file
            outfilename = dir_path + "/" + file
            if log_enable:
                print(infilename)
                print(outfilename)
            compress_image_in_iteration(infilename, outfilename, interpolation_method, compression_factor, iteration_count, write_all_iteration)
else:
    compress_image_in_iteration(in_filename, out_filename, interpolation_method, compression_factor, iteration_count, write_all_iteration)

