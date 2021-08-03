from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

options = Options()
options.headless = False
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

driver.get('https://witty-hill-0acfceb03.azurestaticapps.net/mutant_teams.html')

radio_input = driver.find_elements_by_tag_name("input")
characters = driver.find_elements_by_tag_name("li")
for i in radio_input:
    print(i.get_attribute("id"))
    for j in characters:
        print(j.find_element_by_tag_name('h2').text)
    i.get_attribute("type").value("radio").click()


# //ul[@class="characters"]/li