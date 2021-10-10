import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from muacloud import *
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

username = "mathor" # 登录账号
password = "w123456" # 登录密码

def moyupai():
    try:
        driver = webdriver.Chrome(chrome_options=chrome_options)
        driver.get("https://pwl.icu/login")
        driver.find_element_by_xpath("//*[@id='nameOrEmail']").send_keys(username)
        driver.find_element_by_xpath("//*[@id='loginPassword']").send_keys(password)
        driver.find_element_by_xpath("//*[@class='green']").click()
        time.sleep(2)

        driver.find_element_by_xpath("//*[@id='yesterday']").click()
        driver.find_element_by_xpath("//*[@id='checkIn']").click()
        time.sleep(1)
    finally:
        driver.quit()
        muacloud()
        # pass