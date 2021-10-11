import time, ddddocr, requests, os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from PIL import Image

username = '15549457220'
password = 'w739616037'

def Sliding_Captcha():
    

def juejin(driver):
    driver = webdriver.Chrome()
    driver.get("https://juejin.cn/")
    driver.find_element_by_xpath("//*[@class='login-button']").click() # 点击"登录"按钮
    driver.find_element_by_xpath("//*[@class='login-button']").click() # 点击"其他登录方式"
    driver.find_element_by_xpath("//*[@name='loginPhoneOrEmail']").send_keys(username)
    driver.find_element_by_xpath("//*[@name='loginPassword']").send_keys(password)
    driver.find_element_by_xpath("//*[@class='btn']").click() # 点击"登录"按钮

    # 验证码处理


if __name__ == '__main__':
    # driver = get_web_driver()
    juejin(driver)