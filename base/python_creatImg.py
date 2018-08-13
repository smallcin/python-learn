#coding=utf-8

import threading
from PIL import Image
import random,string 

image_size = range(30, 230)
 
def start():
  
  for size in image_size:
    t = threading.Thread(target=create_image, args=(size,))
    t.start()


 
 
def create_image(size):
  strSign = ""
  listNameBody = [chr(i) for i in range(65,91)] + [chr(i) for i in range(97,123)]
	#大写字母  + 小写字母  + 数字
  listBody = listNameBody + [str(i) for i in range(1,10)]

  nameList = random.sample(listNameBody,7)
  strName = strSign.join(nameList)

  pri_image = Image.open("login_xjsz.png")
  pri_image.resize((size, size), Image.ANTIALIAS).save("img/jinengitem_{}.png".format(strName))
 
 
if __name__ == "__main__":
	start()