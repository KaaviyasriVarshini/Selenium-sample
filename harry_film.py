from selenium import webdriver
import time



PATH = "/home/sanjju/Downloads/chromedriver_linux64/chromedriver"
driver = webdriver.Chrome(PATH)

def startpy():

    URL = "https://en.wikipedia.org/wiki/Harry_Potter_(film_series)"

    driver.get(URL)
    driver.maximize_window()
    time.sleep(5)
    harry_potter = { }

    for i in range(2, 10):
    
        year = driver.find_element_by_xpath(f'//*[@id="mw-content-text"]/div[1]/table[2]/tbody/tr[{i}]/td[1]')
        print(year.text)
        film = driver.find_element_by_xpath(f'//*[@id="mw-content-text"]/div[1]/table[2]/tbody/tr[{i}]/td[2]')
        print(film.text)
        harry_potter[year.text] = film.text
    print(harry_potter)



startpy()









