#coding=utf-8

from Tkinter import *

class Root(Frame):
	#"""docstring for Root"""
	def __init__(self, master = None):
		Frame.__init__(self,master)
		self.pack()
		self.label = Label(self,text = "Hello world",padx = 15,pady = 15)
		self.label.pack()

if __name__ == "__main__":
	print "__name__:{}".format(__name__)
	root = Root()
	root.mainloop()

		