from header import *

username = "739616037@qq.com" # 登录账号
password = sys.argv[1] # 登录密码

def muacloud(driver):
    try:

        driver = get_web_driver()
        driver.get("https://muacloud.cloud/auth/login")
        driver.find_element_by_xpath("//*[@id='email']").send_keys(username)
        driver.find_element_by_xpath("//*[@id='password']").send_keys(password)
        driver.find_element_by_xpath("//*[@id='login_submit']").click()
        time.sleep(3)

        driver.find_element_by_xpath("//*[@id='checkin']").click()
        time.sleep(1)

    finally:
        driver.quit()