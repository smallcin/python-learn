#coding=utf-8

#收集信息  input()
#收集任何非数字的信息  raw_input()

# >>> number = input()
# 55
# >>> number
# 55
# >>>

#input()不能接受没有引号的字符串，不然会会报错。保存输入的原始数据eg. 1 ,3 ,"Hello"

#raw_input() 把用户输入的任何内容都保存为一个字符串。
# >>> str = raw_input()
# shfkdjh
# >>> str
# 'shfkdjh'
# >>>

#输入前给我提示：raw_input("Please give me your name!")

name = raw_input("Please give your name:")
print name

#将字符串转为数字  float()
#将字符串、浮点数转为整数  int()

weight = 170.5
print int(weight)

#获取密码
from getpass import getpass #从getpass库导入getpass函数
password = getpass() #可以加提示
print password

#使用format()  输出
greeting = "Good {},{}, How are you doing?"
name = "Hannah"
time = "morning"
print greeting.format(time,name)

#可以通过键值决定放的位置
greetingTmp = "Good {time},{name}, How are you doing?"
name = "Hannah"
time = "morning"
print greetingTmp.format(name = name,time = time)

#可以通过下标 下标从0开始
# greetingTmp = "Good {0},{1}, How are you doing?"
# name = "Hannah"
# time = "morning"
# print greetingTmp.format(name,time)  #传递参数少会报错，多会舍弃

#练习
# breakfast_special = "Texas Omelet"
# breakfast_notes = "Contains brisket, horseradish cheddar"
# lunch_special = "Greek patty melt"
# lunch_notes = "Like the regular one, but with tzatziki sauce"
# dinner_special = "Buffalo steak "
# dinner_notes = "Top loin with not sauce and blue cheese,NOT BUFFALO MEAT."
# meal_time = raw_input("Which mealtime do you want? [breakfast,lunch,dinner] ")
# meal_time = meal_time.strip()
# print "meal_time:{}".format(meal_time)
# meal_time = meal_time.lower()
# print "Specials for {}".format(meal_time)
# if meal_time == "breakfast":
# 	print breakfast_special
# 	print breakfast_notes
# elif meal_time == "lunch":
# 	print lunch_special
# 	print lunch_notes
# elif meal_time == "dinner":
# 	print dinner_special
# 	print dinner_notes
# else:
# 	print "Sorry, {} isn\'t valid.".format(meal_time)


Good_Name = raw_input("Give me your name,please:")
Good_Widget = raw_input("How many widgets are you buying?[#]")
Good_Cost = raw_input("How much do they cost,per item?[#.##]")

tocal = int(Good_Widget)*float(Good_Cost)
print "Your tocal is ${}".format(tocal)
print "Thanks for shopping with us today,{name}!".format(name = Good_Name)











