#coding=utf-8
# import Tkinter
# top = Tkinter.Tk()
# #进入消息循环
# top.mainloop()

# from Tkinter import *
# root = Tk()

# li = ['C',"python","php","html","SQL"]
# movie = ["CSS","jQuery","Bootstrap"]
# lisb = Listbox(root)
# listb2 = Listbox(root)

# for item in li:
# 	lisb.insert(0,item)

# for item in movie:
# 	listb2.insert(0,item)

# lisb.pack()
# listb2.pack()
# root.mainloop()

import wx
app = wx.App(False)
frame = wx.Frame(None,wx.ID_ANY,"Hello World")
frame.Show(True)
app.MainLoop()