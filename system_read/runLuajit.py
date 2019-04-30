#coding=utf-8

import sys, getopt ,os , time , getpass ,string, random
import re

dirPath = "rFile"

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


def addTimeWithFile(fileList):

	files = os.listdir(fileList)
	for fi in files:
		fi_d = os.path.join(fi)
		# print("fi_d",fi_d)
		#os.path.isdir(需要绝对路径) #检查是否为文件夹
		if os.path.isdir( os.path.join(fileList,fi_d) ):
			# os.mkdir(os.path.join(fileList,fi_d),0777)
			addTimeWithFile(os.path.join(fileList,fi_d))
		else:
			filePath = os.path.join(fileList,fi_d)
			print("write-------{}".format(os.path.join(fileList,fi_d)))
			sysStr = "luajit-win32 -b {} out/{}".format(filePath, filePath)
			os.system(sysStr)
			# readFile = open(filePath,"wb+") #wb 写入
			# fileStr = readFile.read()
			# # print(fileStr)
			# fileStr = fileStr + "\n --abc"
			# readFile.write(fileStr)
			# readFile.close() /AppDelegate.cpp:52:

		

def main(argv):

	#读取配置文件
	#fileName , createFileNum = readTxt(os.getcwd()+"/jsonConfig.txt")
	
	isDir = os.path.exists(dirPath)
	if isDir == False:
		os.mkdir(dirPath)

	os.chdir(dirPath)
  
   	# fileList = os.listdir(os.path.abspath(os.getcwd())) 
   	# print("fileList",fileList)
   	addTimeWithFile(os.path.abspath(os.getcwd()))

   	print("Finish!")   
   	    
          

if __name__ == "__main__":
    main(sys.argv[1:])



