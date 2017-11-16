#-*- coding:utf-8 -*-

import xlsxwriter

#1 创建一个Excel文件

work = xlsxwriter.Workbook('1.xlsx')

work.write('A:A', 20)

work.close()