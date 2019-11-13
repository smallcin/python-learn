#coding=utf-8

from PIL import Image
import random,os, sys, gc, time

def add_rgba_image(init_img, new_img):
    global dataIndex
    try:
        img_ori = Image.open(init_img)
    except IOError:
        gc.collect()
        # filePath = "G:\MyWorkSpace\python-learn\img_create\\res_cn"
        # start_change(filePath)
        return

    # img_datas = img_ori.getdata()
    # new_data = list()
    img_ori.convert("RGBA")
    # dataIndex = 0
    # for item in img_datas:
    #     dataIndex = dataIndex + 1
    #     if item[3] != 0:
    #         new_data.append(item)
    #     else:
    #         new_data.append((item[0]+1,item[1],item[2],item[3]))
    # for dataTmp in list(img_datas):
    #     a = dataTmp
    #     dataIndex = dataIndex + 1
    #     print("dataIndex:{}".format(dataIndex))

    changeIm = img_ori.load()
    # rectX = img_ori.size[0] / 3
    # rectY = img_ori.size[1] / 3
    rectWidth = img_ori.size[0]
    rectHeight = img_ori.size[1]
    # for x in range(rectX,rectX + rectWidth):
    #     for y in range(rectY, rectY + rectHeight):
    #         # posBand = img_ori.getpixel((x, y))
    #         posBand = changeIm[x, y]
    #         # changeIm[x, y] = (posBand[0]+100,posBand[1],posBand[2],posBand[3])
    #         changeIm[x, y] = (posBand[0], posBand[1], posBand[2], 0)

    for x in range(1,rectWidth, 10):
        for y in range(1, rectHeight, 10):
            posBand = changeIm[x, y]
            changeValueR = random.choice([-1, 0, 1])
            changeValueG = random.choice([-1, 0, 1])
            changeValueB = random.choice([-1, 0, 1])
            changeIm[x, y] = (posBand[0] + changeValueR, posBand[1] + changeValueG, posBand[2] + changeValueB, 0)

    # posBand = img_ori.getpixel((100,100)) #slow
    # posBand = changeIm[100, 100]
    # print("dataIndex:{}".format(dataIndex))
    # img_ori.putdata(new_data)
    dataIndex = dataIndex + 1
    img_ori.save(new_img,"PNG")
    print("加载第{}个资源".format(dataIndex))
    img_ori.close()
    del changeIm
    del img_ori
    del rectWidth
    del rectHeight
    # print ("sdfga{}".format(gc.isenabled()))
    gc.collect()
    time.sleep(2)




def check_dir(dirPath):

    if os.path.exists(dirPath) == False:
        print ("create dir {}".format(dirPath))
        os.makedirs(dirPath)

def start_change(fileList):
    files = os.listdir(fileList)
    for fi in files:
        fi_d = os.path.join(fi)
        # print("fi_d",fi_d)
        # os.path.isdir(需要绝对路径) #检查是否为文件夹
        if os.path.isdir(os.path.join(fileList, fi_d)):
            # os.mkdir(os.path.join(fileList,fi_d),0777)
            start_change(os.path.join(fileList, fi_d))
            del fi_d
            gc.collect()
        else:
            filePath = os.path.join(fileList, fi_d)
            # print("change-------{}".format(os.path.join(fileList, fi_d)))
            abspath = filePath  # os.getcwd()  # 获取当前路径
            rootpath = os.path.abspath('.')  # 获取上级路径
            # print(abspath)
            # print(rootpath)
            ret = abspath.replace(rootpath, '', 1)
            # print(ret)
            # print('此路径是否为文件夹：%s' % os.path.isdir('../' + ret))
            # new_image_path = "dirPng/pinruiicon{}.png".format(index)
            # chPath = os.chdir(fileList)
            # fileTab = filePath.split('/')[-1]
            # 图片名
            # image_name = filePath.split('/')[-1].split('.')[-2]
            # 图片的类型
            image_type = filePath.split('/')[-1].split('.')[-1]
            if image_type == "png":

                # if os.path.exists(rootpath+"\dirpng1") == False:
                #     os.mkdir(rootpath+"\dirpng1")
                print("start Image {}".format(filePath))
                new_imgPath = rootpath + "\dirpng1" + ret
                print("finish Image {}".format(new_imgPath))
                # if os.isdir(rootpath + "\dirpng1" + ret):
                # lcoalImgPathTab = new_imgPath.split('\\')[-2]
                # for pathItem in lcoalImgPathTab:
                #     print ("dsdfdsf")
                #     check_dir(new_imgPath)
                    # if check_dir(new_imgPath) == True:
                    #     pass
                        # lcoalImgPath = new_imgPath.split('\\')[-2]
                        # lcoalDirPath = new_imgPath.split(lcoalImgPath)[-2]
                        # check_dir(lcoalDirPath + "\\" + lcoalImgPath)
                        # print ("lcoalImgPath {}".format(lcoalDirPath + "\\" + lcoalImgPath))

                # check_dir(new_imgPath)
                lcoalImgPath = new_imgPath.split('\\')[-2]
                lcoalDirPath = new_imgPath.split("\\"+lcoalImgPath + "\\")[-2]
                check_dir(lcoalDirPath + "\\" + lcoalImgPath)
                # print ("lcoalImgPath {}".format(lcoalDirPath + "\\" + lcoalImgPath))
                add_rgba_image(filePath, new_imgPath)
                del new_imgPath
                del lcoalImgPath
                del lcoalDirPath

            del filePath
            del abspath
            del rootpath
            del ret
            del image_type
            gc.collect()

    # for index in range(1,2):
    #     new_image_path = "dirPng/pinruiicon{}.png".format(index)
    #     if os.path.exists("dirPng") == False:
    #         os.mkdir("dirPng")
    #     print("start Image {}".format(new_image_path))
    #     add_rgba_image("pinruiicon.png", new_image_path)


if __name__ == "__main__":
    print('==========start===========')
    filePath = "G:\MyWorkSpace\python-learn\img_create\\res_cn"
    dataIndex = 0
    start_change(filePath)
    print('==========finish===========')

