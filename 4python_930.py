#-*- coding=utf-8 -*-
#第10天 1 - 4
#1 私有方法、私有变量
#2 __del__ 方法, 类似OC 中的dealloc 方法
#  	管理内存有点类似 OC 的引用计数

# sys 模块下的 getrefcount方法可以获取到引用计数的值
# 但该值比真实的值多1

#继承、方法重写
#如何调用父类的方法
#	1 通过父类名调用
#	2 通过super方法

# 私有方法、私有变量的继承
#	1 私有方法不会被继承
#	2 私有变量也不会被继承


#多重继承
#默认继承自 object
# class Base(object):
# 	def test(self):
# 		print ('base')
# class A(Base):
# 	def test1(self):
# 		print ('test1')
# class B(Base):
# 	def test2(self):
# 		print ('test2')
# class C(A, B):
# 	pass
# c = C()
# c.test1()
# c.test2()

#Python 是一门动态语言,既面向对象又面向过程

#类属性、实例属性
#类方法、实例方法
#类对象、实例对象
#@classmethod 创建一个类方法，如下
# @classmethod 
# def addNum(cls):
# 	pass

#@staticmethod创建静态方法


class Game:
	#类属性
	num = 0
	#类方法，可以被实例对象或者类调用
	@classmethod
	def addNum(cls):
		#操作类属性
		num = 100
		print ('调用类方法')

	#实例方法
	def __init__(self):
		#操作实例属性
		self.name = 'hello'
		print ('调用实例方法')

	#静态方法， 可以被实例对象或者类调用
	@staticmethod
	def printMethod():
		print ('调用静态方法')

game = Game()
game.addNum()
Game.addNum()

print ('\n')
game.printMethod()
Game.printMethod()