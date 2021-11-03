from util import *

username = sys.argv[1] # 登录账号
password = sys.argv[2] # 登录密码
img_path = os.getcwd() + "/1.png"

# @retry(stop_max_attempt_number=5)
def moyupai():
    try:
        driver = webdriver.Chrome()
        driver.get("https://www.91wii.com/forum-125-1.html")
        a = driver.find_element_by_xpath("//*[@style='font-size: 16px']").text
        driver.find_element_by_xpath("//*[@type='text']").send_keys(eval(a[:-4]))
        driver.find_element_by_xpath("//*[@type='submit']").click() # 为了显示验证码，先点击一次登录

        driver.find_element_by_xpath("//*[@name='username']").send_keys(username)
        driver.find_element_by_xpath("//*[@name='password']").send_keys(password)
        driver.find_element_by_xpath("//*[@type='submit']").click()

        if driver.find_elements_by_xpath("//*[@style='font-size: 16px']"):
            a = driver.find_element_by_xpath("//*[@style='font-size: 16px']").text
            driver.find_element_by_xpath("//*[@type='text']").send_keys(eval(a[:-4]))
            valid = Ocr_Captcha(driver, "//*[@class='captcha-clk2']", img_path) # 验证码识别

        driver.find_element_by_xpath("//*[@id='dcsignin_tips']").click() # 点击'签到' 按钮
        if driver.find_elements_by_xpath("//*[@id='emot_4']") != []:
            driver.find_element_by_xpath("//*[@id='emot_4']").click()
            driver.find_element_by_xpath("//*[@type='submit']").click()
            print('91wii签到成功')
    except:
        raise
    finally:
        driver.quit()

if __name__ == '__main__':
    moyupai()