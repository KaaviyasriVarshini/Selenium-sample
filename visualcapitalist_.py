from selenium import webdriver
import pandas as pd


PATH = "/home/sanjju/Downloads/chromedriver_linux64/chromedriver"
driver = webdriver.Chrome(PATH)


def startpy():

    INFO = []

    URL = "https://www.visualcapitalist.com/cp/ranked-the-best-selling-video-game-consoles-of-all-time/"
    driver.get(URL)
    driver.maximize_window()
    

    def visualcapitalist(n):
        for i in range(1, n):

            DATA = {}

            rank = driver.find_element_by_xpath(f'//*[@id="tablepress-2347"]/tbody/tr[{i}]/td[1]')
            print(rank.text)
            console = driver.find_element_by_xpath(f'//*[@id="tablepress-2347"]/tbody/tr[{i}]/td[2]')
            print(console.text)
            manufacturer = driver.find_element_by_xpath(f'//*[@id="tablepress-2347"]/tbody/tr[{i}]/td[3]')
            print(manufacturer.text)
            global_lifetime_sales = driver.find_element_by_xpath(f'//*[@id="tablepress-2347"]/tbody/tr[{i}]/td[4]')
            print(global_lifetime_sales.text)


        

            DATA["RANK"] = [rank.text]
            DATA["CONSOLE"] = [console.text]
            DATA["manufacturer"] = [manufacturer.text]
            DATA["global_lifetime"] = [global_lifetime_sales.text]
            INFO.append(DATA)

            df = pd.DataFrame.from_dict(INFO)
            df.to_csv("data.csv", index = False, header = True)



    visualcapitalist(11)
    next = driver.find_element_by_xpath('//*[@id="tablepress-2347_next"]')
    next.click()
    visualcapitalist(11)
    next_1 = driver.find_element_by_xpath('//*[@id="tablepress-2347_next"]')
    next_1.click()
    visualcapitalist(9)
                
        


    # if (next.click() != None):
    
    


startpy()


# //*[@id="tablepress-2347"]/tbody/tr[1]/td[2]
# //*[@id="tablepress-2347"]/tbody/tr[1]/td[2]



























































































































































































































































































































