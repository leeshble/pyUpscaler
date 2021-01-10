import os
import numpy as np
from PIL import Image

input_path = './Example/input'
output_path = './Example/output'
user_select = ''
working_img = []

def upscale_pre(user_select):
    """
    Preprocessing before upscale image which user selected.
    """
    print('=======================================')
    print('Starting upscale...')
    input_img_x, input_img_y = working_img.size
    working_img_mode = working_img.mode
    working_img_format = working_img.format
    output_img = Image.new(working_img_mode, (input_img_x*2, input_img_y*2))
    outputx, outputy = output_img.size
    print(f'outputx set:{outputx} outputy set:{outputy}')
    pixel_buff = ()
    """
    rbga = "RGBA"
    if rbga == working_img_mode:
        working_img.convert('RBGA')
        pixel_buff = (0, 0, 0, 0)
    else:
        working_img.convert('RGB')
        pixel_buff = (0, 0, 0)
    """
    pixel_buff = (0, 0, 0)
    print('Making space...')
    buffx = buffy= True
    ix = iy = 0
    for oy in range(0, outputy):
        if buffy == False:
            for ox in range(0, outputx):
                if buffx == False:
                    output_img.putpixel((ox, oy), working_img.getpixel((ix,iy)))
                    ix += 1
                else:
                    output_img.putpixel((ox, oy), pixel_buff)
                buffx = not buffx
                if ix == input_img_x:
                    ix = 0
                print(f'pixel:{ix, iy} input:{working_img.getpixel((ix,iy))} / pixel:{ox, oy} output:{output_img.getpixel((ox,oy))}')
        else:
            for ox in range(0, outputx):
                output_img.putpixel((ox, oy), pixel_buff)
                print(f'pixel:{ix, iy} input:{working_img.getpixel((ix,iy))} / pixel:{ox, oy} output:{output_img.getpixel((ox,oy))}')
            iy += 1
            if iy == input_img_y:
                iy = 0
        buffy = not buffy
    output_img.save(output_path+'/output.'+working_img_format.lower())
    print('Upscale finished..!')
    output_img.show()

def image_info(path):
    """
    Show image info in terminal.
    """
    global working_img
    working_img = Image.open(user_select)
    print('=======================================')
    print(f'이미지 파일 이름:{working_img.filename}')
    print(f'이미지 파일 파일 형식:{working_img.format}')
    print(f'이미지 용량:{working_img.size}')
    print(f'이미지 색상모드:{working_img.mode}')
    print(f'이미지 크기:{working_img.width}x{working_img.height}')

def image_list(path):
    """
    List image in your input directory.
    """
    global user_select
    user_list = os.listdir(path)
    print('=======================================')
    print('Listing files...')
    for i, v in enumerate(user_list):
        print(i, v)
    print('=======================================')
    user_select = input_path+'/'+user_list[int(input('Select images which you what to scale: '))]
    print("Selected: ", user_select)
    
def test():
    """
    docstring
    """
    input_img = Image.open('./Example/input/example.png')
    output_img = Image.new('RGB', (10, 10))
    input_img.show()
    output_img.show()
    print(f'input:{input_img.getpixel((1, 1))} output:{output_img.getpixel((1,1))}')
    
if __name__ == "__main__":
    image_list(input_path)
    image_info(user_select)
    upscale_pre(user_select)
    #test()