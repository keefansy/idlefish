#!usr/bin/python
#coding=utf-8
import os
import xlrd
import unittest
import HTMLTestRunner
import time
import sched
from openidlefish import driver,openidlefish,ElementA
from selenium.webdriver.support.ui import WebDriverWait
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


begintest = openidlefish()
def addexcelprodcut(openoff):#添加商品
	if openoff=='Y':
		begintest.Testopen()
	excel = xlrd.open_workbook(r"C:\Python27\idlefish\casedate\allproducts.xlsx")
	sheet = excel.sheets()[0]
	nrows = sheet.nrows  # 获取行数
	beginum = 1
	while beginum<nrows:#按照表格里的商品数量循环添加商品
		allcoldates = sheet.row_values(beginum)
		getusername01 = begintest.pushproduct(phonename=allcoldates[4])
		getusername02 = begintest.editproductinfo(title=allcoldates[0],text=allcoldates[1],price1=str(int(allcoldates[2])),price2=str(int(allcoldates[3])))
		print ' 第 %s 个 product be added end ！'%(beginum)
		beginum = beginum + 1
	driver.press_keycode(3)
	if getusername01 == getusername02:
		return [getusername01,beginum]
	else:
		return [getusername01,beginum,getusername02]


if __name__ == "__main__":
	#添加商品，添加完成后
	try:
		newusername = addexcelprodcut('Y')
	except:
		newsinfos = '%s 添加%s个商品添加过程中报错，且%s给你发送过信息 '\
					%(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())),newusername[1],newusername[0])
		newsinfos = unicode(newsinfos, 'utf-8')
		begintest.sendnews('lewis',newsinfos)#添加完商品后给自己发条消息
	else:
		newsinfos = '%s 已经正确添加完%s个商品,且%s给你发送过信息 '\
					% (time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())),newusername[1], newusername[0])
		newsinfos = unicode(newsinfos, 'utf-8')
		begintest.sendnews('lewis', newsinfos)  # 添加完商品后给自己发条消息