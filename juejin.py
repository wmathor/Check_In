from util import *

username = '15549457220'
password = 'w739616037'

def Sliding_Captcha(driver):
    # 获取验证图片
    slide_img = driver.find_element_by_xpath("//*[@id='captcha-verify-image']")
    backgroud_img = driver.find_element_by_xpath("//*[@class='captcha_verify_img_slide react-draggable sc-VigVT ggNWOG']")
    slide_url = slide_img.get_attribute("src")
    backgroud_url = backgroud_img.get_attribute("src")
    
    track = Track()
    result = track.get_track(slide_url, backgroud_url)

    verify_div = driver.find_element(By.XPATH, '''//div[@class="sc-kkGfuU bujTgx"]''')

    # 按下鼠标左键
    ActionChains(driver).click_and_hold(verify_div).perform()
    time.sleep(0.5)
    # 遍历轨迹进行滑动
    for t in result:
        time.sleep(0.01)
        ActionChains(driver).move_by_offset(xoffset=t, yoffset=0).perform()
    # 释放鼠标
    ActionChains(driver).release(on_element=verify_div).perform()

    
def juejin(driver):
    try:

        driver.get("https://juejin.cn/")
        driver.find_element_by_xpath("//*[@class='login-button']").click() # 点击"登录"按钮
        driver.find_element_by_xpath("//*[@class='clickable']").click() # 点击"其他登录方式"
        driver.find_element_by_xpath("//*[@name='loginPhoneOrEmail']").send_keys(username)
        driver.find_element_by_xpath("//*[@name='loginPassword']").send_keys(password)
        driver.find_element_by_xpath("//*[@class='btn']").click() # 点击"登录"按钮
        
        # 验证码处理
        Sliding_Captcha(driver)
        driver.get("https://juejin.cn/user/center/signin")
        print(driver.find_element_by_xpath("//*[@class='user-name']").text)
        driver.find_element_by_xpath("//*[@class='signin btn']").click()

    finally:
        driver.quit()

if __name__ == '__main__':
    driver = get_web_driver()
    juejin(driver)