#-*- coding=utf-8 -*-
#工厂模式

# __new__ 方法
#	new只完成对象的创建、 init 方法对对象初始化

#单例

#异常处理

try:
	# print (a)
	open('a')
except NameError:
	print ('NameError')
#如果不是NameError，按此异常处理
#异常的统称， 通过ret 可以接收具体的错误原因

#Ctrl + c 也是一种异常
except Exception as ret:
	print ('Exceptiont %s' %ret)
else:
	print ('没有异常会执行')	
finally:
	print ('有无异常都会执行')
	
#自定义异常 详细见  11天09节


#该看 11天  11节