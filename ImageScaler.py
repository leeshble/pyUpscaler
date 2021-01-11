import os
from PIL import Image

input_path = './Example/input'
output_path = './Example/output'
user_select = ''
pixel_buff = ()
working_img = []
result_img = ''

def upscale_pre(user_select):
    """
    Preprocessing before upscale image which user selected.
    """
    global result_img
    global pixel_buff
    print('=======================================')
    print('Starting upscale...')
    input_img_x, input_img_y = working_img.size
    working_img_mode = working_img.mode
    output_img = Image.new(working_img_mode, (input_img_x*2, input_img_y*2))
    outputx, outputy = output_img.size
    print(f'outputx set:{outputx} outputy set:{outputy}')
    if working_img_mode == "RBGA":
        pixel_buff = (0, 0, 0, 0)
    else:
        pixel_buff = (0, 0, 0)
    print('Making space...')
    #Inserting input image pixel and black pixel
    ix = iy = 0
    for oy in range(0, outputy, 2):
        for ox in range(0, outputx):
            if ox % 2 != 1:
                output_img.putpixel((ox, oy), working_img.getpixel((ix,iy)))
                ix += 1
            else:
                output_img.putpixel((ox, oy), pixel_buff)
            if ix == input_img_x:
                ix = 0
            #print(f'pixel:{ix, iy} input:{working_img.getpixel((ix,iy))} / pixel:{ox, oy} output:{output_img.getpixel((ox,oy))}')
        iy += 1
    #Inserting Black line
    ix = iy = 0
    for oy in range(1, outputy, 2):
        for ox in range(0, outputx):
            output_img.putpixel((ox, oy), pixel_buff)
            #print(f'pixel:{ix, iy} input:{working_img.getpixel((ix,iy))} / pixel:{ox, oy} output:{output_img.getpixel((ox,oy))}')
    return output_img

def upscale_main_side(output_img):
    """
    Fixing black pixel using side pixel of itself.
    """
    #Fixing pixel which y % 2 != 1
    outputx, outputy = output_img.size
    for oy in range(0, outputy-1, 2):
        for ox in range(1, outputx, 2):
            pixel1 = output_img.getpixel((ox-1, oy))
            p1 = pixel1[0]
            p2 = pixel1[1]
            p3 = pixel1[2]
            if ox == outputx-1 :
                output_img.putpixel((ox, oy), (p1, p2, p3))
            else:
                pixel2 = output_img.getpixel((ox+1, oy))
                P1 = pixel2[0]
                P2 = pixel2[1]
                P3 = pixel2[2]
                output_img.putpixel((ox, oy), (int((p1+P1)/2), int((p2+P2)/2), int((p3+P3)/2)))
            #print(f'pixel:{ox, oy} output:{output_img.getpixel((ox,oy))}')
    #Fixing pixel which y % 2 == 1
    for oy in range(1, outputy-1, 2):
        for ox in range(0, outputx):
            pixel1 = output_img.getpixel((ox, oy-1))
            p1 = pixel1[0]
            p2 = pixel1[1]
            p3 = pixel1[2]
            if oy == outputx:
                output_img.putpixel((ox, oy), (p1, p2, p3))
                break
            else:
                pixel2 = output_img.getpixel((ox, oy+1))
                P1 = pixel2[0]
                P2 = pixel2[1]
                P3 = pixel2[2]
                output_img.putpixel((ox, oy), (int((p1+P1)/2), int((p2+P2)/2), int((p3+P3)/2)))
            #print(f'pixel:{ox, oy} output:{output_img.getpixel((ox,oy))}')
    #Save image 
    result_img = output_path+'/output.'+working_img.format.lower()
    output_img.save(result_img)
    print('Upscale finished..!')
    output_img.show()

def image_info(path):
    """
    Show image info in terminal.
    """
    global working_img
    working_img = Image.open(path)
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
    upscale_main_side(upscale_pre(user_select))
    image_info(result_img)