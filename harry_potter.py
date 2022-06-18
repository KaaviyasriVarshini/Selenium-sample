from selenium import webdriver
import time

PATH = "/home/sanjju/Downloads/chromedriver_linux64/chromedriver"
driver = webdriver.Chrome(PATH)
def startpy():
    driver.get("https://www.wizardingworld.com/")
    driver.maximize_window()
    time.sleep(3)
    book = driver.find_element_by_xpath('//*[@id="j_k_rowling_archive"]/div[2]')

    # print(book.text)
    book.click()
    powder = driver.find_element_by_xpath('//*[@id="__next"]/div[2]/div/div[3]/div[2]/div/a[2]')
    powder.click()
    time.sleep(2)
    para = driver.find_element_by_xpath('//*[@id="__next"]/div[2]/div/div[2]/div/div[2]/div/div/section')
    print(para.text)



startpy()


