#coding=utf-8

#使用If语句
num = 5
if num > 1 :
	print(num)

#代码块：python中使用空格来表示代码块；只要所有语句都缩进到同一层级，这些语句将被看作是同一个代码块的一部分。

#eg.
name = "doug"
if name == "doug":
	print "Hello, D man"
elif name == "man":
	print "World"
else:
	print "How are you today?"
#使用else是可选的，但是如果加了else则它的下面就一定要放置语句，不然会报错。


#True   False
#如果一个变量包含了除了“空”以外的其他内容，他将被认为是真，否则，它被认为是假。

#False   0、0.0、（）、{}、[]

#使用 try/except避免错误
#首先运行try语句，如果得到错误，则将运行except中的语句
try:
	5/0
	print "Dood to go!"
except Exception, e:
	pass
	print "Please don't do that"
else:
	print "Please else"
finally:
	print "Please finally"

# try:
# 	pass
# except Exception, e:
# 	raise e

#如果不想在except中做任何操作，在其中放一条pass语句
num = 5
if num > 0:
	print "You have money"
elif num == 0 :
	print "You're out"
else:
	print "You seem to be mdebt"

