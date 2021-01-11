import os
import cv2
import numpy as np

input_path = './Example/input'
output_path = './Example/output'
selected_img = ''
#input_img = ()
result_img = ()

def image_list(path):
    """
    List image in your input directory.
    """
    global selected_img
    user_list = os.listdir(path)
    print('=======================================')
    print('Listing files...')
    for i, v in enumerate(user_list):
        print(i, v)
    print('=======================================')
    selected_img = input_path+'/'+user_list[int(input('Select images which you what to scale: '))]
    print("Selected: ", selected_img)

def upscale_pre():
    """
    Preprocessing before upscale image which user selected.
    """
    input_img = cv2.imread(selected_img, cv2.IMREAD_ANYCOLOR)
    iy, ix = input_img.shape