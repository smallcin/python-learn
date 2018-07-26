#coding=utf-8

import Tkinter as tk

class Todo(tk.Tk,object):
	"""docstring for Todo"""
	def __init__(self, tasksTmp=None):
		super(Todo, self).__init__()
		#self.arg = arg
		print("Todo {}".format(tasksTmp))
		if tasksTmp == None:
			print("Todo if{}".format(tasksTmp))
			self.tasks = []
		else:
			print("Todo else{}".format(tasksTmp))
			self.tasks = []
		self.title("To-Do App v1")
		self.geometry("300x400")
		todo1 = tk.Label(self,text = "---Add Item here ---",bg = "lightgrey",fg = "black",pady = 10)
		self.tasks.append(todo1)
		for task in self.tasks:
			task.pack(side=tk.TOP,fill = tk.X)

if __name__ == "__main__":
	root = Todo(None) #None  参数为tasksTmp
	root.mainloop()