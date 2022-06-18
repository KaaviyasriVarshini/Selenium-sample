# from selenium import webdriver
# import pandas as pd




# PATH = "/home/sanjju/Downloads/chromedriver_linux64/chromedriver"
# driver = webdriver.Chrome(PATH)


# def startpy():


#     for i in range(1, 11):

#         driver.get("https://www.visualcapitalist.com/cp/ranked-the-best-selling-video-game-consoles-of-all-time/")
#         # driver.maximize_window()


#         rank = driver.find_element_by_xpath(f'//*[@id="tablepress-2347"]/tbody/tr[{i}]/td[1]')
#         # print(rank.text)
#         console = driver.find_element_by_xpath(f'//*[@id="tablepress-2347"]/tbody/tr[{i}]/td[2]')
#         # print(console.text)
#         manufacturer = driver.find_element_by_xpath(f'//*[@id="tablepress-2347"]/tbody/tr[{i}]/td[3]')
#         # print(manufacturer.text)
#         global_lifetime_sales = driver.find_element_by_xpath(f'//*[@id="tablepress-2347"]/tbody/tr[{i}]/td[4]')
#         # print(global_lifetime_sales.text)

        
#     def write_csv():
#         file = open("data.csv","x")
#         data = {
#             "Rank" : rank,
#             "Console" : console,
#             "Manufacturer" : manufacturer,
#             "Global lifetime sales" : global_lifetime_sales
#         }
        
#         df = pd.DataFrame([data])
#         df.to_csv("data.csv",index=False)
#         print(df)



#     write_csv()


# startpy()


# '''

# //*[@id="tablepress-2347"]/tbody/tr[1]/td[1]
# //*[@id="tablepress-2347"]/tbody/tr[1]/td[2]
# //*[@id="tablepress-2347"]/tbody/tr[1]/td[3]
# //*[@id="tablepress-2347"]/tbody/tr[1]/td[4]










# import pandas as pd



# def write_csv():
#     # file = open("subject.csv","x")
#     subject_dict = {
#         "kaaviya":["math","physics"],
#         "chaaya": ["games","computer"]
#     }

#     df = pd.DataFrame([subject_dict])
#     df.to_csv("subject.csv",index=False)

#     # print(df)

# def read_file():
#     df = pd.read_csv("scapanza-s5.csv")
#     print(df)

# # write_csv()
# read_file()


# '''








