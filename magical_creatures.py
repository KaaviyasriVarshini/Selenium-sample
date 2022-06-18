from selenium import webdriver
import time



PATH = "/home/sanjju/Downloads/chromedriver_linux64/chromedriver"
driver = webdriver.Chrome(PATH)

def startpy():

    URL = "https://wizardingworldz.com/harry-potter-creatures-list/"

    driver.get(URL)
    driver.maximize_window()
    time.sleep(2)


    for i in range(1, 21):
        magical_creatures = driver.find_element_by_xpath(f'//*[@id="tps_slideContainer_500"]/div/h2[{i}]')
        print(magical_creatures.text)
        


startpy()








