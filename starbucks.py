from selenium import webdriver


PATH = "/home/sanjju/Downloads/chromedriver_linux64/chromedriver"
driver = webdriver.Chrome(PATH)

def startpy():

    for i in range(1300, 1401):
        URL = "https://www.starbucks.ca/store-locator/store/"+str(i)

        driver.get(URL)
        try:
            
            working_hours = driver.find_element_by_xpath('//*[@id="content"]/div[3]/div/div/div[2]/article/section[2]/div/div')
            print(working_hours.text)
        except:
            continue
    driver.maximize_window()
# //*[@id="content"]/div[3]/div/div/div[2]/article/section[2]/div/div



startpy()










