#coding=utf-8
from PIL import Image
import random,os, sys, gc, time
bEnviormentOk=True      #环境是否Ok
curToolPath=sys.path[0]

def  checkEnviornment():
    global  bEnviormentOk
    if not bEnviormentOk:
        try:
            from PIL import Image
            global Image
            bEnviormentOk=True
        except:
            pyPath=sys.executable
            pyPath=pyPath[0:pyPath.find("python.exe")]+"Lib\\site-packages"
            os.system("xcopy  /E /Q /S  %s  %s" % (os.path.join(curToolPath,"lib"),pyPath))
            from PIL import Image
            global Image
            bEnviormentOk=True

def add_rgba_image(init_img, new_img):

    try:
        img_ori = Image.open(init_img)
    except IOError:
        gc.collect()
        print("image open Error")
        return

    img_ori.convert("RGBA")
    changeIm = img_ori.load()
    rectWidth = img_ori.size[0]
    rectHeight = img_ori.size[1]
    print("Finish to init_img:{}".format(init_img))
    for x in range(1,rectWidth, 10):
        for y in range(1, rectHeight, 10):
            posBand = changeIm[x, y]
            changeValueR = random.choice([-1, 0, 1]) + posBand[0]
            changeValueG = random.choice([-1, 0, 1]) + posBand[1]
            changeValueB = random.choice([-1, 0, 1]) + posBand[2]
            if changeValueR > 255 or changeValueR < 0 :
                changeValueR = posBand[0]
            if changeValueG > 255 or changeValueG < 0 :
                changeValueG = posBand[1]
            if changeValueB > 255 or changeValueB < 0 :
                changeValueB = posBand[2]
            # 随机改变RGB
            changeIm[x, y] = (changeValueR, changeValueG, changeValueB, posBand[3])

    img_ori.save(new_img,"PNG")
    # print("Finish to new_imgPath:{}".format(new_img))
if __name__ == "__main__":

    init_imgPath = sys.argv[1]
    new_imgPath = sys.argv[2]
    # checkEnviornment()
    if bEnviormentOk == True:
        if init_imgPath != "" and new_imgPath != "" and os.path.isfile(init_imgPath):
            add_rgba_image(init_imgPath, new_imgPath)
        else:
            print("Error init_imgPath {}, new_imgPath{}".format(init_imgPath,new_imgPath))
    else:
        print("Enviornment Error")


