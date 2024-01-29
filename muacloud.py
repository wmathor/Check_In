from util import *

username = sys.argv[1] # 登录账号
password = sys.argv[2] # 登录密码

@retry(stop_max_attempt_number=5)
def muacloud():
    try:
        driver = get_web_driver()
#         driver.get("https://muacloud.cloud/auth/login")
        driver.get("https://12o.ooo/user")
        driver.find_element_by_xpath("//*[@id='email']").send_keys(username)
        driver.find_element_by_xpath("//*[@id='password']").send_keys(password)
        driver.find_element_by_xpath("//*[@id='login_submit']").click()

        if driver.find_elements_by_xpath("//*[@id='checkin']") != []:
            driver.find_element_by_xpath("//*[@id='checkin']").click()
            print('muacloud签到成功')
    except:
        raise
    finally:
        driver.quit()

if __name__ == '__main__':
    muacloud()
