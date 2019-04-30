#coding=utf-8

import os,random,sys

pathName = "resetTile\\"
count = 1

#os.path.join(os.getcwd(),'data')就是获取当前目录，并组合成新目录
def resetName():
	
	strSign = ""
	listBody = [chr(i) for i in range(65,91)] + [chr(i) for i in range(97,123)]
	nameList = random.sample(listBody,7)
	fileName = strSign.join(nameList)
	filePath = pathName + fileName

	isDir = os.path.exists(filePath) 
	if isDir == False:
		os.mkdir(filePath)

	checkListDir(pathName,filePath,fileName)

def checkListDir(pathName,filePath,fileName):
	global count

	for file in os.listdir(pathName):

		#os.chdir(sys.path[0])#设置当前目录
		#获取文件所在路径 os.path.abspath(pathName+file)
		#获取文件所在文件夹路径 os.path.dirname(os.path.abspath(pathName+file))

		#print("sdf",os.getcwd())
		#print("dfds",os.path.dirname(os.path.abspath(pathName+file)),os.path.abspath(pathName+file),file)
		if os.path.isfile(os.path.abspath(pathName+file)):
			print("{} is file ++++++++++:".format(os.path.abspath(pathName+file)))
			os.rename(os.path.join(pathName,file),os.path.join(filePath,fileName+str(count)))

		elif os.path.exists(os.path.abspath(pathName+file)) == True:
			print("{} is dir ==========:".format(os.path.abspath(pathName+file)))
			checkListDir(os.path.abspath(pathName+file),filePath,fileName)
			#resetName()
			isDir = os.path.exists(pathName+fileName) 
			if isDir == False:
				os.mkdir(pathName+fileName)
		else:
			print("final -------------")
			#os.system(exit())
		#print("resetName:{},file:{},filePath:{},count:{},{}".format(path,file,os.getcwd()+"\\"+path+file
			#,os.access(os.getcwd()+"\\"+path+file,os.F_OK),os.path.isfile(os.getcwd()+"\\"+path+file)))
		# if os.access(os.path.abspath(file),os.F_OK) == True:
		# 	print("resetName:{},file:{},count:{}".format(pathName,file,count))
		# 	os.rename(os.path.join(pathName,file),os.path.join(fileName,str(count)+".png"))
		
		count += 1
		

if __name__ == "__main__":
	resetName()