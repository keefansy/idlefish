#!usr/bin/python
#coding=utf-8
import os
from appium import webdriver
from time import sleep
import subprocess

#ipp = ['31465c2b7d92','11915135']
class ElementA():
	def open(self):
		#for i in range(len(ip)):
		desired_caps = {}
		desired_caps['platformName'] = 'Android'
		#desired_caps['platformVersion'] = '4.4.4'
		desired_caps['deviceName'] = 'M15'
		desired_caps['appPackage'] = 'com.taobao.idlefish'
		#desired_caps['appPackage'] = 'com.douban.frodo'
		#desired_caps['appActivity']= 'com.douban.frodo.activity.SplashActivity'
		desired_caps['appActivity'] = 'com.taobao.fleamarket.home.activity.MainActivity'
		#desired_caps['automationName'] = 'Selendroid'#捕捉toast信息
		desired_caps['unicodeKeyboard'] = 'True'
		desired_caps['resetKeyboard'] = 'True'
		__driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
		#driverlist.append(__driver)
		return __driver

