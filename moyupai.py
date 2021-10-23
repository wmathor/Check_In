from util import *

username = sys.argv[1] # 登录账号
password = sys.argv[2] # 登录密码
img_path = os.getcwd() + "/1.png"

@retry(stop_max_attempt_number=5)
def moyupai():
    try:
        driver = get_web_driver()
        driver.get("https://pwl.icu/login")
        driver.find_element_by_xpath("//*[@id='nameOrEmail']").send_keys(username)
        driver.find_element_by_xpath("//*[@id='loginPassword']").send_keys(password)
        driver.find_element_by_xpath("//*[@class='green']").click() # 为了显示验证码，先点击一次登录

        # if driver.find_elements_by_xpath("//*[@id='captchaLogin']"): # 如果需要输入验证码
        #     driver.find_element_by_xpath("//*[@id='nameOrEmail']").send_keys(username) # 从这开始才是真正的登录步骤
        #     driver.find_element_by_xpath("//*[@id='loginPassword']").send_keys(password)
        #     valid = Ocr_Captcha(driver, "//*[@class='captcha-img fn-pointer']", img_path) # 验证码识别
        #     driver.find_element_by_xpath("//*[@id='captchaLogin']").send_keys(valid)
        #     driver.find_element_by_xpath("//*[@class='green']").click()
        
        driver.find_element_by_xpath("//*[@id='yesterday']").click()
        driver.find_element_by_xpath("//*[@id='checkIn']").click()

        valid = Ocr_Captcha(driver, "//*[@id='registerCaptchaImg']", img_path) # 验证码识别
        if valid != '':
            print(valid)
            driver.find_element_by_xpath("//*[@placeholder='验证码']").send_keys(valid)
            driver.find_element_by_xpath("//*[@onclick='submitCheckIn()']").click()
            print('moyupai签到成功')
    except:
        raise
    finally:
        driver.quit()

if __name__ == '__main__':
    moyupai()