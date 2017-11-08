# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
import pdb, datetime, os,glob

class Flipkart(unittest.TestCase):
	def setUp(self):
		profile = webdriver.FirefoxProfile()
		profile.set_preference('browser.download.folderList', 2)
		profile.set_preference('browser.download.manager.showWhenStarting', False)
		profile.set_preference('browser.download.dir', os.getcwd())
		profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'text/csv/xls')
		self.driver = webdriver.Firefox(profile)
#		self.driver.implicitly_wait(30)
		time.sleep(5)
		self.base_url = "https://seller.flipkart.com/"
		self.verificationErrors = []
		self.accept_next_alert = True
    
	def test_flipkart(self):
		now = datetime.datetime.now()
		year = now.year
		month = now.month
		date1 = now.day
		if(date1 >= 8):
			date = date1-7
		else:
			date = 30-(7-date1)

		driver = self.driver
		driver.get(self.base_url + "/")
		driver.find_element_by_id("username").clear()
		driver.find_element_by_id("username").send_keys("enter_your_id")
		driver.find_element_by_id("userpass").clear()
		driver.find_element_by_id("userpass").send_keys("enter_your_password")
		driver.find_element_by_id("edit-submit").click()
		time.sleep(10)
		driver.get("https://seller.flipkart.com/index.html#dashboard/fa/report")
		time.sleep(10)
		try:
			driver.switch_to.frame(driver.find_element_by_css_selector('#webklipper-publisher-widget-container-notification-frame'))
			driver.find_element_by_css_selector('#webklipper-publisher-widget-container-notification-close-div').click()
			driver.switch_to_default_content()
		except :
			a=5
		time.sleep(7)
		driver.find_element_by_class_name('caret').click()
		time.sleep(10)
		driver.find_element_by_link_text("Hyderabad Medchal 01").click()
		time.sleep(10)
		driver.switch_to.frame(driver.find_element_by_tag_name('iframe'))
		time.sleep(5)
		select=Select(driver.find_element_by_xpath('/html/body/div[2]/section/div[4]/ui-view/div[2]/div[2]/div/ui-view/div[3]/div/ui-view/div[1]/div[1]/div/form/span[1]/select'))
		select.select_by_visible_text("Invoice (CSV)")
		time.sleep(5)
		driver.find_element_by_xpath('//*[@id="sfx"]/ui-view/div[1]/div[1]/div/form/span[1]/input').click()
		time.sleep(8)
		cal_left = driver.find_element_by_css_selector('body > div.daterangepicker.dropdown-menu.show-calendar.opensright > div.calendar.left')

		if(date1 < 8):
			driver.find_element_by_css_selector('body > div.daterangepicker.dropdown-menu.show-calendar.opensright > div.calendar.left > div > table > thead > tr:nth-child(1) > th.prev.available > i').click()

			driver.find_element_by_xpath('//*[@id="sfx"]/ui-view/div[1]/div[1]/div/form/span[1]/input').click()

		cal_left.find_element_by_xpath('//td[@class="available"][text()="'+str(date)+'"]').click()

		driver.find_element_by_xpath('//*[@id="sfx"]/ui-view/div[1]/div[1]/div/form/span[1]/input').click()
		driver.find_element_by_xpath('/html/body/div[4]/div[3]/div/button[1]').click()
		driver.find_element_by_xpath('//*[@id="sfx"]/ui-view/div[1]/div[1]/div/form/span[2]/span[1]/button').click()
		time.sleep(10)
		driver.refresh()
		time.sleep(3)
		driver.find_element_by_css_selector(".table > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(6) > span:nth-child(2) > a:nth-child(1)").click()
		time.sleep(10)
		files = glob.glob('/home/abhinav/Desktop/Flipkart_Task/*.csv')
		newest = max(files , key = os.path.getctime)
		for file in files:
			if str(file) == "/home/abhinav/Desktop/Flipkart_Task/faHyderabad.csv":
				os.remove('/home/abhinav/Desktop/Flipkart_Task/faHyderabad.csv')
		os.rename(newest, "faHyderabad.csv")
    	

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
