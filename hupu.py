from util import *
import time

username = sys.argv[1] # 登录账号
password = sys.argv[2] # 登录密码

@retry(stop_max_attempt_number=5)
def hupu():
    try:
        driver = get_web_driver()
        driver.get("https://www.hupu.com/")
        driver.find_element_by_xpath("//*[@class='btn-login']").click()
        driver.find_element_by_xpath("//*[@id='bbs-login-form_username']").send_keys(username)
        driver.find_element_by_xpath("//*[@id='bbs-login-form_password']").send_keys(password)
        driver.find_element_by_xpath("//*[@id='rectBottom']").click()
        time.sleep(1)
        driver.find_element_by_xpath("//*[@class='ant-btn ant-btn-primary ant-btn-block submit-btn']").click()
    except:
        raise
    finally:
        driver.quit()

if __name__ == '__main__':
    hupu()
