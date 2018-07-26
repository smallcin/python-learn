#coding=utf-8

import Tkinter as tk

# root = tk.Tk()

# label = tk.Label(root, text = "hello world",padx = 10, pady = 10)
# label.pack()

# root.mainloop()


#Using Class
#Tkinter.Button的继承关系是->Widget->BaseWidget->...->Mixc，但是Mixc却没有继承自python中的祖宗类object，
#于是乎使用python的内置函数super调用基类方法会出现TypeError。
#2.7如果不加object会报错
class Root(tk.Tk,object):
	"""docstring for ClassName"""
	def __init__(self,arg):
		super(Root,self).__init__()
		self.arg = arg
		print("arg{}".format(arg))
		self.label = tk.Label(self,text = "Hello world", padx = 5,pady = 5)
		self.label.pack()

if __name__ == "__main__":
	root = Root(object)
	root.mainloop()