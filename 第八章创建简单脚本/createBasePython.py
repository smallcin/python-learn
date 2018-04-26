#coding=utf-8

# def function_name(parameter1,parameterl2):
# 	pass
# 	pass

def hello():
	print "Hello! How are you?"

hello()

#传递参数
def hello2(name):
	print "Hello, {}".format(name)

hello2('Hannah')

#通过函数调用中使用参数的名称
def print_total(cuetomer_name, items):
	print "Total for {}".format(cuetomer_name)
	total = 0
	for item in items:
		total = item + total
	print "${}".format(total)

print_total(items = [4.52,6.31,5.00],cuetomer_name = "Karen")