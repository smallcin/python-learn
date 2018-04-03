#coding=utf-8

# python创建一个列表，进行添加、删除项、修改项

#创建一个列表
fruit = ['apple','strawberry','pear','papaya']
print fruit

#创建一个空列表
toppings = []
print toppings

#列表中的编号  从0开始到任意数
#列表中每一项叫做它的索引

#获取指定索引的项
print "列表第二项{}".format(fruit[1]) #如果我们请求的索引为-1，则会返回最后一项

#可以使用变量来创建一个列表，但保存在列表中的，只是变量中的内容的一个副本。如果我们要修改最初的变量的值，列表的值不会改变
fruit1 = 'apple'
fruit2 = 'pear'
fruit_list = [fruit1,fruit2,fruit1]
print fruit_list
fruit1 = 'grapea'
print fruit_list
print fruit1

#获取列表有多少项
print len(fruit_list)

#统计列表中某哥项的总数目 count()
print fruit_list.count('apple')

#找到一个项在列表中的位置 index() 将返回这个项在列表中第一次出现的索引位置
print fruit_list.index('apple')#如果该项不存在则返回一个错误

#使用in 判断该项是否在列表中
print 'apple' in fruit_list

#在表末尾添加一项，可使用append()方法
toppings.append('pepperoni')
toppings.append('mushrooms')
print toppings

#将一个列表中的项添加到另一个列表的后面extend()
order1 = ['pizza','fries','baklave']
oeder2 = ['soda','lasagna']
order1.extend(oeder2)
print order1

#删除找到的第一个项  remove()  有多个相同的项，只会删除第一个
order1.remove('pizza')

#在列表中指定位置添加一项 insert()
# e.g insert(1,"orange")

#如果不想改变任何一个列表，将两个列表加起来，使用+,返回带所有项的一个列表
#一个列表乘以一个数字，会得到旧列表重复多次的  *

#排序列表  
#反转列表中的项 reverse()   names.reverse()
#按照字母排序或者数字升序排序  names.sort()

#比较列表  ==   !=




