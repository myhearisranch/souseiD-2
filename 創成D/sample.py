from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep

ChromeOptions = webdriver.ChromeOptions()
ChromeOptions.add_experimental_option('excludeSwitches', ['enable-logging'])

browser = webdriver.Chrome('chromedriver.exe')
browser.get('https://azby.fmworld.net/app/customer/enquete/EnqueteServlet?ENQ_N=azbyclub_kids2008&USR_NO=20221109')


question_1 = browser.find_element_by_name("q001")
select = Select(question_1)
select.select_by_value("a001")

question_2 = browser.find_element_by_name("q002")
select = Select(question_2)
select.select_by_value("a002")

question_3 = browser.find_element_by_name("q003")
select = Select(question_3)
select.select_by_value("a002")

question_4 = browser.find_element_by_name("q004")
select = Select(question_4)
select.select_by_value("a002")

question_5 = browser.find_elements_by_xpath("//input[@name='q005'][@type='radio']")
labels = browser.find_elements_by_xpath("//label")
radio_arr = {}
for elem in question_5:
    for label in labels:
        if(elem.get_attribute("id") == label.get_attribute("for")):
            radio_arr[elem.get_attribute("value")] = label.text
            if elem.get_attribute("value") == "a001":
                elem.click()


question_6 = browser.find_elements_by_xpath("//input[@name='q007'][@type='checkbox']")
labels = browser.find_elements_by_xpath("//label")
checkbox_arr = {}
for elem in question_6:
    for label in labels:
        if (elem.get_attribute("id") == label.get_attribute("for")):  
            checkbox_arr[elem.get_attribute("value")] = label.text
            if elem.get_attribute("value") == "a001":
                label.click()    


question_7 = browser.find_elements_by_xpath("//input[@name='q008'][@type='checkbox']")
labels = browser.find_elements_by_xpath("//label")
checkbox_arr = {}
for elem in question_7:
    for label in labels:
        if (elem.get_attribute("id") == label.get_attribute("for")):  
            checkbox_arr[elem.get_attribute("value")] = label.text
            if elem.get_attribute("value") != "a001":
                label.click()


question_8 = browser.find_element_by_name("q010")
question_8.send_keys("特になし")




# 参考文献:
# https://office54.net/python/scraping/selenium-select-option
# http://holiday-programmer.net/selenium-radio/
# http://holiday-programmer.net/selenium-checkbox/#checkboxlabel-2