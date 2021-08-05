from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

import time


options = Options()
options.headless = False
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

driver.get("https://witty-hill-0acfceb03.azurestaticapps.net/periodic_table.html")

try:
    # Lementjük az elemeket a periodusos táblából a rendszámuk sorrendjében.
    elements = driver.find_elements_by_xpath('//li[@data-pos]')
    # Ez sajnos nem jó, mert a táblázat hibás, az utolsó 4 elemnek azonos a rendszáma.
    # elements_dict = {}
    # for i in range(len(elements)):
    #     elements_dict[elements[i].get_attribute("data-pos")] = elements[i].find_element_by_tag_name("span").text
    #     print()
    #     print(elements[i].get_attribute("data-pos"))
    #     print(elements[i].find_element_by_tag_name("span").text)
    # print()
    # print(elements_dict)

    elements_list = []
    for i in range(len(elements)):
        elements_list.append(elements[i].find_element_by_tag_name("span").text)

    # Beolvassuk az elemeket a data.txt-ből sorban.
    elements_datatxt = []
    with open('data.txt', encoding="utf-8") as datafile:
        for row in datafile:
            elements_tmp = row.strip()
            elements_datatxt.append(elements_tmp.strip(' ,-0123456789'))

    # Összehasonlítjuk a két listát, hogy azonosak lettek e.
    assert elements_list == elements_datatxt
    print("Az elemek listája megegyezik, a megjelenési sorrend megfelelő.")

except AssertionError:
    print("Hiba történt, az elemek listája nem egyezik meg, a megjelenési sorrend NEM megfelelő.")

finally:
    time.sleep(3)
    driver.close()
    driver.quit()
