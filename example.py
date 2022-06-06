from selenium import webdriver

path = "/home/sanjju/Downloads/chromedriver_linux64/chromedriver"
driver = webdriver.Chrome(path)


def startpy():
    driver.get("https://smazee.com/casestudy/blaer")
    id = driver.find_element_by_xpath("/html/body/footer/div[2]/div/div[1]/div[1]/div/div[2]/a[3]")
    print(id.text.strip())
    driver.maximize_window()







startpy()























