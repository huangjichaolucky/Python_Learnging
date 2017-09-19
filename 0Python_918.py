#-*- coding:utf-8 -*-
#推荐第一种写法
'''coding=utf-8'''

# #是注释
print("hello world")

'''
这是多行注释
'''



#1 变量
# number = 8
# 打印第一种方法
# print 'number = ', number
#第二种打印变量方法
# print "number = %s" %(number)


# price = 5.0
# money = number * price
# print "money = %s" %(money)




#2 输入
# high = input('请输入你的身高')
# print ("high = %s" %high)

'''
raw_input在pyhton2 下使用， 
Python3 使用input，在2下使用，当输入字符串
的时候报错
2 中 会将输入的内容当做命令来执行
3 输入的内容当做文件内容来处理
'''
name = raw_input("输入名字:")
print("name = %s" %name)

#17.9.18做 21.52
