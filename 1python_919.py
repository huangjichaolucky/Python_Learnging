# -*- coding=utf-8 -*-
import random
#这是注释

'''
#input获取的所有数据，都当做字符创
age = input("输入年纪")
# int(age)将 age变量转成int类型
#执行多条语句时，注意缩进的使用
if int(age) >= 18:
	print("能进网吧")
	print("能进网吧")	
	print("能进网吧")

else:
	print("未成年，不能进网吧")
	print("未成年，不能进网吧")
	print("未成年，不能进网吧")

#查看变量的数据类型
print("type = ", type(age))
'''

'''
1 if else  语句使用
2 类型转换
3 ifelse 后面之心多条语句
'''

'''
# 命名规则
# 数字、字母、下划线组成，数字不能开头
# 变量名不能和 关键字一样

#小驼峰命名法
englishScore = 100
#Python推荐下面的方法
english_score = 100
#大驼峰命名法
EnglishScore = 100
'''

#运算符
'''
+
-
*
// 取整
** 幂运算

可以对字符串进行 乘运算
'''

'''
#输出多个变量
wangName = "laowang"
wangAge = 33
print("name =%s, age = %s"
	%(wangName, wangAge))
'''


'''
!= 不等于
<>也是不等于， 在p3中不可用，P2中可用
>= 大于等于
== 等于

逻辑运算符 与或非
and or not


小技巧
可以用汉语先写逻辑，然后用语言翻译
'''

'''
number = 50
if not (number >0 and number < 100):
	print ("0..100")
else:
	print ("不符合条件啊")
'''

number = 85
if number > 100:
	print ("> 100")
elif number > 80:
	print (">80")
elif number > 60:
	print ("> 60")
else:
	print ("<= 50")
'''
if elif 的使用
'''

'''
while 1:	
	number2 = int(input("输入数字1-7:"))
	if number2 == 1:
		print ("星期1")
	elif number2 == 2:
		print ("星期2")
	elif number2 == 3:
		print ("星期3")
	elif number2 == 4:
		print ("星期4")
	elif number2 == 5:
		print ("星期5")
	elif number2 == 6:
		print ("星期6")
	elif number2 == 7:
		print ("星期7")
	else:
		print ("输入的数据不在1-7")
'''

'''
#打印1 - 10之间的输
number = 1
while number <= 10:
	print ("number = %d" %number)
	number = number + 1;

'''

a = 8
if a > 3:
	if a < 10:
		print ("a 在 3...10之间")
	else:
		print ("> 3 >10")
else:
	print ("<=3")

'''
if 嵌套,最多嵌套2层，再多层的话，可能有其他更好的解决
方法来取代这种多层嵌套
'''

'''
male = int(input("输入性别（1:男，2女）"))
if male == 1:
	print ("男")
	height = input("输入高矮:1高,2矮")
	money = input("是否富: 1富,2穷")
	cool = input("帅 1,2")
	if height == 1 and money == 1 and cool ==1:
		print ("是高富帅")
	else:
		print ("不是高富帅")
elif male == 2:
	print ("女")
else:
	print ("数据有误")
'''

'''
number = 1
maxNumber = 15
yu = maxNumber % 2
if yu == 0:
	half = maxNumber / 2
else:
	half = maxNumber / 2 + 1
print (half)

while number <= maxNumber:
	if number < half:		
		print (number * " *")
	else:
		print ((maxNumber - number + 1) * " *")
	# number = number + 1
	# 运算符
	number += 1

#打印 * 
'''


'''
number1 = 1
maxNumber = 9
while number1 <= maxNumber:
	number2 = 1
	while number2 <= number1:		
		#没有 end = "",打印后自动换行
		print ("%2d *%2d = %2d " %(number1, number2,
		number1 * number2), end = "")
		number2+=1
	print ("\n")
	number1 += 1

9 * 9乘法表
'''

'''
while 1:
	player = int(input("输入 0剪刀、1石头、2布") )
	computer = random.randint(0, 2)
	if (player >= 0 and player <=2 ):
		if (player == 0 and computer == 2) or (player == 1
		and computer == 0) or (player == 2 and computer == 1):
			print ("赢")
		elif (player == computer):
			print ("平局")
		else:
			print ("输了")
	else:
		print ("数据不和规范")
	print ("%d %d" %(player, computer))

模拟剪刀、石头、布 游戏
'''


