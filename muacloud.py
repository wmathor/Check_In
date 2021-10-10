import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

username = "739616037@qq.com" # 登录账号
password = "w739616037" # 登录密码

def muacloud():
    try:

        driver.get("https://muacloud.cloud/auth/login")
        print(driver.title)
        driver.find_element_by_xpath("//*[@id='email']").send_keys(username)
        driver.find_element_by_xpath("//*[@id='password']").send_keys(password)
        driver.find_element_by_xpath("//*[@id='login_submit']").click()
        time.sleep(3)

        driver.find_element_by_xpath("//*[@id='checkin']").click()
        time.sleep(1)
    finally:
        driver.quit()
        return 0