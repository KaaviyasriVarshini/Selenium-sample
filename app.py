from selenium import webdriver

PATH = "/home/sanjju/Downloads/chromedriver_linux64/chromedriver"
driver = webdriver.Chrome(PATH)
def startpy():
    driver.get("https://ifconfig.me/")
    ip_address = driver.find_element_by_xpath('//*[@id="ip_address"]')
    print(ip_address.text)
    driver.maximize_window()



startpy()
