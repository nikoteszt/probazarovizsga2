from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

options = Options()
options.headless = False
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

driver.get("https://witty-hill-0acfceb03.azurestaticapps.net/film_register.html")

time.sleep(2)  # várakozás, hogy elkezdjenek az elemek megjelenni az oldalon
movie_list = WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located((By.CLASS_NAME, 'container-movies')))
# A 24 db film megjelenésének ellenőrzése az alkalmazásban.
assert len(movie_list) == 24

# Lenyitjuk a regisztrációs panelt.
register_button = driver.find_element_by_tag_name("button")
if register_button.text == "Register":
    register_button.click()
else:
    print("Regisztráció nem müködik.")

film_cim = driver.find_element_by_id("nomeFilme")
driver.execute_script("arguments[0].click();", film_cim)
driver.execute_script("arguments[0].send_keys('Black widow');", film_cim)
# driver.find_element_by_id("anoLancamentoFilme").click().send_keys('2021')
# driver.find_element_by_id("anoCronologiaFilme").click().send_keys('2020')

