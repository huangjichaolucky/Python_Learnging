#-*- coding=utf-8 -*-
#局部变量、全局变量

a = 100

def test1():
	print("a = %d" %a)

def test2():
	print("a = %d" %a)

#缺省参数， 缺省参数的值如果没有传入，被认为是
#默认值, 带默认值的参数一定要位于参数列表的最后
def printInfo(name, age = 30):
	print("name =%s age= %d" %(name, age))
printInfo("huang")
printInfo("ji", 20)

'''
#不定长参数  不懂， 引用传参
def functionName([format_args,] *args, 
	**kwargs):
	function_suit 
	return [expression]
functionName()

'''
