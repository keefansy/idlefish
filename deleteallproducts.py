#!usr/bin/python
#coding=utf-8
import os
import xlrd
import unittest
import time
from server import ElementA
from openidlefish import  driver,openidlefish
from addproducts import  addexcelprodcut
from selenium.webdriver.support.ui import WebDriverWait
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

begintest = openidlefish()
#删除商品，删除完成后给自己发消息
try:
    #begintest = openidlefish()
    begintest.Testopen()
    begintest.deleallproducts()#删除商品
except:
    newsinfos = '商品删除有误，%s 已经删除过商品'%(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    newsinfos = unicode(newsinfos, 'utf-8')
    begintest.sendnews('lewis',newsinfos)#添加完商品后给自己发条消息
else:
    newsinfos = '%s 已经正确删除完商品'%(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    newsinfos = unicode(newsinfos, 'utf-8')
    begintest.sendnews('lewis',newsinfos)#添加完商品后给自己发条消息


#添加商品，添加完成后给自己发消息
try:
    driver.start_activity('com.taobao.idlefish', 'com.taobao.fleamarket.home.activity.MainActivity')  #再次切换为闲鱼
    newusername = addexcelprodcut('N')
except:
	newsinfos = '%s 添加%s个商品添加过程中报错，且%s给你发送过信息 '\
				%(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())),newusername[1],newusername[0])
	newsinfos = unicode(newsinfos, 'utf-8')
	begintest.sendnews('lewis',newsinfos)#添加完商品后给自己发条消息
else:
	newsinfos = '%s 已经正确添加完%s个商品,且%s给你发送过信息 '\
				% (time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())),newusername[1],newusername[0])
	newsinfos = unicode(newsinfos, 'utf-8')
	begintest.sendnews('lewis', newsinfos)  # 添加完商品后给自己发条消息