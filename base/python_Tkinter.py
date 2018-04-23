#coding=utf-8

from Tkinter import *

class Applocation(Frame):
	def __init__(self,master = None):
		Frame.__init__(self,master)
		self.grid()
		self.createWidgets()
	def createWidgets(self):
		
		self.entry = Entry(self,width = 20)
		self.entry.grid(row = 1,column = 2,sticky = E)
		self.label = Label(self,text = "Quit")
		self.label.grid(row = 1,column = 1)
		self.quitButton = Button(self,padx = 5,pady = 5,text="Quit",command=self.btnCallBack)
		self.quitButton.grid(row = 2,column = 2)
	def btnCallBack(self):
		print "btnCallBack"
		print "entry:{}".format(self.entry.get())

app = Applocation()
app.master.title("Sample Application")
app.mainloop()
		