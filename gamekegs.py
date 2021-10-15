from util import *

username = sys.argv[1] # 登录账号
password = sys.argv[2] # 登录密码
img_path = os.getcwd() + "/1.png"

def save_img(src):
    img = requests.get(src)
    with open(img_path, "wb") as f:
        f.write(img.content)

@retry(stop_max_attempt_number=5)
def gamekegs():
    try:
        driver = get_web_driver()
        driver.get("https://gamekegs.com/login")
        driver.find_element_by_xpath("//*[@id='username']").send_keys(username)
        driver.find_element_by_xpath("//*[@id='password']").send_keys(password)
        driver.find_element_by_xpath("//*[@class='captcha-clk2']").click() # 点击验证码

        time.sleep(5)
        valid = Ocr_Captcha(driver, "//*[@class='captcha-clk2']", img_path) # 验证码识别

        driver.find_element_by_xpath("//*[@placeholder='验证码']").send_keys(valid)
        driver.find_element_by_xpath("//*[@type='submit']").click()

        if driver.find_elements_by_xpath("//*[@class='usercheck checkin']") != []:
            driver.find_element_by_xpath("//*[@class='usercheck checkin']").click()
            print('gamekegs签到成功')
    except:
        raise
    finally:
        driver.quit()

if __name__ == '__main__':
    gamekegs()