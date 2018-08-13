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
		self.task_create = tk.Text(self,height = 3,bg = "white",fg = "black")
		self.task_create.pack(side = tk.BOTTOM,fill = tk.X)
		self.task_create.focus_set()
		self.bind("<Return>",self.add_item)
		self.colour_schemes = [{"bg":"lightgrey","fg":"black"},{"bg":"grey","fg":"white"}]

	def add_item(self,event = None):
		task_text = self.task_create.get(1.0,tk.END).strip()
		if len(task_text) > 10:
			new_text = tk.Label(self,text = task_text,pady = 10)
			_, task_style_choice= divmod(len(self.tasks),2)
			my_scheme_choice = self.colour_schemes[task_style_choice]
			new_text.configure(bg = my_scheme_choice["bg"])
			new_text.configure(fg = my_scheme_choice["fg"])
			new_text.pack(side = tk.TOP,fill = tk.X)
			self.tasks.append(new_text)

		self.task_create.delete(1.0,tk.END)

if __name__ == "__main__":
	root = Todo(None) #None  参数为tasksTmp
	root.mainloop()