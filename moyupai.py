from header import *

username = sys.argv[1] # 登录账号
password = sys.argv[2] # 登录密码

def moyupai(driver):
    try:

        driver = get_web_driver()
        driver.get("https://pwl.icu/login")
        driver.find_element_by_xpath("//*[@id='nameOrEmail']").send_keys(username)
        driver.find_element_by_xpath("//*[@id='loginPassword']").send_keys(password)
        driver.find_element_by_xpath("//*[@class='green']").click()
        time.sleep(2)

        driver.find_element_by_xpath("//*[@id='yesterday']").click()
        driver.find_element_by_xpath("//*[@id='checkIn']").click()
        time.sleep(1)
        print('gamekegs签到成功')
        
    finally:
        driver.quit()

if __name__ == '__main__':
    driver = get_web_driver()
    moyupai(driver)