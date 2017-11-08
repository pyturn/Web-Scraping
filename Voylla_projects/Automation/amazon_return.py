# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from bs4 import BeautifulSoup
import unittest, time, re
import pdb, datetime, os, glob 

class Amazon(unittest.TestCase):
	def setUp(self):
		
		profile = webdriver.FirefoxProfile()
		profile.set_preference("browser.download.folderList", 2)
		profile.set_preference("browser.download.manager.showWhenStarting", True)
		profile.set_preference("browser.download.dir", "/tmp")
		profile.set_preference("browser.helperApps.neverAsk.saveToDisk","text/xls,application/vnd.openxmlformats-officedocument.spreadsheetml.sheet,application/vnd.ms-excel,text/plain,application/xls,text/comma-separated-values,application/octet-stream,text/csv")
		self.driver = webdriver.Firefox(firefox_profile=profile,executable_path='/home/localserver/bi/script/geckodriver')
		time.sleep(5)
		self.base_url = "https://sellercentral.amazon.in/"
		self.verificationErrors = []
		self.accept_next_alert = True
    
	def test_amazon(self):
		driver = self.driver
		driver.get(self.base_url + "/ap/signin?_encoding=UTF8&language=en_US&openid.assoc_handle=sc_in_amazon&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.ns.pape=http%3A%2F%2Fspecs.openid.net%2Fextensions%2Fpape%2F1.0&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fsellercentral.amazon.in%2Fgp%2Fhomepage.html%2F255-9855437-7391129%3Fie%3DUTF8%26*Version*%3D1%26*entries*%3D0&pageId=sc_eu_amazon")
		driver.find_element_by_id("ap_email").clear()
		driver.find_element_by_id("ap_email").send_keys("enter_your_id")
		driver.find_element_by_id("ap_password").clear()
		driver.find_element_by_id("ap_password").send_keys("enter_your_password")
		driver.find_element_by_id("signInSubmit").click()
		time.sleep(4)
		driver.get("https://sellercentral.amazon.in/gp/ssof/reports/search.html#orderAscending=&recordType=CUSTOMER_RETURNS&noResultType=&merchantSku=&fnSku=&FnSkuXORMSku=&reimbursementId=&orderId=&genericOrderId=&asin=&shipmentId=&hazmatStatus=&inventoryEventTransactionType=&inventoryAdjustmentReasonGroup=&eventDateOption=1&fromDate=dd%2Fmm%2Fyyyy&toDate=dd%2Fmm%2Fyyyy&startDate=&endDate=&eventMonthOption=1&fromMonth=1&fromYear=2017&toMonth=1&toYear=2017&startMonth=&startYear=&endMonth=&endYear=")
		time.sleep(10)
		driver.find_element_by_id("tab_download").click()
		time.sleep(3)
		Select(driver.find_element_by_id("downloadDateDropdown")).select_by_visible_text("last 7 days")
		time.sleep(3)
		#pdb.set_trace()
		driver.find_element_by_css_selector("button[name=\"Request Download\"]").click()
		time.sleep(150)
		html = driver.page_source
		soup = BeautifulSoup(html, "lxml")
		hrefLink = soup.find_all("a",{"class":"buttonImage"})[0]['href']
		if hrefLink == '':
			time.sleep(120)
			hrefLink = soup.find_all("a",{"class":"buttonImage"})[0]['href']
		try:
			driver.get('%s'%hrefLink)
		except:pass

		os.chdir("/tmp")
		time.sleep(30)
		files = glob.glob('/tmp/*.txt')
		newest = max(files , key = os.path.getctime)
		for file in files:
			if str(file) == "/.*tmp/fbaReturn.txt":
				os.remove('/.*tmp/fbaReturn.txt')
		os.rename(newest, 'fbaReturn.txt')
		txt_file = r"fbaReturn.txt"
		csv_file = r"fbaReturn.csv"
		in_txt = csv.reader(open(txt_file, "rb"), delimiter = '\t')
		out_csv = csv.writer(open(csv_file, 'wb'))
		out_csv.writerows(in_txt)
		

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
