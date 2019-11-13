#coding=utf-8

from PIL import Image
# import cv2

def remove_transparency(initial_pic,new_pic, bg_colour=(255, 255, 255)):
    # Only process if image has transparency

    try:
        img_pil = Image.open(initial_pic)
    except IOError:
        return
    if img_pil.mode in ('RGBA', 'LA') or \
        (img_pil.mode == 'P' and 'transparency' in img_pil.info):
        # Need to convert to RGBA if LA format due to a bug in PIL (http://stackoverflow.com/a/1963146)
        alpha = img_pil.convert('RGBA').split()[-1]

        alphas = img_pil.split()
        aa = img_pil.getchannel("A")
        # Create a new background image of our matt color.
        # Must be RGBA because paste requires both images have the same format
        # (http://stackoverflow.com/a/8720632  and  http://stackoverflow.com/a/9459208)
        bg = Image.new("RGBA", img_pil.size, bg_colour + (255,))  #img_pil.size
        bg.paste(img_pil, mask=alpha)

        # width, height = bg.size
        # if width == height:
        #     region = bg
        # else:
        #     if width > height:
        #         delta = (width - height) / 2
        #         box = (delta, 0, delta + height, height)
        #     else:
        #         delta = (height - width) / 2
        #         box = (0, delta, width, delta + width)
        #     region = bg.crop(box)
        bg.resize((512,512), Image.ANTIALIAS)
        # cv2.resize(bg,(512,512), interpolation = cv2.INTER_AREA)
        bg.save(new_pic, "PNG")
        # return bg

    else:
        return img_pil
def add_rgba_image(init_img, new_img):
    try:
        img_ori = Image.open(init_img)
    except IOError:
        return

    img_datas = img_ori.getdata()
    new_data = list()
    for item in img_datas:
        if item[3] != 0:
            new_data.append(item)
        else:
            new_data.append((item[0]+1,item[1],item[2],item[3]))

    img_ori.putdata(new_data)
    img_ori.save(new_img,"PNG")

def trans_PNG(initial_pic, new_pic):
    '''
    to get a transparent picture
    :param initial_pic: initial picture's path
    :param new_pic: the transparent picture's path
    :return:
    '''
    img = Image.open(initial_pic)

    img = img.convert("RGBA")
    x, y = img.size
    # for i in range(x):
    #     for j in range(y):
    #         color = img.getpixel((i, j))
    #         color = color[:-1] + (240,)
    #         img.putpixel((i, j), color)

    datas = img.getdata()
    new_data = list()
    for item in datas:
        if item[3] != 0:
            new_data.append(item)
        else:
            new_data.append((255, 255, 255, 255))
    # for item in datas:
    #     if item[0] > 240 and item[1] > 240 and item[2] > 240:
    #         new_data.append((255, 255, 255, 100))
    #     else:
    #         new_data.append(item)
    img.putdata(new_data)
    img.save(new_pic, "PNG")
if __name__ == "__main__":
    # remove_transparency("pinruiicon.png","pinruiicon1.png")
    add_rgba_image("pinruiicon.png","pinruiicon4.png")
    # trans_PNG("pinruiicon.png","pinruiicon1.png")
