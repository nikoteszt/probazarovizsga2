from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
# from selenium.webdriver import ActionChains
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import time
import random

options = Options()
options.headless = False
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

driver.get('https://witty-hill-0acfceb03.azurestaticapps.net/guess_the_number.html')

input_number = driver.find_element_by_tag_name("input")
number_send = driver.find_element_by_xpath('//span/button')

minN = 1
maxN = 100
testN = 0
n_guess = "0"

try:
    while True:
        tipp = random.randint(minN, maxN)
        input_number.clear()
        input_number.send_keys(tipp)
        number_send.click()
        testN += 1
        n_guess = driver.find_element_by_xpath('//p/span').text
#        print(n_guess)
        guess_answer = driver.find_element_by_xpath('//p[@class="alert alert-warning"]')
#        print(guess_answer.text)

        if guess_answer.text == "Guess lower.":
            maxN = tipp
        elif guess_answer.text == "Guess higher.":
            minN = tipp
        else:
            break


except NoSuchElementException:
    print("Saját belső számlálónk állása:", testN)
    print("Applikáció számlálójának állása:", n_guess)
    if testN == int(n_guess):
        print("A két számláló megegyezik.")
    else:
        print("A két számláló különbözik.")


finally:
    pass
