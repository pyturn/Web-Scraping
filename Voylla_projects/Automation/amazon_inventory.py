# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from bs4 import BeautifulSoup
import unittest, time, re
import pdb, datetime, os, glob 
import csv

class Amazon(unittest.TestCase):
	def setUp(self):
		
		profile = webdriver.FirefoxProfile()
		profile.set_preference("browser.download.dir",os.getcwd());
		profile.set_preference("browser.download.folderList",2);
		profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "text/xls,application/vnd.openxmlformats-officedocument.spreadsheetml.sheet,application/vnd.ms-excel,text/plain,application/xls,text/comma-separated-values,application/octet-stream,text/csv");
		profile.set_preference("browser.download.manager.showWhenStarting",False);
		profile.set_preference("browser.helperApps.neverAsk.openFile","text/xls,application/vnd.openxmlformats-officedocument.spreadsheetml.sheet,application/vnd.ms-excel,text/plain,application/xls,text/comma-separated-values,application/octet-stream,text/csv");
		profile.set_preference("browser.helperApps.alwaysAsk.force", False);
		profile.set_preference("browser.download.manager.useWindow", False);
		profile.set_preference("browser.download.manager.focusWhenStarting", False);
		profile.set_preference("browser.download.manager.alertOnEXEOpen", False);
		profile.set_preference("browser.download.manager.showAlertOnComplete", False);
		profile.set_preference("browser.download.manager.closeWhenDone", True);
		profile.set_preference("pdfjs.disabled", True);
		self.driver = webdriver.Firefox(profile)
		time.sleep(5)
		self.verificationErrors = []
		self.accept_next_alert = True
    
	def test_amazon(self):
		driver = self.driver
		driver.get("https://sellercentral.amazon.in//ap/signin?_encoding=UTF8&language=en_US&openid.assoc_handle=sc_in_amazon&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.ns.pape=http%3A%2F%2Fspecs.openid.net%2Fextensions%2Fpape%2F1.0&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fsellercentral.amazon.in%2Fgp%2Fhomepage.html%2F255-9855437-7391129%3Fie%3DUTF8%26*Version*%3D1%26*entries*%3D0&pageId=sc_eu_amazon")
		pdb.set_trace()
		driver.find_element_by_id("ap_email").clear()
		driver.find_element_by_id("ap_email").send_keys("enter_your_id")
		driver.find_element_by_id("ap_password").clear()
		driver.find_element_by_id("ap_password").send_keys("enter_your_password")
		driver.find_element_by_id("signInSubmit").click()
		time.sleep(4)
		driver.get("https://sellercentral.amazon.in/gp/ssof/reports/search.html#orderAscending=&recordType=INVENTORY_SNAPSHOT&noResultType=&merchantSku=&fnSku=&FnSkuXORMSku=&reimbursementId=&orderId=&genericOrderId=&asin=&lpn=&shipmentId=&hazmatStatus=&inventoryEventTransactionType=&inventoryAdjustmentReasonGroup=&eventDateOption=1&fromDate=dd%2Fmm%2Fyyyy&toDate=dd%2Fmm%2Fyyyy&startDate=&endDate=&eventMonthOption=1&fromMonth=1&fromYear=2017&toMonth=1&toYear=2017&startMonth=&startYear=&endMonth=&endYear=")
		time.sleep(7)
		driver.find_element_by_css_selector('#tab_download').click()
		time.sleep(3)
		driver.find_element_by_css_selector('table.formTable:nth-child(2) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > button:nth-child(1)').click()
		time.sleep(35)
		driver.find_element_by_css_selector('tr.list-row-odd:nth-child(1) > td:nth-child(4) > a:nth-child(1) > span:nth-child(1) > span:nth-child(1)').click()
		files = glob.glob('/home/abhinav/Desktop/*.txt')
		newest = max(files , key = os.path.getctime)
		

		with open(newest, 'r') as in_file:
		    stripped = (line.strip() for line in in_file)
		    lines = (line.split(",") for line in stripped if line)
		    with open('fbaInventory.csv', 'w') as out_file:
		        writer = csv.writer(out_file)
		        writer.writerows(lines)
		os.remove(newest)

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
