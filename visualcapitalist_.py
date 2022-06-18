from selenium import webdriver
import pandas as pd


PATH = "/home/sanjju/Downloads/chromedriver_linux64/chromedriver"
driver = webdriver.Chrome(PATH)


def startpy():

    


    driver.get("https://www.visualcapitalist.com/cp/ranked-the-best-selling-video-game-consoles-of-all-time/")
    # driver.maximize_window()
    # def write_csv(a, b,c, d):
    #     file = open("data.csv","w")
    #     data = {
    #          "Rank" : a,
    #          "Console" : b,
    #          "Manufacturer" : c,
    #          "Global lifetime sales" : d
    #         }
        
    #     df = pd.DataFrame([data])
    #     df.to_csv("data.csv")


    def visualcapitalist(n):
        for i in range(1, n):
            rank = driver.find_element_by_xpath(f'//*[@id="tablepress-2347"]/tbody/tr[{i}]/td[1]')
            print(rank.text)
            console = driver.find_element_by_xpath(f'//*[@id="tablepress-2347"]/tbody/tr[{i}]/td[2]')
            print(console.text)
            manufacturer = driver.find_element_by_xpath(f'//*[@id="tablepress-2347"]/tbody/tr[{i}]/td[3]')
            print(manufacturer.text)
            global_lifetime_sales = driver.find_element_by_xpath(f'//*[@id="tablepress-2347"]/tbody/tr[{i}]/td[4]')
            print(global_lifetime_sales.text)

        def write_csv(a, b,c, d):
            # file = open("data.csv","x")
            data = {
                "Rank" : a,
                "Console" : b,
                "Manufacturer" : c,
                "Global lifetime sales" : d
                }
            
            df = pd.DataFrame([data])
            df.to_csv("data.csv")



            visualcapitalist(11)
            next = driver.find_element_by_xpath('//*[@id="tablepress-2347_next"]')
            next.click()
            visualcapitalist(11)
            next_1 = driver.find_element_by_xpath('//*[@id="tablepress-2347_next"]')
            next_1.click()
            visualcapitalist(9)
            
        write_csv(rank, console, manufacturer, global_lifetime_sales)


    # if (next.click() != None):
    
    


startpy()


# //*[@id="tablepress-2347"]/tbody/tr[1]/td[2]
# //*[@id="tablepress-2347"]/tbody/tr[1]/td[2]



























































































































































































































































































































