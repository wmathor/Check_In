import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

username = "mathor" # 登录账号
password = "w123456" # 登录密码

def moyupai():
    try:
        
        driver.get("https://pwl.icu/login")
        print(driver.title)
        driver.find_element_by_xpath("//*[@id='nameOrEmail']").send_keys(username)
        driver.find_element_by_xpath("//*[@id='loginPassword']").send_keys(password)
        driver.find_element_by_xpath("//*[@class='green']").click()
        time.sleep(2)

        driver.find_element_by_xpath("//*[@id='yesterday']").click()
        driver.find_element_by_xpath("//*[@id='checkIn']").click()
        time.sleep(1)
    finally:
        driver.quit()
        return 0