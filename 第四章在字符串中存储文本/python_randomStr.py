#coding=utf-8

import string
import random
import re

#大写字母  + 小写字母  + 数字
list = [chr(i) for i in range(65,91)] + [chr(i) for i in range(97,123)] + [str(i) for i in range(1,10)]

FH = ('!','@','#','$','%','&','_')  #特殊字符
# for x in list:
# 	print(x)

num = random.sample(list,60) + random.sample(list,60)
str = ''
value = str.join(num)#将取出的十个随机数进行重新合并
print(value)
