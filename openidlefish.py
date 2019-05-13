#!usr/bin/python
#coding=utf-8
import os
import xlrd
import time
import sys
#reload(sys)
from server import ElementA
#sys.setdefaultencoding('utf8')
from selenium.webdriver.support.ui import WebDriverWait
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

test = ElementA()
driver = test.open()
class openidlefish():

	def Testopen(self):#打开并登录闲鱼后返回进入到主页面
		try:
			driver.find_element_by_xpath("//android.widget.TextView[@text='暂不升级']").click()
		except:
			pass
		try:
			WebDriverWait(driver, 7).until(lambda x: x.find_element_by_id('com.android.packageinstaller:id/permission_allow_button'))
		except:
			WebDriverWait(driver, 7).until(lambda x: x.find_element_by_id('android:id/button1'))
			driver.find_element_by_id('android:id/button1').click()
		else:
			pass
		while True:
			try:
				driver.find_element_by_id('com.android.packageinstaller:id/permission_allow_button').click()
			except:
				break
			else:
				pass

		driver.find_element_by_id('com.taobao.idlefish:id/tab_post_icon').click()#登录闲鱼
		time.sleep(3)
		x = driver.get_window_size()['width']
		y = driver.get_window_size()['height']
		#print x,y
		ratiox = (800.0/1440.0)
		ratioy = (1450.0/2560.0)
		#print ratiox,ratioy
		newx01=(ratiox*x-10)
		newy01=(ratioy*y-10)
		newx02=ratiox*x
		newy02=ratioy*y
		#print newx01 ,newy01 ,newx02,newy02,ratiox*x,ratioy*y ,ratiox ,ratioy
		driver.tap([(newx01,newy01),(newx02,newy02)],500)
		WebDriverWait(driver, 10).until(lambda x: x.find_element_by_xpath("//android.widget.TextView[@text='淘宝账户授权']"))
		ratioyloginx = (380.0/1440.0)
		ratioyloginy = (1600.0 / 2560.0)
		loginx01 = (ratioyloginx*x-20)
		loginy01 = (ratioyloginy*y -20)
		loginx02 = ratioyloginx*x
		loginy02 = ratioyloginy*y
		time.sleep(3)
		#driver.find_element_by_xpath("//android.view.View[@text='确认授权']").click()
		while True:#尝试多次登录闲鱼
			try:
				driver.tap([(loginx01, loginy01), (loginx02, loginy02)], 500)#根据坐标来定位登录按钮，登录闲鱼
			except:
				driver.tap([(loginx01-10, loginy01-10), (loginx02, loginy02)], 500)  # 根据坐标来定位登录按钮，登录闲鱼
			else:
				break
		try:
			WebDriverWait(driver, 10).until(lambda x: x.find_element_by_id("com.taobao.idlefish:id/publish_icon"))
			driver.find_element_by_id('com.taobao.idlefish:id/publish_icon').click()
		except:
			print 'at x location error'
		else:
			time.sleep(2)

	def pushproduct(self,phonename):#从发布开始到上传图片完成进入到编辑信息页面
		newusername = '没有人'
		x = driver.get_window_size()['width']
		y = driver.get_window_size()['height']
		clicky = (61.0/2560.0)*y
		driver.find_element_by_id('com.taobao.idlefish:id/tab_post_icon').click()#点击发布按钮
		driver.find_element_by_id('com.taobao.idlefish:id/pop_out_entry_first').click()
		time.sleep(5)
		while True:
			try:
				driver.find_element_by_id('com.android.packageinstaller:id/permission_allow_button').click()
			except:
				break
			else:
				pass
		time.sleep(3)
		#检查有消息时打开消息，然后再打开相册，然后消息人的名称
		while True:
			try:
				driver.find_element_by_id('com.taobao.idlefish:id/center_text').click()
				time.sleep(1.5)
			except:
				driver.tap([(x / 2, clicky - 10), (x / 2, clicky)], 1500)
			else:
				try:
					driver.find_element_by_id("com.taobao.idlefish:id/pond_chat_box_content").text
					newusername = driver.find_element_by_id('com.taobao.idlefish:id/center_text').text
					driver.press_keycode(4)
				except:
					try:#发有人关注的消息情况下查看并退出
						driver.find_element_by_xpath("//android.view.View[@text='我的粉丝']")
						driver.press_keycode(4)
					except:
						break
					else:
						pass
				else:
					pass
		phonenameelemnet = "//android.widget.TextView[@text='%s']"%phonename
		#滑动选中相册名称
		while True:
			try:
				driver.find_element_by_xpath(phonenameelemnet)
			except:
				driver.swipe(x/2,y/2,x/2,y/2-(640.0/2560.0)*y,1500)
			else:
				break
		driver.find_element_by_xpath(phonenameelemnet).click()
		phones = driver.find_elements_by_class_name('android.widget.ImageView')[1:]
		#print phones , len(phones)
		for phone in phones:
			phone.click()
			while True:#查看是否有消息进来，如有打开消息后再进行操作
				try:
					driver.find_element_by_id('com.taobao.idlefish:id/title_select').click()
					time.sleep(1.5)
				except:
					break
				else:
					try:
						driver.find_element_by_id("com.taobao.idlefish:id/pond_chat_box_content").text
						newusername = driver.find_element_by_id('com.taobao.idlefish:id/center_text').text
						driver.press_keycode(4)
					except:
						try:
							driver.find_element_by_xpath("//android.view.View[@text='我的粉丝']")
							driver.press_keycode(4)
						except:
							break
						else:
							pass
					else:
						pass

			driver.find_element_by_id('com.taobao.idlefish:id/title_back').click()
		driver.find_element_by_id('com.taobao.idlefish:id/confirm').click()
		driver.find_element_by_id('com.taobao.idlefish:id/effect_next').click()
		WebDriverWait(driver, 15).until(lambda x: x.find_element_by_xpath("//android.view.View[@text='全新宝贝']"))
		return newusername

	def editproductinfo(self,title,text,price1,price2):#选择和编辑发布信息并返回到我的tab函数
		newusername = '没有人'
		numbers = driver.find_elements_by_xpath('//android.widget.EditText')
		while True:#当有消息过来时打开消息然后再执行下面的操作
			try:
				numbers[0].send_keys(title)
				time.sleep(1.5)
			except:
				break
			else:
				try:
					driver.find_element_by_id("com.taobao.idlefish:id/pond_chat_box_content").text
					newusername = driver.find_element_by_id('com.taobao.idlefish:id/center_text').text
					driver.press_keycode(4)
				except:
					try:
						driver.find_element_by_xpath("//android.view.View[@text='我的粉丝']")
						driver.press_keycode(4)
					except:
						break
					else:
						pass
				else:
					pass
		numbers[1].send_keys(text)
		beginx = driver.find_element_by_xpath("// android.view.View[ @ text = '照片/视频']").location.get('x') # 获取元素对应的x的坐标值
		beginy = driver.find_element_by_xpath("// android.view.View[ @ text = '照片/视频']").location.get('y') # 获取元素对应的y的坐标值
		endx = driver.find_element_by_xpath("// android.view.View[ @ text = '发布']").location.get('x') # 获取元素对应的x的坐标值
		endy = driver.find_element_by_xpath("// android.view.View[ @ text = '发布']").location.get('y') # 获取元素对应的y的坐标值
		driver.swipe(beginx,beginy,endx,endy,500)
		driver.find_element_by_xpath("//android.view.View[@text='价格']").click()
		edittext = driver.find_elements_by_xpath("//android.widget.EditText")
		#print len(edittext), edittext
		edittext[0].click()
		for everyelement in price1:#输入价格
			element1 = ("//android.widget.Button[@text='%s']") %(everyelement)
			driver.find_element_by_xpath(element1).click()
		edittext[-1].click()
		for everyelement in price2:#输入运费
			element2 = ("//android.widget.Button[@text='%s']") % (everyelement)
			driver.find_element_by_xpath(element2).click()
		driver.find_element_by_xpath("//android.widget.Button[@text='确定']").click()
		driver.find_element_by_xpath("//android.view.View[@text='邮寄']").click()
		driver.find_element_by_xpath("//android.view.View[@text='确认发布']").click()
		while True:
			try:
				WebDriverWait(driver, 3).until(lambda x: x.find_element_by_xpath("//android.widget.TextView[@text='我的']"))
			except:
				driver.press_keycode("4")
				time.sleep(1)
			else:
				break
		driver.find_element_by_xpath("//android.widget.TextView[@text='我的']").click()
		time.sleep(2.5)
		return newusername

	def checknews(self):#查询是否有新消息回复
		x = driver.get_window_size()['width']
		y = driver.get_window_size()['height']
		for newstab in  driver.find_elements_by_id("com.taobao.idlefish:id/tab_title"):
			if newstab.text == u'消息':
				newstab.click()
				time.sleep(2)
		print '开始监控是否有新消息'
		driver.swipe(x / 2, y / 2, x / 2, y / 2 + 400, 5500)  # 持续刷新页面等待消息
		print '刷新消息页面'
		while True:
			newsnum = driver.find_element_by_id("com.taobao.idlefish:id/msg_tag_debug_text_id").text
			try:
				driver.find_element_by_id("com.taobao.idlefish:id/msg_tag_debug_text_id")
				if driver.find_element_by_id("com.taobao.idlefish:id/msg_tag_debug_text_id").text <>"":
					print '有%s条消息进来'%(newsnum.encode('gbk'))
				else:
					print '暂时无消息'
					driver.find_element_by_id("com.taobao.idlefish:id/msg_tag_debug_text_0000")
			except:
				driver.swipe(x / 2, y / 2, x / 2, y / 2 + 400, 5500)  # 持续刷新页面等待消息
			else:
				print '---开始查看新消息---'
				break

	def watcheverynews(self):#开始读取每个人的消息
		aaa = driver.find_elements_by_id("com.taobao.idlefish:id/msg_tag_debug_text_id")
		#print len(aaa),aaa
		for i in aaa:
			if i.text <>"":#开始进入到消息界面查看消息
				i.click()
				#WebDriverWait(driver, 4).until(lambda x: x.find_element_by_id("com.taobao.idlefish:id/center_text")
				try:
					driver.find_element_by_id("com.taobao.idlefish:id/close_icon").click()#关闭见一见
				except:
					pass
				finally:
					time.sleep(2)
					celltext = driver.find_elements_by_id("com.taobao.idlefish:id/cell_text")[-1].text
					username = driver.find_element_by_id("com.taobao.idlefish:id/center_text").text
					productprice = driver.find_element_by_id("com.taobao.idlefish:id/tv_price").text
					return [username,productprice,celltext]#把商品相关信息返回
					break


	def toidelfish(self,appname):#再次切换程序
		driver.press_keycode('3')
		time.sleep(1)
		if appname == 'idlefish':
			driver.start_activity('com.taobao.idlefish', 'com.taobao.fleamarket.home.activity.MainActivity')# 切换为闲鱼
		elif appname == 'QQ':
			driver.start_activity('com.tencent.mobileqq', 'com.tencent.mobileqq.activity.SplashActivity')  # 切换为QQ
		elif appname == 'weixin':
			driver.start_activity('com.tencent.mm','com.tencent.mm.ui.LauncherUI')#切换为微信
		else:
			print 'app名称输入错误，请重新检查输入'

	def toapp(self,username,infos):#切换到app程序，并把消息发送给自己，前提是app必须登录,传入一个用户的名称
		allinfos =infos
		print allinfos
		driver.press_keycode(3)
		time.sleep(3)
		#driver.start_activity('com.tencent.mm','com.tencent.mm.ui.LauncherUI')#切换为微信
		driver.start_activity('com.tencent.mobileqq','com.tencent.mobileqq.activity.SplashActivity')#切换为QQ
		WebDriverWait(driver, 5).until(lambda x: x.find_element_by_id("com.tencent.mobileqq:id/name"))
		driver.find_element_by_xpath("//android.widget.TextView[@text='联系人']").click()
		driver.find_element_by_id("com.tencent.mobileqq:id/et_search_keyword").click()
		username = unicode(username, 'utf-8')
		xpathname = "//android.widget.TextView[@text='(%s)']"%username
		print username
		driver.find_element_by_id("com.tencent.mobileqq:id/et_search_keyword").send_keys(username)
		driver.find_element_by_xpath(xpathname).click()
		sendtext = "%s用户正在咨询价位为%s的商品，内容为：%s,请及时回复"%(allinfos[0],allinfos[1],allinfos[2])
		driver.find_element_by_id("com.tencent.mobileqq:id/input").\
			send_keys(sendtext)
		driver.find_element_by_id("com.tencent.mobileqq:id/fun_btn").click()
		newalloes = driver.find_elements_by_id("com.tencent.mobileqq:id/chat_item_content_layout")
		while True:
			if newalloes[-1].text <>sendtext:
				replynews = newalloes[-1].text
				break
		print replynews
		return [replynews,allinfos[0]]#返回回复的消息

	def sendnews(self,username,infos):#向qq发送添加商品成功或者删除商品的消息
		driver.press_keycode(3)
		time.sleep(3)
		# driver.start_activity('com.tencent.mm','com.tencent.mm.ui.LauncherUI')#切换为微信
		driver.start_activity('com.tencent.mobileqq', 'com.tencent.mobileqq.activity.SplashActivity')  # 切换为QQ
		WebDriverWait(driver, 5).until(lambda x: x.find_element_by_id("com.tencent.mobileqq:id/name"))
		driver.find_element_by_xpath("//android.widget.TextView[@text='联系人']").click()
		driver.find_element_by_id("com.tencent.mobileqq:id/et_search_keyword").click()
		username = unicode(username, 'utf-8')
		xpathname = "//android.widget.TextView[@text='(%s)']" % username
		#print username
		driver.find_element_by_id("com.tencent.mobileqq:id/et_search_keyword").send_keys(username)
		time.sleep(3)
		#driver.find_element_by_xpath(xpathname).click()
		driver.find_element_by_id('com.tencent.mobileqq:id/image').click()
		driver.find_element_by_id("com.tencent.mobileqq:id/input"). \
			send_keys(infos)
		driver.find_element_by_id("com.tencent.mobileqq:id/fun_btn").click()
		driver.press_keycode(3)


	def getandreplynews(self,replytextgetinfos):#把回复的消息传给闲鱼客户端
		x = driver.get_window_size()['width']
		y = driver.get_window_size()['height']
		retext = replytextgetinfos
		openidlefish.toidelfish(self,'idlefish')
		for newstab in driver.find_elements_by_id("com.taobao.idlefish:id/tab_title"):
			if newstab.text == u'消息':
				newstab.click()
				time.sleep(1)
		while True:
			try:
				driver.find_element_by_xpath("//android.widget.TextView[@text='%s']")%retext[1]
			except:
				driver.swipe(x/2,y/2,x/2,y/2-300,1500)
			else:
				driver.find_element_by_xpath("//android.widget.TextView[@text='%s']") %(retext[1]).click()
				break
		driver.find_element_by_id("com.taobao.idlefish:id/pond_chat_box_content").send_keys(retext[0])
		driver.find_element_by_id("com.taobao.idlefish:id/chat_send_button")


	def allnums(self,seenums):#根据用户的浏览量决定是否删除
		for i in range(seenums):
			decstion = '浏览%s'%i
			print decstion
			try:
				num = driver.find_elements_by_accessibility_id(decstion)[0].text
				print num
				if i >= seenums:
					return False
				else:
					return  True
			except:
				if i  == seenums:
					return True
				else:
					pass



	def deleallproducts(self,seenums):#循环删除商品,传入一个用户的浏览量参数
		x = driver.get_window_size()['width']
		y = driver.get_window_size()['height']
		morex = (1277.0 / 1440.0) * x
		morey = (1759.0 / 2560.0) * y
		delex = (700.0 / 1440.0) * x
		deley = (1700 / 2560.0) * y
		enterx = (994.0 / 1440.0) * x
		entery = (1441.0 / 2560.0) * y
		swipey = (585.0/2560.0)*y
		beignswipey = (1860.0/2560.0)*y
		driver.find_element_by_xpath("//android.widget.TextView[@text='我的']").click()
		time.sleep(1.5)
		driver.find_element_by_xpath("//android.widget.TextView[@text='我发布的']").click()
		time.sleep(1.5)
		delenum = 1
		while True:
			try:
			# iftf = self.allnums(seenums)#调用查看商品的浏览量，返回是否删除
			# if iftf is True:
				driver.find_element_by_accessibility_id("更多").click()
				time.sleep(1)
				driver.find_element_by_accessibility_id("删除").click() # 根据坐标来定位删除按钮
				time.sleep(1)
				driver.find_element_by_accessibility_id("确认").click()  # 根据坐标来定位确认按钮
				time.sleep(2)
				delenum = delenum + 1
			except:
				driver.press_keycode(4)
				driver.find_element_by_xpath("//android.widget.TextView[@text='我发布的']").click()
				try:
					driver.find_element_by_accessibility_id("发布宝贝赚钱")
				except:
					driver.press_keycode(4)
				else:
					driver.press_keycode(4)
					break
			else:
				print " 删除 %s 个商品 "%delenum
		#driver.press_keycode(3)

if __name__ == '__main__':

	begintest = openidlefish()
	begintest.Testopen()
	beginum = 1
	excel = xlrd.open_workbook(r"C:\Python27\idlefish\casedate\allproducts.xlsx")
	sheet = excel.sheets()[0]
	nrows = sheet.nrows  # 获取行数
	#driver.press_keycode('3')
	begintest.checknews()
	ifos = begintest.watcheverynews()
	getinfos = begintest.toapp(ifos,'lewis')
	begintest.getandreplynews(getinfos)
	begintest.deleallproducts()#删除商品