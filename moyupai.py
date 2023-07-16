=from util import *

username = sys.argv[1] # 登录账号
password = sys.argv[2] # 登录密码
img_path = os.getcwd() + "/1.png"

def save_img(src):
img = requests.get(src)
with open(img_path, "wb") as f:
f.write(img.content)

@retry(stop_max_attempt_number=5)
def moyupai():
try:
driver = get_web_driver()
driver.get("https://h5.xoxo7.cc/#/login")
time.sleep(10)
driver.find_element_by_xpath("//[@name='username']").send_keys(username)
driver.find_element_by_xpath("//[@name='password']").send_keys(password)
# 验证码
time.sleep(5)
valid = Ocr_Captcha(driver, "//[@class='fr_item']", img_path) # 验证码识别
driver.find_element_by_xpath("//[@placeholder='输入图形码']").send_keys(valid)
driver.find_element_by_xpath("//[@type='submit']").click()
print("验证码识别结果：", valid)
time.sleep(10)
driver.find_element_by_xpath("//[@class='close']").click()
time.sleep(3)
driver.find_element_by_xpath("//[@class='close2']").click()
time.sleep(3)
driver.find_element_by_xpath("//[@class='close2']").click()
time.sleep(3)
driver.find_element_by_xpath("//*[@class='ok']").click()
time.sleep(2)
driver.find_element_by_xpath("//h6[text()='我的']").click()
time.sleep(2)
driver.find_element_by_xpath("//a[text()='签到']").click()
except:
raise
finally:
driver.quit()

if name == 'main':
moyupai() 
