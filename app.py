"""
Module that will launch browser to automate pickups.

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
from .creds import UNAME, PWD


def execute():
	"""
	Executes the application
	"""
	driver = webdriver.Chrome()
	driver.get("https://www.etsy.com")
	driver.implicitly_wait(15)
	# locate login
	sign_in = driver.find_element(By.XPATH, value='/html/body/div[3]/header/div[4]/nav/ul/li[1]/button')
	sign_in.click()
	# locate input
	email_in = driver.find_element(By.XPATH, value='//*[@id="join_neu_email_field"]')
	email_in.send_keys(UNAME)
	pwd_in = driver.find_element(By.XPATH, value='//*[@id="join_neu_password_field"]')
	pwd_in.send_keys(PWD + '\ue007')

	# locate shop button
	shop_btn = driver.find_element(By.XPATH, value='/html/body/div[3]/header/div[4]/nav/ul/li[2]/span/a/span[1]/svg')
	shop_btn.click()

	# find sales tab
	orders_btn = driver.find_element(By.XPATH, value='/html/body/div[4]/div/div[1]/div/div[1]/div[3]/div/div[1]/div[2]/ul/li[5]/a/div/div[2]/span')
	orders_btn.click()

	order_qty = driver.find_element(By.XPATH, value='/html/body/div[4]/div/div[1]/div/div[3]/div/div[3]/div/div/div[1]/div[2]/nav/ul/li[1]/a/span[2]').text


	driver.quit()