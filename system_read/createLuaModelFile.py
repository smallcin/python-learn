#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys, getopt ,os , time , getpass ,string, random
import re, threading

def createOutputFile(ofileName, dirPathName):
	
	'''
	创建.lua文件
	'''
	outfileName = "/%s.lua" % ofileName
	flua = open(dirPathName + outfileName,"wb+")

	localTime =  time.localtime(time.time())
# 	dateString = chr(localTime.tm_mday) + "/" + chr(localTime.tm_mon) + "/" + chr(localTime.tm_year)
	dateString = "%d/%d/%d" % (localTime.tm_mday,localTime.tm_mon,localTime.tm_year)
	yearStr = "%d" % localTime.tm_year
	userName = getpass.getuser()
	ocString = "--\n--  %s.lua\n--\n--\n--  Created by %s on %s.\n--  Copyright © %s年 %s. All rights reserved.\n--" % (ofileName,userName , dateString,yearStr,userName)

	flua.write(ocString)
	flua.close()
	
#读取配置文件
def readTxt(fileName):

	inputFile = open(fileName,"rb")
	inputFileStr = inputFile.read()
	#print("fileName {}".format(inputFileStr))
	inputFile = inputFileStr.replace("=",":")

	dictTmp = eval(inputFile)
	#print("readTxt {}".format(dictTmp))
	#print("readTxt",dictTmp["FileName"],dictTmp["CreateFileNum"])
	return dictTmp["FileName"],dictTmp["CreateFileNum"]

#生成多目录结构
def saveMoreDir(PathName, createFileNum):
	  #创建文件夹
	isDirImgDir = os.path.exists(PathName)
  	if isDirImgDir == False:
  		os.mkdir(PathName)
  
  	#随机生成名字
  	strSign = ""
  	listNameBody = [chr(i) for i in range(97,123)] #[chr(i) for i in range(65,91)] + 
  	#大写字母  + 小写字母  + 数字
  	listBody = listNameBody + [str(i) for i in range(1,10)]
  	dirPathName = PathName
  	outputFileNameStr = ""
  	
  	#print("num {}".format(createFileNum))

  	for x in xrange(1,createFileNum):
  		
  		nameList = random.sample(listNameBody,7)
  		strName = strSign.join(nameList)
  		# print(strName)
  		if (x-1)%5 == 0:
  			nameList = random.sample(listNameBody,7)
  			dirStrName = strSign.join(nameList)
  			dirPathName = PathName + dirStrName
  			print(dirPathName)
  			isDirImg = os.path.exists(dirPathName)
  			if isDirImg == False:
  				os.mkdir(dirPathName)

  		outputFileName = random.sample(listNameBody,7)
  		outputFileNameTmp = outputFileNameStr.join(outputFileName)
  		#print(outputFileNameTmp)
  		t = threading.Thread(target = createOutputFile, args = (outputFileNameTmp, dirPathName))
  		t.start()  


def main(argv):
	
	#读取配置文件
	fileName , createFileNum = readTxt(os.getcwd()+"/jsonConfig_lua.txt")

   	saveMoreDir("luaFile/",createFileNum)
   	print("Finish!")       
          
if __name__ == "__main__":
    main(sys.argv[1:])



