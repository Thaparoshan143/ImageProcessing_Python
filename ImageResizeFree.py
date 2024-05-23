import cv2

in_filename = "temp1.png"
out_filename = in_filename.split(".")[0] + "_resized.png"
out_width, out_height = 2560, 1707
interpolation_method = cv2.INTER_CUBIC
BG_CLIP_COLOR = [0,0,0] # if resize diable which color to put in bg 

img = cv2.imread(in_filename)
curr_width, curr_height = img.shape[1], img.shape[0]
border_w = (int((abs(curr_width - out_width)/2)))
border_h = (int((abs(curr_height - out_height)/2)))

img = cv2.copyMakeBorder(img, border_h, border_h, border_w, border_w, cv2.BORDER_CONSTANT, value=BG_CLIP_COLOR)
cv2.imwrite(out_filename, img)