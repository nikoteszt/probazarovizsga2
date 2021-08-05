from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

import time


options = Options()
options.headless = False
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

driver.get('https://witty-hill-0acfceb03.azurestaticapps.net/charterbooker.html')

# Megnézzük megfelelő oldalon vagyunk e.
first_question = driver.find_element_by_xpath('//*[@id="step1"]/ul/li[1]/label')
print(first_question.is_displayed())
print(first_question.text)

# Kérdések megválaszolása, és továbblépés.
many_guest = driver.find_element_by_tag_name("select")
many_guest.click()
select_row = driver.find_element_by_xpath('//*[@id="step1"]/ul/li[1]/select/option[6]')
select_row.click()
time.sleep(2)
first_next_button = driver.find_element_by_class_name("next-btn1")
first_next_button.click()

time.sleep(1)
# Megnézzük megfelelő oldalon vagyunk e.
second_queston = driver.find_element_by_xpath('//*[@id="step2"]/ul/li[1]/label')
print(second_queston.is_displayed())
print(second_queston.text)

# Kérdések megválaszolása, és továbblépés.
date_time = driver.find_element_by_xpath('//*[@id="step2"]/ul/li[1]/input')
date_time.send_keys('20210808')
time_day = driver.find_element_by_xpath('//*[@id="step2"]/ul/li[2]/select')
time_day_row = driver.find_element_by_xpath('//*[@id="step2"]/ul/li[2]/select/option[3]')
time_day_row.click()
many_hours = driver.find_element_by_xpath('//*[@id="step2"]/ul/li[3]/select')
many_hours.click()
many_hours_row = driver.find_element_by_xpath('//*[@id="step2"]/ul/li[3]/select/option[7]')
many_hours_row.click()
time.sleep(2)
second_next_button = driver.find_element_by_class_name("next-btn2")
second_next_button.click()

time.sleep(1)
# Megnézzük megfelelő oldalon vagyunk e.
third_page_question = driver.find_element_by_xpath('//*[@id="step3"]/ul/li[1]/label')
print(third_page_question.is_displayed())
print(third_page_question.text)

# Kérdések megválaszolása, és továbblépés.
your_name = driver.find_element_by_xpath('//*[@id="step3"]/ul/li[1]/input')
your_name.send_keys("Proba Karesz")
your_email = driver.find_element_by_xpath('//*[@id="step3"]/ul/li[2]/input')
# Email cim validáció ellenőrzése
your_email.send_keys("pkaresz")
your_message = driver.find_element_by_xpath('//*[@id="step3"]/ul/li[3]/textarea')
your_message.send_keys("None")
time.sleep(2)
assert driver.find_element_by_id("bf_email-error").text == "PLEASE ENTER A VALID EMAIL ADDRESS."
your_email.send_keys("pkaresz@valami.hu")

time.sleep(2)
submit_button = driver.find_element_by_class_name("submit-btn")
submit_button.click()

time.sleep(4)
# Ellenőrizzük a helyes kitöltésre adott választ
last_message = driver.find_element_by_tag_name("h2").text
assert last_message == "Your message was sent successfully. " \
                       "Thanks! We'll be in touch as soon as we can, which is usually like lightning " \
                       "(Unless we're sailing or eating tacos!)."


time.sleep(4)
driver.close()
driver.quit()
