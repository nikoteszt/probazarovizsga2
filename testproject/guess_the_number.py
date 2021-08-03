from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random

options = Options()
options.headless = False
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

driver.get('https://witty-hill-0acfceb03.azurestaticapps.net/guess_the_number.html')

input_number = driver.find_element_by_tag_name("input")
number_send = driver.find_element_by_xpath('//span/button')
input_number.click()
tipp = random.randint(1, 100)
input_number.send_keys(tipp)
number_send.click()

n_guess = driver.find_element_by_xpath('//p/span').text
print(n_guess)
