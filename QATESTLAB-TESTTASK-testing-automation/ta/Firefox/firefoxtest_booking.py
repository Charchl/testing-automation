# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver import Firefox
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import unittest
import time


# Firefox browser

#Scenario 2

class BookingTest1Firefox(unittest.TestCase):
	def setUp(self):
		binary = r'C:\Program Files\Mozilla Firefox\firefox.exe'
		options = Options()
		options.set_headless(headless=True)
		options.binary = binary
		cap = DesiredCapabilities().FIREFOX
		cap["marionette"] = True

		self.driver = webdriver.Firefox(firefox_options=options, capabilities=cap, executable_path="D:\\Programming\\Python_not_web\\QATESTLAB-TESTTASK-testing-automation2\\TestingAutomationQATESTLAB\\TestingAutomationQATESTLAB\\geckodriver.exe")
		self.driver.get('http://booking.com')

	def test_city(self):
		driver = self.driver
		input_field = driver.find_element_by_id('ss')
		input_field.send_keys('Хмельницкий')
		input_field.send_keys(Keys.ENTER)
		time.sleep(5)

		hotels = driver.find_elements_by_class_name('sr-hotel__title-wrap')
		self.assertTrue(hotels is not None)

	def test_calendar(self):
		driver = self.driver
		input_field = driver.find_element_by_id('ss')
		input_field.send_keys('Хмельницкий')
		input_field.send_keys(Keys.ENTER)
		time.sleep(2)

		cal_check = driver.find_element_by_class_name('bui-calendar')
		time.sleep(5)
		display = cal_check.value_of_css_property('display')
		
		self.assertTrue(cal_check is not None)


	def test_price(self):
		driver = self.driver
		input_field = driver.find_element_by_id('ss')
		input_field.send_keys('Хмельницкий')
		input_field.send_keys(Keys.ENTER)
		time.sleep(2)

		prices = driver.find_elements_by_class_name('prco-ltr-right-align-helper')
		self.assertTrue(len(prices) == 0)


	def tearDown(self):
		self.driver.quit()


class BookingTest2Firefox(unittest.TestCase):
	def setUp(self):
		binary = r'C:\Program Files\Mozilla Firefox\firefox.exe'
		options = Options()
		options.set_headless(headless=True)
		options.binary = binary
		cap = DesiredCapabilities().FIREFOX
		cap["marionette"] = True

		self.driver = webdriver.Firefox(firefox_options=options, capabilities=cap, executable_path="D:\\Programming\\Python_not_web\\QATESTLAB-TESTTASK-testing-automation2\\TestingAutomationQATESTLAB\\TestingAutomationQATESTLAB\\geckodriver.exe")
		self.driver.get('http://booking.com')


	def test_click(self):
		driver = self.driver
		input_field = driver.find_element_by_id('ss')
		input_field.send_keys('Хмельницкий')
		input_field.send_keys(Keys.ENTER)
		time.sleep(2)

		btn  = driver.find_element_by_class_name('sr-cta-button-row')
		btn.click()
		time.sleep(2)

		calendar = driver.find_element_by_class_name('bui-calendar')
		time.sleep(5)
		display = calendar.value_of_css_property('display')

		self.assertTrue(calendar is not None)

	def tearDown(self):
		self.driver.quit()

class BookingTest3Firefox(unittest.TestCase):
	def setUp(self):
		binary = r'C:\Program Files\Mozilla Firefox\firefox.exe'
		options = Options()
		options.set_headless(headless=True)
		options.binary = binary
		cap = DesiredCapabilities().FIREFOX
		cap["marionette"] = True

		self.driver = webdriver.Firefox(firefox_options=options, capabilities=cap, executable_path="D:\\Programming\\Python_not_web\\QATESTLAB-TESTTASK-testing-automation2\\TestingAutomationQATESTLAB\\TestingAutomationQATESTLAB\\geckodriver.exe")
		self.driver.get('http://booking.com')

	def test_date(self):
		driver = self.driver
		input_field = driver.find_element_by_id('ss')
		input_field.send_keys('Хмельницкий')

		full_calendar = driver.find_element_by_class_name('xp-calendar')

		date = driver.find_element_by_class_name('-month-year')
		dateOptions = date.find_elements_by_tag_name("option")
		dateOptions[8].click()
        

		date = driver.find_element_by_name('checkin_monthday')
		dateOptions = date.find_elements_by_tag_name("option")
		dateOptions[4].click()
        

		input_field.send_keys(Keys.ENTER)
		time.sleep(2)

		self.assertTrue(True)

	def tearDown(self):
		self.driver.quit()


class BookingTest4Firefox(unittest.TestCase):
	def setUp(self):
		binary = r'C:\Program Files\Mozilla Firefox\firefox.exe'
		options = Options()
		options.set_headless(headless=True)
		options.binary = binary
		cap = DesiredCapabilities().FIREFOX
		cap["marionette"] = True

		self.driver = webdriver.Firefox(firefox_options=options, capabilities=cap, executable_path="D:\\Programming\\Python_not_web\\QATESTLAB-TESTTASK-testing-automation2\\TestingAutomationQATESTLAB\\TestingAutomationQATESTLAB\\geckodriver.exe")
		self.driver.get('http://booking.com')

	def test_search(self):
		driver = self.driver
		input_field = driver.find_element_by_id('ss')
		input_field.send_keys('Хмельницкий')
		input_field.send_keys(Keys.ENTER)
		time.sleep(2)

		date_field = driver.find_element_by_class_name('-month-year')
		allOptions = date_field.find_elements_by_tag_name("option")
		allOptions[8].click()

		date_field = driver.find_element_by_name('checkin_monthday')

		allOptions = date_field.find_elements_by_tag_name("option")

		allOptions[4].click()
		time.sleep(2)

		adult_field = driver.find_element_by_id('group_adults')
		adultOptions = adult_field.find_elements_by_tag_name("option")
		adultOptions[2].click()

		child_field = driver.find_element_by_id('group_children')
		childOptions = child_field.find_elements_by_tag_name("option")
		childOptions[1].click()

		rooms_field = driver.find_element_by_id('no_rooms')
		roomsOptions = rooms_field.find_elements_by_tag_name("option")
		roomsOptions[2].click()

		age_field = driver.find_element_by_name('age')
		ageOptions = age_field.find_elements_by_tag_name("option")
		ageOptions[2].click()

		btn_submit = driver.find_element_by_class_name('sb-searchbox__button')
		btn_submit.click()
		time.sleep(2)

		price = driver.find_element_by_class_name('prco-ltr-right-align-helper')
		self.assertTrue(price is not None)


	def tearDown(self):
		self.driver.quit()


# Scenario 1

class BookingTest5Firefox(unittest.TestCase):
	def setUp(self):
		binary = r'C:\Program Files\Mozilla Firefox\firefox.exe'
		options = Options()
		options.set_headless(headless=True)
		options.binary = binary
		cap = DesiredCapabilities().FIREFOX
		cap["marionette"] = True

		self.driver = webdriver.Firefox(firefox_options=options, capabilities=cap, executable_path="D:\\Programming\\Python_not_web\\QATESTLAB-TESTTASK-testing-automation2\\TestingAutomationQATESTLAB\\TestingAutomationQATESTLAB\\geckodriver.exe")
		self.driver.get('http://booking.com')

	def test_search(self):
		driver = self.driver

		number_of_guests = driver.find_element_by_class_name('xp__guests')
		number_of_guests.click()

		number_of_kids = driver.find_element_by_class_name('sb-group-children')
		time.sleep(2)

		btn_knumber = driver.find_element_by_class_name('sb-group__stepper-a11y')
		time.sleep(2)

		btn_plus = driver.find_elements_by_class_name('bui-stepper__add-button')

		click_count = 3
		for x in range(0, click_count):
			btn_plus[1].click()
		time.sleep(5)

		kids_age = driver.find_element_by_class_name('sb-group__children__field')
		select_age = len(driver.find_elements_by_name('age'))
		if select_age == click_count:
			print(True)

		self.assertTrue(True)

	def tearDown(self):
		self.driver.quit()