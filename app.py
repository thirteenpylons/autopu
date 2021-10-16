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


def execute():
	"""
	Executes the application
	"""
	driver = webdriver.Chrome()
	driver.get("https://www.etsy.com")
	driver.implicitly_wait(15)


	driver.quit()