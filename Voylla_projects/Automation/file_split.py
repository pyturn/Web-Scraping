import pandas as pd
import pdb,os,math,time
from selenium import webdriver
pdb.set_trace()
files_1 = os.listdir(os.getcwd())
files = [i for i in files_1 if i.endswith('csv')]
for file in files:
	df = pd.read_csv(file)
	no_of_files = int(math.ceil(df.shape[0]/20.0))
	pdb.set_trace()
	for i in range(no_of_files):
		file_name = file+str(i+1)+".csv"
		df1 = df[:20]
		df1.to_csv(file_name,index=False)
		df = df[20:]
	driver = webdriver.Firefox(executable_path = 'C:\Users\Voylla.RTO-CR\Downloads\geckodriver-v0.18.0-win64\geckodriver.exe')
	driver.implicitly_wait(30)
	base_url = "https://pos-mumbai.voylla.com"
	driver.get(base_url + "/")
	driver.find_element_by_id("login").clear()
	driver.find_element_by_id("login").send_keys('ENTER_YOUR_KEYS')
	driver.find_element_by_id("password").clear()
	driver.find_element_by_id("password").send_keys('ENTER_YOUR_PASSWORD')
	driver.find_element_by_css_selector('button.btn').click()
	time.sleep(10)
	driver.get('https://pos-mumbai.voylla.com/web#view_type=form&model=pos.session.opening&menu_id=313&action=386')
	time.sleep(10)
	def is_alert_present(self):
		try: self.driver.switch_to_alert()
		except NoAlertPresentException as e: return False
		return True
	for j in range(no_of_files):
		path_file = "C:\Users\Voylla.RTO-CR\Desktop\\Testing\\"+file+str(j+1)+".csv"
		path_success = "C:\Users\Voylla.RTO-CR\Desktop\\Testing\\Success\\"+file+str(j+1)+".csv"
		path_failure = "C:\Users\Voylla.RTO-CR\Desktop\\Testing\\Failure\\"+file+str(j+1)+".csv" 
		driver.find_element_by_css_selector('div.oe_secondary_menu:nth-child(2) > ul:nth-child(10) > li:nth-child(1) > a:nth-child(1) > span:nth-child(1)').click()
		time.sleep(3)
		driver.find_element_by_css_selector('.oe_form_binary_file').send_keys("C:\Users\Voylla.RTO-CR\Desktop\\Testing\\"+file+str(j+1)+".csv")
		time.sleep(3)
		driver.find_element_by_css_selector('button.oe_form_button:nth-child(1)').click()
		time.sleep(90)
		if(is_alert_present):
			os.rename(path_file,path_success)
			continue
		else:
			os.rename(path_file,path_failure)
			continue
	driver.quit()
	
		
