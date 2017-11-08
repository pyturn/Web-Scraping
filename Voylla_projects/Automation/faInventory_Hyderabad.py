# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re, glob
import pdb, datetime, os 
import pandas as pd 

class Flipkart(unittest.TestCase):
	def setUp(self):
		profile = webdriver.FirefoxProfile()
		profile.set_preference('browser.download.folderList', 2)
		profile.set_preference('browser.download.manager.showWhenStarting', False)
		profile.set_preference('browser.download.dir', '/tmp')
		profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'text/csv/xls')

		self.driver = webdriver.Firefox(firefox_profile=profile,executable_path='/home/localserver/bi/script/geckodriver')
#		self.driver.implicitly_wait(30)
		self.base_url = "https://seller.flipkart.com/"
		self.verificationErrors = []
		self.accept_next_alert = True
    
	def test_flipkart(self):
		
		driver = self.driver
		driver.get(self.base_url + "/")
		driver.find_element_by_id("username").clear()
		driver.find_element_by_id("username").send_keys("enter_your_id")
		driver.find_element_by_id("userpass").clear()
		driver.find_element_by_id("userpass").send_keys("enter_your_password")
		driver.find_element_by_id("edit-submit").click()
		time.sleep(5)
		driver.get("https://seller.flipkart.com/index.html#dashboard/fa/inventory")
		time.sleep(20)
		driver.find_element_by_xpath('//*[@id="dropdownMenu1"]').click()
		driver.find_element_by_link_text('Hyderabad Medchal 01').click()
		time.sleep(5)
		driver.find_element_by_css_selector(".checkbox-container > input:nth-child(1)").click()
		time.sleep(5)
		driver.find_element_by_css_selector('div.dropdown:nth-child(3) > button:nth-child(1)').click()
		time.sleep(5)
		driver.find_element_by_css_selector('div.dropdown:nth-child(3) > ul:nth-child(2) > li:nth-child(1)').click()
		time.sleep(10)
		files = glob.glob('/tmp/*.csv')
		newest = max(files , key = os.path.getctime)
		for file in files:
			if str(file) == "/tmp/faInventory.csv":
				os.remove('/tmp/faInventory.csv')
		os.rename(newest, "faInventory.csv")
		time.sleep(15)
		df = pd.read_csv('faInventory.csv')
		for i in range(df.shape[0]):
			df['Warehouse']='Hyderabad'
		df.to_csv('faInventory.csv',index=False)


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
