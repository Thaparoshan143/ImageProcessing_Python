import cv2

in_filename = "temp.png"
out_filename = in_filename.split(".")[0] + "_resized.png"
scale_factor = 0.90 # uniform precentage to scale less than 1 means downscaling and greater than 1 means upscaling
interpolation_method = cv2.INTER_CUBIC

img = cv2.imread(in_filename)
curr_width, curr_height = img.shape[1], img.shape[0]
print(curr_height*scale_factor, curr_width*scale_factor)
img = cv2.resize(img, (int(curr_width * scale_factor), int(curr_height * scale_factor)), interpolation=interpolation_method)

cv2.imwrite(out_filename, img)