import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

username = "739616037@qq.com" # 登录账号
password = "w739616037" # 登录密码

def muacloud():
    try:
        driver = webdriver.Chrome(chrome_options=chrome_options)
        driver.get("https://muacloud.cloud/auth/login")
        driver.find_element_by_xpath("//*[@id='email']").send_keys(username)
        driver.find_element_by_xpath("//*[@id='password']").send_keys(password)
        driver.find_element_by_xpath("//*[@id='login_submit']").click()
        time.sleep(3)

        driver.find_element_by_xpath("//*[@id='checkin']").click()
        time.sleep(1)
    finally:
        driver.quit()
        # pass