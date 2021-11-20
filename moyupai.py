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
        driver.find_element_by_xpath("//*[@class='green']").click()

        driver.find_element_by_xpath("//*[@id='yesterday']").click()
        print('moyupai签到成功')
    except:
        raise
    finally:
        driver.quit()

if __name__ == '__main__':
    moyupai()
