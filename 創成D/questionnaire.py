from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep
import random 

print("アンケートの選択肢の数を入力してください")
questions = input()

ChromeOptions = webdriver.ChromeOptions()
ChromeOptions.add_experimental_option('excludeSwitches', ['enable-logging'])

browser = webdriver.Chrome('chromedriver.exe')
browser.get('file:///C:/Users/81909/Desktop/%E5%89%B5%E6%88%90D/sousei.html')


for i in range(1 , int(questions)+1):
    answer = random.randint(1,5)
    question = browser.find_elements_by_xpath(f"//input[@name={i}][@type='radio']")
    radio_arr = {}
    for elem in question:
        if elem.get_attribute("value") == str(answer):
            elem.click()

question_2 = browser.find_element_by_name("message")
question_2.send_keys("忘れている事が多いから。")


# 参考文献:
#https://programming-dojo.com/%E3%80%90python3%E5%85%A5%E9%96%80%E3%80%91%E6%96%87%E5%AD%97%E5%88%97%E3%81%AE%E4%B8%AD%E3%81%AB%E5%A4%89%E6%95%B0%E5%B1%95%E9%96%8B%E3%82%92%E3%81%99%E3%82%8B/
#https://www.headboost.jp/python-convert-int-into-str/