from selenium import webdriver
import time



PATH = "/home/sanjju/Downloads/chromedriver_linux64/chromedriver"
driver = webdriver.Chrome(PATH)

def startpy():

    URL = "https://wizardinghome.com/harry-potter-spells-list-a-z/"

    driver.get(URL)
    driver.maximize_window()
    time.sleep(2)


    for i in range(2, 31):
        spells = driver.find_element_by_xpath(f'//*[@id="post-110"]/div/div/p[{i}]/strong')
        print(spells.text)
        effect = driver.find_element_by_xpath(f'//*[@id="post-110"]/div/div/p[{i}]/text()[2]')
        print(effect.text)




startpy()











