#-*- coding=utf-8 -*-
# 面向对象

stu_a = {
	'name': 'a',
	'age': '23',
	'home': 'heNan'
}

stu_b = {
	'name': 'b',
	'age': '22',
	'home': 'shangHai'
}
print (stu_a)
print (stu_b)

class Student(object):
	"""docstring for Student学生类"""	
	def __init__(self, name, age):
		super(Student, self).__init__()
		self.name = name
		self.age = age
	def printStuInfo(self):
		print('%s %s' %(self.name, self.age))
stu1 = Student('huang', 23)
stu1.printStuInfo()

class Cat:
	def eat(self):
		print('吃东西')
	def drink(self):
		print('喝水方法')
'''
class 类名：
	#属性

	#方法

'''


#