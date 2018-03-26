#coding=utf-8

s = "Hello, World!"
print s

#引号可以是单引号，双引号。但是一定要配对

#print打印会去掉字符串的引号
#print打印字符串然后转到下一行，如果不想转到下一行，可以在末尾加一个逗号

print 'Apple: ',
print '$ 1.99 / lb'

#len() 查看字符串的长度
print len(s)

#.upper()   把所有字符串转换为大写
#.lower()   把所有字符串转换为小写
#.capitalize()   把字符串中的首字母大写，并把剩余的字母转换为小写
#.title()        把首字母以及每个空格或者标点符号后面的字母转换为大写，其他字母转换为小写

title = "wind in the willows"

print title.upper()
print title.lower()
print title.capitalize()
print title.title()
#这些方法都不会改变原来的字符串的值！

#isalpha()  一旦字符串包含任何数字或者符号，将返回False
#isdigit()  一旦字符串包含任何字母或者符号，将返回False

state = "VA"
print state.isdigit()

#连接字符串 +

first_name = "Jacob"
last_name = "Fulton"
print first_name + " " + last_name

#乘法 * 将字符串重复n次
s = "Hello"
print 5*s

#字符串乘以一个负数将得到一个空字符串

#比较字符串  python严格区分大小写、空格

#转义字符 多行打印 \t \\ \'
rhyme = "Little Miss Muffett\n\
Sat on a Tuffet\n\
Eating her curds and whey"
print rhyme

#删除空格 strip()  删除开头和结尾的空格
nameTmp = "***Han*nah***"
print nameTmp.strip()
#strip()可以删除开头和结尾指定的其他字符 ，将字符作为参数传递给strip （使用之前确保开头和结尾没有空格）
print nameTmp.strip('*') #开头和结尾不能有空格，不然不生效
print nameTmp.rstrip('*') #删除结尾
print nameTmp.lstrip('*') #删除开头

#查找和替换
#count() 方法返回一个字符串在另一个字符串中出现的次数
long_text = "the the the the wo wo wo "
print long_text.count('the')

#查找字符串在另一个字符串总第一次出现的位置find() 如果没有找到则返回-1
print long_text.find("the")

#替换 replace('a','b')  使用b替换a

#查询关于字符串的操作  shell 中 help(type(""))  按ente下一行  q退出帮助
