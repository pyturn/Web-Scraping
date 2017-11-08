# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
import pdb, datetime, os, glob 

class Flipkart(unittest.TestCase):
	def setUp(self):
		profile = webdriver.FirefoxProfile()
		profile.set_preference('browser.download.folderList', 2)
		profile.set_preference('browser.download.manager.showWhenStarting', False)
		profile.set_preference('browser.download.dir', os.getcwd())
		profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'application/vnd.ms-excel')
		# driver = webdriver.Firefox(profile)
		self.driver = webdriver.Firefox(profile)
		self.driver.implicitly_wait(30)
		self.base_url = "https://www.facebook.com/"
		self.verificationErrors = []
		self.accept_next_alert = True
    
	def test_flipkart(self):
		
		driver = self.driver
		driver.get(self.base_url + "/")
		driver.find_element_by_id("email").clear()
		driver.find_element_by_id("email").send_keys("enter_your_id")
		driver.find_element_by_id("pass").clear()
		driver.find_element_by_id("pass").send_keys("enter_your_password")
		time.sleep(10)
		pdb.set_trace()
		driver.find_element_by_id("u_0_r").click()
		time.sleep(5)
		
#		driver.get('https://www.facebook.com/ads/manager/accounts/?act=126144237804364')
#		time.sleep(5)
#		driver.get('https://business.facebook.com/home/accounts?business_id=781358231978911')
#		time.sleep(5)
		driver.get('https://business.facebook.com/ads/manager/account/campaigns/?act=848357492669&pid=p1&business_id=781358231978911')
		time.sleep(20)
		pdb.set_trace()
		driver.find_element_by_css_selector('._2a2d').click()
		driver.find_element_by_css_selector('button._1x8p').click()
		time.sleep(7)
#		driver.back()
#		time.sleep(5)
		driver.get('https://business.facebook.com/ads/manager/account/campaigns/?act=968148763299856&pid=p1&business_id=781358231978911')
		time.sleep(25)
		driver.find_element_by_css_selector('._2z1w').click()
		driver.find_element_by_css_selector('._2a2d').click()
		driver.find_element_by_css_selector('button._1x8p').click()
		time.sleep(7)
#		driver.back()
#		time.sleep(5)
		driver.get('https://business.facebook.com/ads/manager/account/campaigns/?act=798884183559649&pid=p1&business_id=781358231978911')
		time.sleep(20)
		driver.find_element_by_css_selector('._1uz0').click()
		driver.find_element_by_css_selector('li._rce:nth-child(4)').click()
		driver.find_element_by_css_selector('button._4jy0:nth-child(3)').click()
		time.sleep(3)
		driver.find_element_by_css_selector('._2a2d').click()
		driver.find_element_by_css_selector('button._1x8p').click()
		time.sleep(7)
#		driver.back()
#		time.sleep(5)
		driver.get('https://business.facebook.com/ads/manager/account/campaigns/?act=1146613965453334&pid=p1&business_id=781358231978911')
		time.sleep(20)
#		pdb.set_trace()
		driver.find_element_by_css_selector('._1uz0').click()
		driver.find_element_by_css_selector('li._rce:nth-child(3)').click()
		driver.find_element_by_css_selector('button._4jy0:nth-child(3)').click()
		time.sleep(3)
		driver.find_element_by_css_selector('._2a2d').click()
		driver.find_element_by_css_selector('button._1x8p').click()
		time.sleep(7)
#		driver.back()
#		time.sleep(5)
		driver.get('https://business.facebook.com/ads/manager/account/campaigns/?act=1043676909080374&pid=p1&business_id=781358231978911')
		time.sleep(20)
		driver.find_element_by_css_selector('._1uz0').click()
		driver.find_element_by_css_selector('li._rce:nth-child(3)').click()
		driver.find_element_by_css_selector('button._4jy0:nth-child(3)').click()
		time.sleep(3)
		driver.find_element_by_css_selector('._2a2d').click()
		driver.find_element_by_css_selector('button._1x8p').click()
		time.sleep(7)
		
#		files = glob.glob('C:/Users/Abhinav Jain/Documents/Flipkart_Task/*.csv')
		
#		newest = max(files , key = os.path.getctime)
#		for file in files:
#			if str(file) == "C:/Users/Abhinav Jain/Documents/Flipkart_Task\\faBilaspur.csv":
#				os.remove('C:/Users/Abhinav Jain/Documents/Flipkart_Task\\faBilaspur.csv')
#		os.rename(newest, "faBilaspur.csv")


	def is_element_present(self, how, what):
		try: self.driver.find_element(by=how, value=what)
		except NoSuchElementException as e: return False
		return True
    
	def is_alert_present(self):
		try: self.driver.switch_to_alert()
		except NoAlertPresentException as e: return False
		return True
    
	def close_alert_and_get_its_text(self):
		try:
			alert = self.driver.switch_to_alert()
			alert_text = alert.text
			if self.accept_next_alert:
				alert.accept()
			else:
				alert.dismiss()
			return alert_text
		finally: self.accept_next_alert = True
    
	def tearDown(self):
		self.driver.quit()
		self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
#This last line of code allows us to run all the test code just by running the file.