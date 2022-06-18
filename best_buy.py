from selenium import webdriver
import time
import pandas as pd





PATH = "/home/sanjju/Downloads/chromedriver_linux64/chromedriver"
driver = webdriver.Chrome(PATH)

def startpy():

    BEST_BUY = []

    URL = "https://www.bestbuy.ca/en-ca/product/canon-eos-6d-mark-ii-dslr-full-frame-dslr-camera-body-only/13222066"

    driver.get(URL)
    driver.maximize_window()
    time.sleep(5)

    customer_review = driver.find_element_by_xpath('//*[@id="reviews"]/div')
    customer_review.click()
    all_reviews = driver.find_element_by_xpath('//*[@id="reviews"]/div/div[4]/button/span')
    all_reviews.click()
    time.sleep(3)
    
    more_click()
    

    review = driver.find_elements_by_class_name('col-sm-6_28Jaa.col-md-8_24nR0.col_3jYsd')
    # print(review)
    for i in review:

        Review = {}
        # print(i.text)
        title = i.find_element_by_class_name('reviewTitle_1qq1j')
        print(title.text)
        _review_ = i.find_element_by_class_name('reviewContent_XCspv')
        print(_review_.text)

        Review["TITLE"] = [title.text]
        Review["REVIEW"] = [_review_.text]
        BEST_BUY.append(Review)

    # file = open("Review.csv", "x")
    df = pd.DataFrame.from_dict(BEST_BUY)
    df.to_csv("Review.csv", index = False, header = True)








def more_click():
    while True:
        try:

            show_more = driver.find_element_by_class_name('button_E6SE9.secondary_2Lchg.button_1Yg9v.loadMore_3AoXT.regular_1jnnf')
            show_more.click()
            time.sleep(3)
        except:
            break



startpy()

