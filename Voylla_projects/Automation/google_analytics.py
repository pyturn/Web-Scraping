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
		profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
		# driver = webdriver.Firefox(profile)
		self.driver = webdriver.Firefox(profile)
		self.driver.implicitly_wait(30)
		self.base_url = "https://accounts.google.com/signin/v2/identifier?service=analytics&passive=1209600&continue=https%3A%2F%2Fanalytics.google.com%2Fanalytics%2Fweb%2F%23&followup=https%3A%2F%2Fanalytics.google.com%2Fanalytics%2Fweb%2F&flowName=GlifWebSignIn&flowEntry=ServiceLogin"
		self.verificationErrors = []
		self.accept_next_alert = True
    
	def test_flipkart(self):

		now = datetime.datetime.now()
		year = now.year
		month_name = now.strftime("%B")
		date1 = now.day-1
		month = month_name + " " +str(year)  
		driver = self.driver
		driver.get(self.base_url + "/")
#		pdb.set_trace()
		driver.find_element_by_id("identifierId").clear()
		driver.find_element_by_id("identifierId").send_keys("enter_your_id")
		driver.find_element_by_css_selector("span.RveJvd.snByac").click()
		time.sleep(3)
		driver.find_element_by_name("password").clear()
		driver.find_element_by_name("password").send_keys("enter_your_password")
		time.sleep(3)
		driver.find_element_by_css_selector("span.RveJvd.snByac").click()
		time.sleep(20)
		

		pdb.set_trace()
		driver.get('https://analytics.google.com/analytics/web/?pli=1#my-reports/okly0HRzQz6aOGh4JNqGOw/a29059432w55026993p56011011/%3F_u.date00%3D20170613%26_u.date01%3D20170613/')
		time.sleep(12)
		driver.find_element_by_css_selector('._GAPj').click()
		month_1_selector = driver.find_element_by_css_selector('td._GAb-_GAt-_GAC:nth-child(2) > table:nth-child(1)')
		month_2_selector = driver.find_element_by_css_selector('td._GAb-_GAt-_GAC:nth-child(3) > table:nth-child(1)')
		month_3_selector = driver.find_element_by_css_selector('td._GAb-_GAt-_GAC:nth-child(4) > table:nth-child(1)')
		if(month_3_selector.find_element_by_tag_name('button').text.encode('utf-8') == month):
			month_3_selector.find_element_by_xpath('.//td[text()="'+str(date1)+'"]').click()
			driver.find_element_by_css_selector('.ID-apply').click()
		elif(month_2_selector.find_element_by_tag_name('button').text == month):
			month_2_selector.find_element_by_xpath('.//td[text()="'+str(date1)+'"]').click()
			driver.find_element_by_css_selector('.ID-apply').click()
		else:
			month_1_selector.find_element_by_xpath('.//td[text()="'+str(date1)+'"]').click()
			driver.find_element_by_css_selector('.ID-apply').click()
		time.sleep(10)
		text =  driver.find_element_by_css_selector('.C_PAGINATION_ROWS_LONG > label:nth-child(3)').text
		text = text.encode('utf-8')
		int_list = [int(s) for s in text.split() if s.isdigit()]
		select = Select(driver.find_element_by_css_selector('.ACTION-toggleRowShow'))
#		val_options = [x for x in val_par.find_elements_by_tag_name('option')]
		all_options = [int(o.get_attribute('value')) for o in select.options if int(o.get_attribute('value')) > int_list[-1]]
		select.select_by_value(str(all_options[0]))
		time.sleep(10)
		driver.refresh()
		time.sleep(15)
		driver.find_element_by_css_selector('._GAMt').click()
		driver.find_element_by_css_selector('li.ACTION-export:nth-child(4) > span:nth-child(2)').click()
		time.sleep(10)
		

		pdb.set_trace()
		driver.get('https://analytics.google.com/analytics/web/?pli=1#my-reports/ccjxpIE7TDms3T240YGLGQ/a29059432w126754222p130373335/%3F_u.date00%3D20170613%26_u.date01%3D20170613/')
		time.sleep(10)
		driver.find_element_by_css_selector('._GAPj').click()
		month_1_selector = driver.find_element_by_css_selector('td._GAb-_GAt-_GAC:nth-child(2) > table:nth-child(1)')
		month_2_selector = driver.find_element_by_css_selector('td._GAb-_GAt-_GAC:nth-child(3) > table:nth-child(1)')
		month_3_selector = driver.find_element_by_css_selector('td._GAb-_GAt-_GAC:nth-child(4) > table:nth-child(1)')
		if(month_3_selector.find_element_by_tag_name('button').text.encode('utf-8') == month):
			month_3_selector.find_element_by_xpath('.//td[text()="'+str(date1)+'"]').click()
			driver.find_element_by_css_selector('.ID-apply').click()
		elif(month_2_selector.find_element_by_tag_name('button').text == month):
			month_2_selector.find_element_by_xpath('.//td[text()="'+str(date1)+'"]').click()
			driver.find_element_by_css_selector('.ID-apply').click()
		else:
			month_1_selector.find_element_by_xpath('.//td[text()="'+str(date1)+'"]').click()
			driver.find_element_by_css_selector('.ID-apply').click()
		time.sleep(10)
		text =  driver.find_element_by_css_selector('.C_PAGINATION_ROWS_LONG > label:nth-child(3)').text
		text = text.encode('utf-8')
		int_list = [int(s) for s in text.split() if s.isdigit()]
		select = Select(driver.find_element_by_css_selector('.ACTION-toggleRowShow'))
		all_options = [int(o.get_attribute('value')) for o in select.options if int(o.get_attribute('value')) > int_list[-1]]
		select.select_by_value(str(all_options[0]))
		time.sleep(10)
		driver.refresh()
		time.sleep(15)
		driver.find_element_by_css_selector('._GAMt').click()
		driver.find_element_by_css_selector('li.ACTION-export:nth-child(4) > span:nth-child(2)').click()
		time.sleep(10)

		pdb.set_trace()
		driver.get('https://analytics.google.com/analytics/web/?pli=1#my-reports/NfSvT5HBQYmyWZQkmj9EnA/a29059432w128671062p132428766/%3F_u.date00%3D20170613%26_u.date01%3D20170613/')
		time.sleep(10)
		driver.find_element_by_css_selector('._GAPj').click()
		month_1_selector = driver.find_element_by_css_selector('td._GAb-_GAt-_GAC:nth-child(2) > table:nth-child(1)')
		month_2_selector = driver.find_element_by_css_selector('td._GAb-_GAt-_GAC:nth-child(3) > table:nth-child(1)')
		month_3_selector = driver.find_element_by_css_selector('td._GAb-_GAt-_GAC:nth-child(4) > table:nth-child(1)')
		if(month_3_selector.find_element_by_tag_name('button').text.encode('utf-8') == month):
			month_3_selector.find_element_by_xpath('.//td[text()="'+str(date1)+'"]').click()
			driver.find_element_by_css_selector('.ID-apply').click()
		elif(month_2_selector.find_element_by_tag_name('button').text == month):
			month_2_selector.find_element_by_xpath('.//td[text()="'+str(date1)+'"]').click()
			driver.find_element_by_css_selector('.ID-apply').click()
		else:
			month_1_selector.find_element_by_xpath('.//td[text()="'+str(date1)+'"]').click()
			driver.find_element_by_css_selector('.ID-apply').click()
		text =  driver.find_element_by_css_selector('.C_PAGINATION_ROWS_LONG > label:nth-child(3)').text
		text = text.encode('utf-8')
		int_list = [int(s) for s in text.split() if s.isdigit()]
		select = Select(driver.find_element_by_css_selector('.ACTION-toggleRowShow'))
		all_options = [int(o.get_attribute('value')) for o in select.options if int(o.get_attribute('value')) > int_list[-1]]
		select.select_by_value(str(all_options[0]))
		time.sleep(10)
		driver.refresh()
		time.sleep(15)
		driver.find_element_by_css_selector('._GAMt').click()
		driver.find_element_by_css_selector('li.ACTION-export:nth-child(4) > span:nth-child(2)').click()
		time.sleep(10)

		pdb.set_trace()
		driver.get('https://analytics.google.com/analytics/web/?pli=1#my-reports/jqSzj-ExQM65Yh1pAim8IQ/a29059432w128700432p132453658/%3F_u.date00%3D20170613%26_u.date01%3D20170613/')
		time.sleep(10)
		driver.find_element_by_css_selector('._GAPj').click()
		month_1_selector = driver.find_element_by_css_selector('td._GAb-_GAt-_GAC:nth-child(2) > table:nth-child(1)')
		month_2_selector = driver.find_element_by_css_selector('td._GAb-_GAt-_GAC:nth-child(3) > table:nth-child(1)')
		month_3_selector = driver.find_element_by_css_selector('td._GAb-_GAt-_GAC:nth-child(4) > table:nth-child(1)')
		if(month_3_selector.find_element_by_tag_name('button').text.encode('utf-8') == month):
			month_3_selector.find_element_by_xpath('.//td[text()="'+str(date1)+'"]').click()
			driver.find_element_by_css_selector('.ID-apply').click()
		elif(month_2_selector.find_element_by_tag_name('button').text == month):
			month_2_selector.find_element_by_xpath('.//td[text()="'+str(date1)+'"]').click()
			driver.find_element_by_css_selector('.ID-apply').click()
		else:
			month_1_selector.find_element_by_xpath('.//td[text()="'+str(date1)+'"]').click()
			driver.find_element_by_css_selector('.ID-apply').click()
		text =  driver.find_element_by_css_selector('.C_PAGINATION_ROWS_LONG > label:nth-child(3)').text
		text = text.encode('utf-8')
		int_list = [int(s) for s in text.split() if s.isdigit()]
		select = Select(driver.find_element_by_css_selector('.ACTION-toggleRowShow'))
		all_options = [int(o.get_attribute('value')) for o in select.options if int(o.get_attribute('value')) > int_list[-1]]
		select.select_by_value(str(all_options[0]))
		time.sleep(10)
		driver.refresh()
		time.sleep(15)
		driver.find_element_by_css_selector('._GAMt').click()
		driver.find_element_by_css_selector('li.ACTION-export:nth-child(4) > span:nth-child(2)').click()
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