# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
import pdb, datetime, os, glob 

class Flipkart(unittest.TestCase):
	def setUp(self):
		profile = webdriver.FirefoxProfile()
		profile.set_preference('browser.download.folderList', 2)
		profile.set_preference('browser.download.manager.showWhenStarting', False)
		profile.set_preference('browser.download.dir', os.getcwd())
		profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
		# driver = webdriver.Firefox(profile)
		self.driver = webdriver.Firefox(profile)
		self.driver.implicitly_wait(30)
		self.base_url = "https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fadwords.google.com%2Fum%2Fidentity%3Fltmpl&hl=en_US&service=adwords&skipvpage=true&ltmpl=signin&flowName=GlifWebSignIn&flowEntry=ServiceLogin"
		self.verificationErrors = []
		self.accept_next_alert = True
    
	def test_google(self):
		
		driver = self.driver
		driver.get(self.base_url + "/")
#		pdb.set_trace()
		driver.find_element_by_id("identifierId").clear()
		driver.find_element_by_id("identifierId").send_keys("enter_your_id")
		driver.find_element_by_css_selector("span.RveJvd.snByac").click()
		time.sleep(3)
		driver.find_element_by_name("password").clear()
		driver.find_element_by_name("password").send_keys("enter_your_password")
		driver.find_element_by_css_selector("span.RveJvd.snByac").click()
		time.sleep(25)


		pdb.set_trace()
		driver.find_element_by_css_selector(".aw-current-date-selection-new").click()
		driver.find_element_by_id('gwt-uid-884').click()
		driver.find_element_by_css_selector(".cg-t > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1)").click()
		driver.find_element_by_css_selector("#gwt-uid-745").click()
		time.sleep(10)
		driver.find_element_by_css_selector('.clf-g > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1)').click()
		driver.find_element_by_id('gwt-uid-1003').click()
		driver.find_element_by_css_selector('div.aw-savecancel-panel:nth-child(1) > span:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > span:nth-child(1)').click()
		time.sleep(8)

#		pdb.set_trace()
		driver.get("https://adwords.google.com/cm/CampaignMgmt?authuser=0&__u=8424263312&__c=4209699916#c.386787084.ag&app=cm")
		time.sleep(10)
		driver.find_element_by_css_selector('.aw-current-date-selection-new').click()
		driver.find_element_by_id('gwt-uid-884').click()
		driver.find_element_by_css_selector(".cg-t > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1)").click()
		driver.find_element_by_id('gwt-uid-1298').click()
		time.sleep(10)
		driver.find_element_by_css_selector('.clf-g > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1)').click()
		driver.find_element_by_id('gwt-uid-1460').click()
		driver.find_element_by_css_selector('div.aw-savecancel-panel:nth-child(1) > span:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > span:nth-child(1)').click()
		time.sleep(5)



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