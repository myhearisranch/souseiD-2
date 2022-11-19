from selenium import webdriver
from time import sleep

ChromeOptions = webdriver.ChromeOptions()
ChromeOptions.add_experimental_option('excludeSwitches', ['enable-logging'])

print("学籍番号を入力してください。")
student_number = input()
print("パスワードを入力してください。")
password = input()

# chromeの鼓動
browser = webdriver.Chrome('chromedriver.exe')

# Googleにアクセスする
browser.get('https://tora-net.sti.chubu.ac.jp/portal/top.do')


elem_username = browser.find_element_by_name('userId')
elem_username.send_keys(student_number)

elem_password = browser.find_element_by_name("password")
elem_password.send_keys(password)

elem_login_button = browser.find_element_by_id("loginButton")
elem_login_button.click()