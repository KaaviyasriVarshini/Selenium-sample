from selenium import webdriver
import time
import pandas as pd



PATH = "/home/sanjju/Downloads/chromedriver_linux64/chromedriver"
driver = webdriver.Chrome(PATH)

def startpy():

    _HARRY_POTTER_ = []

    URL = "https://en.wikipedia.org/wiki/Harry_Potter_(film_series)"

    driver.get(URL)
    driver.maximize_window()
    time.sleep(5)
    

    for i in range(2, 10):
        
        harry_potter = {}
    
        year = driver.find_element_by_xpath(f'//*[@id="mw-content-text"]/div[1]/table[2]/tbody/tr[{i}]/td[1]')
        print(year.text)
        film = driver.find_element_by_xpath(f'//*[@id="mw-content-text"]/div[1]/table[2]/tbody/tr[{i}]/td[2]')
        print(film.text)

        harry_potter["Year"] = [year.text]
        harry_potter["Film"] = [film.text]
        _HARRY_POTTER_.append(harry_potter)

        df = pd.DataFrame.from_dict(_HARRY_POTTER_)
        df.to_csv("._.Harry Potter._.csv", index = False, header = True)


    #     harry_potter[year.text] = film.text
    # print(harry_potter)



startpy()









