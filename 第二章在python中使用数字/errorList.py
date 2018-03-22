#[Python]"no encoding declared 错误"解决方法

# 在使用Python编译的时候出现如下错误：

# SyntaxError: Non-ASCII character '\xe5' in file Test1.py on line 8, but no encoding declared; see http://www.python.org/peps/pep-0263.html for details

# 解决方法

# python的默认编码文件是用的ASCII码，将文件存成了UTF-8，编译就可以通过。或在在py文件开头（必须是第一行）加入

#coding=utf-8 
# 或者
# -*- coding:utf-8 -*-

# 原因
# 如果要在python2的py文件里面写中文，则必须要添加一行声明文件编码的注释，否则python2会默认使用ASCII编码。