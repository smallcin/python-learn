#coding=utf-8

#for循环
# for x in xrange(1,10):
# 	pass

print "获取数字范围： {}".format(range(7))
#获取数字范围： [0, 1, 2, 3, 4, 5, 6]  返回从0开始的数

#不想从0开始，则传入两个数range(2,7,2) 第三个为步长

for x in xrange(1,10):
	print x

for year in xrange(1980,2019):
	print "In the {}".format(year)

print year
# continue #跳出本次循环

# break #完全停止循环

#循环注意： for循环创建的变量（year）在for循环完成后并不会消失，
#它将包含for循环中所用到的最后一个值

age = raw_input("Please give me your age in years (eg.30):")
while not age.isdigit():
	print "I'm sorry,but {} isn't valid.".format(age)
	age = raw_input("Please give me your age in years (eg.30):")
print "Thanks! Youe age is set to {}".format(age)

#无限循环，直到输入q
while True:
	text = raw_input("Please Enter 'q' exit:")
	if text == "q":
		break