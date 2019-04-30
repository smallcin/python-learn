#coding=utf-8

import threading
from PIL import Image
import random,string ,os,random,getopt,sys

PathName = "imgDir/"

def start():

  image_size = range(40, 550)
  #创建文件夹
  isDirImgDir = os.path.exists(PathName)
  if isDirImgDir == False:
    os.mkdir(PathName)
  
  #随机生成名字
  strSign = ""
  listNameBody = [chr(i) for i in range(65,91)] + [chr(i) for i in range(97,123)]
  #大写字母  + 小写字母  + 数字
  listBody = listNameBody + [str(i) for i in range(1,10)]
  dirPathName = ""
  
  index = 1
  for size in image_size:
    
    nameList = random.sample(listNameBody,7)
    strName = strSign.join(nameList)

    if index%25 == 0:
      nameList = random.sample(listNameBody,7)
      dirStrName = strSign.join(nameList)

      dirPathName = PathName+dirStrName
      isDirImg = os.path.exists(dirPathName)
      if isDirImg == False:
        os.mkdir(dirPathName)

    index += 1  
    t = threading.Thread(target=create_image, args=(size,strName,dirPathName,))
    t.start()



def create_image(size,strName,dirPathName):

  pri_image = Image.open(inputFilePath)
  pri_image.resize((size, size), Image.ANTIALIAS).save(dirPathName+"/jinitem_{}.png".format(strName))

def showLog():
  print("python test.py -i <inputfile>")

 
def main(argv):
  global inputFilePath

  try:
    opts,args = getopt.getopt(argv,"hi:",["help","ifile="])

    if len(opts) <= 0:
      showLog()
      sys.exit(2)
      
  except getopt.GetoptError:
    showLog()
    sys.exit(2)

  for opt,arg in opts:
    if opt == "-h":
      showLog()
      sys.exit()
    elif opt in ("-i","--ifile"):
      inputFilePath = arg
      if len(inputFilePath) <= 0:
        print("image is nil")
        sys.exit()
      #print("inputFilePath",inputFilePath)
      start()
    else:
      print(opt)
  print("Finish!")

if __name__ == "__main__":
  main(sys.argv[1:])
	