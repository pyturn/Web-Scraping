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
		profile.set_preference("browser.download.dir",os.getcwd());
		profile.set_preference("browser.download.folderList",2);
		profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/csv,application/excel,application/vnd.msexcel,application/vnd.ms-excel,text/anytext,text/comma-separated-values,text/csv,application/vnd.ms-excel,application/vnd.openxmlformats-officedocument.spreadsheetml.sheet,application/octet-stream");
		profile.set_preference("browser.download.manager.showWhenStarting",False);
		profile.set_preference("browser.helperApps.neverAsk.openFile","application/csv,application/excel,application/vnd.msexcel,application/vnd.ms-excel,text/anytext,text/comma-separated-values,text/csv,application/vnd.ms-excel,application/vnd.openxmlformats-officedocument.spreadsheetml.sheet,application/octet-stream");
		profile.set_preference("browser.helperApps.alwaysAsk.force", False);
		profile.set_preference("browser.download.manager.useWindow", False);
		profile.set_preference("browser.download.manager.focusWhenStarting", False);
		profile.set_preference("browser.download.manager.alertOnEXEOpen", False);
		profile.set_preference("browser.download.manager.showAlertOnComplete", False);
		profile.set_preference("browser.download.manager.closeWhenDone", True);
		profile.set_preference("pdfjs.disabled", True);
		self.driver = webdriver.Firefox(profile)
		self.driver.implicitly_wait(30)
		self.base_url = "https://marketing.criteo.com/Login?redirectTo=%252FHome"
		self.verificationErrors = []
		self.accept_next_alert = True
    
	def test_flipkart(self):
		
		driver = self.driver
		driver.get(self.base_url + "/")
		pdb.set_trace()
		driver.find_element_by_id("loginEmailField").clear()
		driver.find_element_by_id("loginEmailField").send_keys("enter_your_id")
		driver.find_element_by_id("loginPasswordField").clear()
		driver.find_element_by_id("loginPasswordField").send_keys("enter_your_password")
#		driver.find_element_by_id("btnSignUp").click()
		pdb.set_trace()
		driver.find_element_by_css_selector("#btnSignUp > span:nth-child(1)").click()
		time.sleep(3)
		driver.get('https://marketing.criteo.com/Analyze/Display?reportId=7897')
		time.sleep(15)
		driver.find_element_by_css_selector('#ci-app > div > ui-advertiser-view > div.reporting-page.reporting-mode-view > div > div.selectors > date-picker-widget > div > div > button').click()
		driver.find_element_by_css_selector('.open > ul:nth-child(2) > li:nth-child(2)').click()
		driver.find_element_by_css_selector('.currencySelector > div:nth-child(1) > div:nth-child(1) > button:nth-child(1)').click()
		driver.find_element_by_css_selector('li.clickable:nth-child(63) > div:nth-child(1) > span:nth-child(2)').click()
		time.sleep(10)
		driver.find_element_by_css_selector('#reportDownloadDropdown').click()
#		pdb.set_trace()
		time.sleep(5)
		driver.find_element_by_css_selector('div.btn-group:nth-child(1) > ul:nth-child(2) > li:nth-child(1) > a:nth-child(1)').click()
#		driver.find_element_by_css_selector('div.btn-group:nth-child(1) > ul:nth-child(2) > li:nth-child(2) > a:nth-child(1)').click()
		time.sleep(10)


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