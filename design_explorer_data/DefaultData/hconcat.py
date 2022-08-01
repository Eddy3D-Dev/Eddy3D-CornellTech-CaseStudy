import cv2 as cv
import os
import glob
import numpy as np

import pathlib

cwd = pathlib.Path.cwd()

#input folders
img_folder = cwd

def getImageName(file_path):
    base = os.path.basename(file_path)
    return os.path.splitext(base)[0]


def stack_images(img_list, how, fill_color):
    max_height, max_width = 0, 0
    padding = 0  # 200 
    total_height, total_width = padding, padding 
    mult_by = 0 if fill_color == 'black' else 255

    for image in img_list:

        img_height, img_width = image.shape[0], image.shape[1]  

        if img_height > max_height:
            max_height = img_height
        total_width += img_width

        if img_width > max_width:
            max_width = img_width
        total_height += img_height

    final_image = None

    if how == 'ver':

        # create a new array with a size large enough to contain all the images with white pixels
        final_image = np.ones((total_height, max_width, 3), dtype=np.uint8)*mult_by

        curr_y = 0  # keep track of where your current image was last placed in the y coordinate
        for curr_image in img_list:

            img_height, img_width  = curr_image.shape[0], curr_image.shape[1]
            curr_height = curr_y + img_height
            calc_width =  max_width - img_width

            # add an image to the final array and increment the y coordinate
            curr_image = np.hstack((curr_image, np.ones((img_height, calc_width , 3))*mult_by))  # with white pixels
            # place current image
            final_image[curr_y:  curr_height, :, :] = curr_image
            curr_y += img_height

    elif how == 'hor':

        # create a new array with a size large enough to contain all the images with white pixels
        final_image = np.ones((max_height,total_width,  3), dtype=np.uint8)*mult_by

        curr_x = 0  # keep track of where your current image was last placed in the x coordinate
        for curr_image in img_list:

            img_height, img_width  = curr_image.shape[0], curr_image.shape[1]
            curr_width = curr_x + img_width
            calc_height =  max_height - img_height

            # add an image to the final array and increment the y coordinate
            curr_image = np.vstack((curr_image, np.ones((calc_height, img_width,  3))*mult_by))  # with white pixels
            # place current image

            final_image[:, curr_x:  curr_width,:] = curr_image          

            curr_x += img_width

    return final_image


#get all jpg files in source folder A
files = glob.glob(str(img_folder) + "\*ScreenParallel.png")

for i, f in enumerate(files):

    image_path_left = files[i]
    image_path_right = image_path_left.replace("ScreenParallel", "ScreenTop")
    image_name_export = image_path_left.split('\\')[-1].split('.')[0].split('ScreenParallel')[0] +".png"
    image_name_right =  image_path_right.split('\\')[-1]
    image_name_left =  image_path_left.split('\\')[-1]

    print("Exporting image {0} with name {1} and {2}".format(image_name_export, image_name_left, image_name_right))
    cv.imwrite(image_name_export,stack_images([cv.imread(image_path_left),cv.imread(image_path_right)], 'hor', 'white'))