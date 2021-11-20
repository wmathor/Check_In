from util import *

username = sys.argv[1] # 登录账号
password = sys.argv[2] # 登录密码
img_path = os.getcwd() + "/1.png"

@retry(stop_max_attempt_number=5)
def v2ex():
    try:
        driver = get_web_driver()
        driver.get("https://v2ex.com/signin")
        driver.find_element_by_xpath("//*[@placeholder='用户名或电子邮箱地址']").send_keys(username)
        driver.find_element_by_xpath("//*[@type='password']").send_keys(password) 
        valid = Ocr_Captcha(driver, "//input[starts-with(@style,'background-image')]", img_path) # 验证码识别
        driver.find_element_by_xpath("//*[@placeholder='请输入上图中的验证码']").send_keys(password)
        driver.find_element_by_xpath("//*[@type='submit']").click()

        time.sleep(2)
        driver.get('https://v2ex.com/mission/daily')
        driver.find_element_by_xpath("//*[@type='button']").click()
    except:
        raise
    finally:
        driver.quit()

if __name__ == '__main__':
    v2ex()