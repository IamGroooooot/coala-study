from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import re

driver = webdriver.Chrome("./chromedriver")
driver.get("https://nid.naver.com/")
id_input = driver.find_element_by_css_selector("#id")
id_input.send_keys("kojuh98")
password = driver.find_element_by_css_selector("#pw")
password.send_keys("1234")
checkbox = driver.find_element_by_css_selector("#label_login_chk")
checkbox.click()
