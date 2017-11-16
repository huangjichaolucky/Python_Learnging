#-*- coding=utf-8 -*-
'''
str100 = str(100)
print ("str = %s" %str100)

#字符串拼接
a = "lao"
b = "wang"
c = "zhao"
ab = a + b
ac = a + c 
print ab
print ac

ae = "==%s=" %a
print ae

print a[0]

longstring = "longString"
#从下标0位置开始，到下标 2-1 位置
print longstring[0:2]

#从下标0开始，到倒数第2位， 步长为2，默认是1
#最后字符的下标是-1
print longstring[0:-1:2]

#最后一个字符
longstring[-1]
#最开始一个字符
longstring[0]

#考虑如何逆序输入字符
longstring[::-1]
'''


'''
#-------------------------数组


longArray = ['1', '2', '3']
#增加
longArray.append('add')
longArray.insert(0,'11')
print longArray

#删除操作, 从尾部删除
# longArray.pop()

#删除 laoC， 根据内容删除
# longArray.remove('laoC')

#根据下标删除
# del longArray[0]

#改
#可以根据下标改元素

#查

# append() 将后面的参数作为整体添加到数据
# extend()， 参数只能是可以迭代的数据，
# 相当于将其中的数据一个个的加入到数组中去
'''

'''
#字典
#增删改查操作
dic = {'key1': 'value1',
	   'key2': 'value2'
	   }
print dic

dic['c'] = 'C'

#删
del dic['key1']

#查  可以用get, 若不存在相关的key2
#程序无返回，但不会崩溃
dic.get('key2')

#遍历 键值对
for (key, value) in dic.items():
	print ('%s %s' %(key, value))
'''

#元组
#只能够查看，不可以修改
# tuple1 = (1, 2, 3)


def printMethod():
	print 'helloWorld'

printMethod()

def addMethod(n1, n2):
	print n1 + n2
addMethod(3, 4)

def addMethod2(n1, n2):
	return n1 + n2

number = addMethod2(5, 7)
print number