#!/usr/bin/python
# -*- coding: UTF-8 -*-

#这个python 脚本 用来生成 oc 的模型文件  传入 文件名  以及 对应的 包含 模型字典的文件  就会生成 oc 的 .h 和 .m文件

#首先 需要接受 命令行中传进来的 文件  （存放的是 模型对应的json数组）


import sys, getopt ,os , time , getpass ,string, random
import re



def openInputFile(fileName,ofileName) :
	
	"在这个类里面 处理 传进来的文件内容然后转化成字典并且  写入到  新的文件中去 （文件路径就是当前终端打开的路径）"
	# fo = open(fileName,"rb")
	
	# string =  fo.read()
	# print "输入的文件中的 字符串 ：", string
	
	# string = string.replace("=",":")
	# print string
	# dic = eval(string)
	# print dic
	# print(dic['num'])
	# list =  dic.keys()
	# print list

	# fo.close()
	
	'''
	创建.h文件
	'''
	outfileName = "%s.h" % ofileName
	foc = open(outfileName,"wb+")
	
# 	foc.write("//create by wangshen\n")
# 	foc.write
# 	foc.write("shuxing")

	localTime =  time.localtime(time.time())
# 	dateString = chr(localTime.tm_mday) + "/" + chr(localTime.tm_mon) + "/" + chr(localTime.tm_year)
	dateString = "%d/%d/%d" % (localTime.tm_mday,localTime.tm_mon,localTime.tm_year)
	yearStr = "%d" % localTime.tm_year
	userName = getpass.getuser()
	ocString = "//\n//  %s.h\n//\n//\n//  Created by %s on %s.\n//  Copyright © %s年 %s. All rights reserved.\n//" % (ofileName,userName , dateString,yearStr,userName)
	ocString = ocString + "\n\n\n#import <Foundation/Foundation.h>"
	ocString = ocString + "\n\n@interface %s : NSObject\n\n" % ofileName
	
	#apString = "\n@property (nonatomic,copy) NSString *"
	apString = "\n+(void)load;"
	# for pname in list :
	# 	ocString = ocString + apString + pname + "\n"
	ocString = ocString + apString	
	ocString = ocString + "\n\n@end"
# 	ocString = ocString + ""
	
	foc.write(ocString)
	foc.close()
	
	'''
	创建.m文件
	'''
	listNameBody = [chr(i) for i in range(65,91)] + [chr(i) for i in range(97,123)]
	#大写字母  + 小写字母  + 数字
	listBody = listNameBody + [str(i) for i in range(1,10)]
	
	#FH = ('!','@','#','$','%','&','_')  #特殊字符
	# for x in listBody:
	# 	print(x)

	# var num = random.sample(list,60) + random.sample(list,60)
	# str = ''
	# value = str.join(num)#将取出的十个随机数进行重新合并

	outfileName = ofileName + ".m"
	fom = open(outfileName,"wb+")
	ocmString = "//\n//  %s.m\n//\n//\n//  Created by %s on %s.\n//  Copyright © %s年 %s. All rights reserved.\n//" % (ofileName,userName,dateString,yearStr,userName)
	ocmString = ocmString + "\n#import \"%s.h\"" % ofileName
	ocmString = ocmString + "\n\n\n@implementation %s" % ofileName
	ocmString = ocmString + "\n+(void)load{"
	for i in xrange(1,400):
		strSign = ""

		strBodyList = random.sample(listBody,60) + random.sample(listBody,60)
		strBody = strSign.join(strBodyList)#将取出的十个随机数进行重新合并  strSign 链接符

		nameList = random.sample(listNameBody,9)
		strName = strSign.join(nameList)

		#print(strName,strBody)
		ocmString = ocmString + "\nNSString *" + strName + "=@\"" + strBody + "\";\n"
		ocmString = ocmString + strName + " = [" + strName + " stringByAppendingString:" + strName + "];\n"

	ocmString = ocmString + "\n}"
	ocmString = ocmString + "\n\n\n\n\n\n\n\n@end"

	fom.write(ocmString)
	fom.close()
	
	
def createRandomCode(outputfilenameList):
	#创建,h文件
	ofileName = "randCode"
	outfileName = "%s.h" % ofileName
	foc = open(outfileName,"wb+")
	
	localTime =  time.localtime(time.time())
# 	dateString = chr(localTime.tm_mday) + "/" + chr(localTime.tm_mon) + "/" + chr(localTime.tm_year)
	dateString = "%d/%d/%d" % (localTime.tm_mday,localTime.tm_mon,localTime.tm_year)
	yearStr = "%d" % localTime.tm_year
	userName = getpass.getuser()
	ocString = "//\n//  %s.h\n//\n//\n//  Created by %s on %s.\n//  Copyright © %s年 %s. All rights reserved.\n//" % (ofileName,userName , dateString,yearStr,userName)
	ocString = ocString + "\n\n\n#import <Foundation/Foundation.h>"
	ocString = ocString + "\n\n@interface %s : NSObject\n\n" % ofileName
	apString = "\n+(void)platform;"
	ocString = ocString + apString	
	ocString = ocString + "\n\n@end"
	
	foc.write(ocString)
	foc.close()

	outfileName = ofileName + ".m"
	fom = open(outfileName,"wb+")
	ocmString = "//\n//  %s.m\n//\n//\n//  Created by %s on %s.\n//  Copyright © %s年 %s. All rights reserved.\n//" % (ofileName,userName,dateString,yearStr,userName)
	ocmString = ocmString + "\n#import \"%s.h\"" % ofileName

	for x in outputfilenameList:
		ocmString = ocmString + "\n#include \"" + x + ".h\""

	ocmString = ocmString + "\n\n\n@implementation %s" % ofileName
	ocmString = ocmString + "\n+(void)platform{\n"
	for x in outputfilenameList:
		ocmString = ocmString + "\n[" + x + " load];"

	ocmString = ocmString + "\n}"
	ocmString = ocmString + "\n\n\n\n\n\n\n\n@end"

	fom.write(ocmString)
	fom.close()

def main(argv):
   inputfile = ''
   isDir = os.path.exists("rFile")
   if isDir == False:
   	os.mkdir("rFile")

   os.chdir("rFile")
   outputfilenameList = []
   outputfileList = [chr(i) for i in range(65,91)] + [chr(i) for i in range(97,123)]
   for x in range(1,41):
	   outputfilename = random.sample(outputfileList,8)
	   outputfilesign = ""
	   outputfilename = outputfilesign.join(outputfilename)
	   outputfilenameList.append(outputfilename)
	   openInputFile(inputfile,outputfilename)
   
   createRandomCode(outputfilenameList)     
   print("Finish!")       
          

if __name__ == "__main__":
    main(sys.argv[1:])



