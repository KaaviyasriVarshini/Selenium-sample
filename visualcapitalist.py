from selenium import webdriver


PATH = "/home/sanjju/Downloads/chromedriver_linux64/chromedriver"
driver = webdriver.Chrome(PATH)

def startpy():

    URL = "https://www.visualcapitalist.com/cp/ranked-the-best-selling-video-game-consoles-of-all-time/"


    driver.get(URL)
    driver.maximize_window()
    game_consoles = driver.find_element_by_xpath('//*[@id="tablepress-2347_wrapper"]')
    print(game_consoles.text)






startpy()







