import sys
import os
import time
from util import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from retrying import retry


username = sys.argv[1]  # 登录账号
password = sys.argv[2]  # 登录密码
img_path = os.path.join(os.getcwd(), "1.png")


def safe_find(driver, xpath, wait_time=5):
    """Safely find an element with explicit wait."""
    try:
        return WebDriverWait(driver, wait_time).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
    except:
        return None


def solve_captcha(driver):
    """Handle captcha if present."""
    captcha_xpath = "//*[@width='160']"
    captcha_input_xpath = "//*[@name='seccodeverify']"
    captcha_elem = safe_find(driver, captcha_input_xpath, wait_time=2)
    if captcha_elem:
        valid = Ocr_Captcha(driver, captcha_xpath, img_path)
        captcha_elem.send_keys(valid)
        submit_btn = safe_find(driver, "//*[@type='submit']")
        if submit_btn:
            submit_btn.click()


@retry(stop_max_attempt_number=5)
def check_in_91():
    """Automate sign-in to 91tvg.com."""
    driver = get_web_driver()
    try:
        driver.get("https://www.91tvg.com")

        # Solve math captcha if present
        captcha_text_elem = safe_find(driver, "//*[@style='font-size: 16px']")
        if captcha_text_elem:
            answer = eval(captcha_text_elem.text[:-4])
            safe_find(driver, "//*[@type='text']").send_keys(answer)
            safe_find(driver, "//*[@type='submit']").click()

        # Login
        safe_find(driver, "//*[@name='username']").send_keys(username)
        safe_find(driver, "//*[@name='password']").send_keys(password)
        safe_find(driver, "//*[@type='submit']").click()

        # Extra captcha check after login
        captcha_text_elem = safe_find(driver, "//*[@style='font-size: 16px']", wait_time=2)
        if captcha_text_elem:
            answer = eval(captcha_text_elem.text[:-4])
            safe_find(driver, "//*[@type='text']").send_keys(answer)
            safe_find(driver, "//*[@type='submit']").click()

        # Handle image captcha
        solve_captcha(driver)

        # Click sign-in button
        signin_btn = safe_find(driver, "//*[@id='dcsignin_tips']", wait_time=10)
        if signin_btn:
            signin_btn.click()

        # Handle emoticon
        emot_btn = safe_find(driver, "//*[@id='emot_4']", wait_time=2)
        if emot_btn:
            emot_btn.click()
            safe_find(driver, "//*[@type='submit']").click()
            print("91wii 签到成功")

    except Exception as e:
        print(f"Error during check-in: {e}")
        raise
    finally:
        driver.quit()


if __name__ == "__main__":
    check_in_91()
