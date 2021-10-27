"""
Module that will launch browser to automate pickups.

TODO: Modularity

Author: Christian M. Fulton
Date: 15.Oct.2021
"""
import datetime, os
from urllib.request import urlopen
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import creds as CREDS


def execute():
	"""
	Executes the application
	"""
	try:
	#### This code can be modularized ####
		driver = webdriver.Chrome(executable_path='/usr/lib/chromium-browser/chromedriver')
		driver.get('https://www.etsy.com/your/shops/me/dashboard?ref=hdr-mcpa')
		driver.implicitly_wait(15)

		email_in = driver.find_element(By.XPATH, value='//*[@id="join_neu_email_field"]')
		email_in.send_keys(CREDS.UNAME)
		pwd_in = driver.find_element(By.XPATH, value='//*[@id="join_neu_password_field"]')
		pwd_in.send_keys(CREDS.PWD + '\ue007')

		orders_btn = driver.find_element(By.XPATH, value='//*[@id="root"]/div/div[1]/div[3]/div/div[1]/div[2]/ul/li[5]/a')
		orders_btn.click()

		order_qty = driver.find_element(By.XPATH, value='//*[@id="browse-view"]/div/div[1]/div[2]/nav/ul/li[1]/a/span[2]').text
		
		# check for any new orders
		if int(order_qty) > 0:
			pickup()
	except:
		print('Something went wrong...')
		driver.quit()


	driver.quit()

def pickup():
	"""
	execute if there is a new order.

	Probably more efficient to just open new tab...make work...Refactor later
	"""
	driver = webdriver.Chrome()
	driver.get('https://www.usps.com')

	sign_in = driver.find_element(By.XPATH, value='//*[@id="login-register-header"]')
	sign_in.click()

	uname = driver.find_element(By.XPATH, value='//*[@id="username"]')
	uname.send_keys(CREDS.USPS_NAME)

	pwd = driver.find_element(By.XPATH, value='//*[@id="password"]')
	pwd.send_keys(CREDS.USPS_NAME + '\ue007')

	# find pickup
	pickup_btn = driver.find_element(By.XPATH, value='/html/body/div[2]/div/nav/ul/li[2]/div/ul[1]/li[5]/a')
	pickup_btn.click()

	avail_btn = driver.find_element(By.XPATH, value='//*[@id="webToolsAddressCheck"]')
	avail_btn.click()

	loc_drp = driver.find_element(By.XPATH, value='//*[@id="packageLocation"]')
	loc_drp.click()

	#### NEED TO VERIFY PATH ####
	fdoor = driver.find_element(By.XPATH, value='/html/body/div[5]/div/div/div[6]/div[1]/div/select/option[4]')
	fdoor.click()

	reg_radio = driver.find_element(By.XPATH, value='//*[@id="pickup-regular-time"]')
	reg_radio.click()

	# anticipate next day will have to use datetime.now
	# avoid calendar by using 'recurring pickup tool'(start/stop same day)
	pu_tool = driver.find_element(By.XPATH, value='/html/body/div[6]/div/div/div[4]/div[4]/div[4]/div[1]/h4')
	pu_tool.click()

	start_date = driver.find_element(By.XPATH, value='//*[@id="recurring-pickup-tool-start-date-cal"]')
	start_date.send_keys()

	today = datetime.date.today()


	# TODO: log scheduled pickup for verification

	driver.quit()