from header import *

username = sys.argv[1] # 登录账号
password = sys.argv[2] # 登录密码

def muacloud(driver):
    try:

        driver.get("https://muacloud.cloud/auth/login")
        driver.find_element_by_xpath("//*[@id='email']").send_keys(username)
        driver.find_element_by_xpath("//*[@id='password']").send_keys(password)
        driver.find_element_by_xpath("//*[@id='login_submit']").click()
        time.sleep(3)

        if driver.find_elements_by_xpath("//*[@id='checkin']") == []: # 如果已经签到过了，就不要签到了
            return 

        driver.find_element_by_xpath("//*[@id='checkin']").click()
        time.sleep(1)

    finally:
        driver.quit()

if __name__ == '__main__':
    driver = get_web_driver()
    muacloud(driver)