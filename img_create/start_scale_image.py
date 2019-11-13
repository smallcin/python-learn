#coding=utf-8
from PIL import Image

def start_scale_image(img_path, image_size):

    try:
        img_ori = Image.open(img_path)
    except IOError:
        return



if __name__ == "__main__":
    start_scale_image("",(20,20))