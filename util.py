# from PIL import Image
# import cv2, ddddocr
import numpy as np
from retrying import retry
from selenium import webdriver
import os, sys, time, requests
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox') # 解决DevToolsActivePort文件不存在的报错
chrome_options.add_argument('window-size=1920x1080') # 指定浏览器分辨率
chrome_options.add_argument('--disable-gpu') # 谷歌文档提到需要加上这个属性来规避bug
chrome_options.add_argument('--headless') # 浏览器不提供可视化页面. linux下如果系统不支持可视化不加这条会启动失败

def get_web_driver():
    chromedriver = "/usr/bin/chromedriver"
    os.environ["webdriver.chrome.driver"] = chromedriver
    driver = webdriver.Chrome(executable_path=chromedriver, chrome_options=chrome_options)
    driver.implicitly_wait(10) # 所有的操作都可以最长等待10s
    return driver

# 一直等待某元素可见，默认超时10秒（此函数暂时没有使用）
def is_visible(driver, locator, timeout=10):
    try:
        element = WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.XPATH, locator)))
        return element
    except TimeoutException:
        return False

# def Ocr_Captcha(driver, locator, img_path): # 验证码识别
#     propertery = driver.find_element_by_xpath(locator)
#     driver.save_screenshot(img_path)
#     img = Image.open(img_path)
#     location = propertery.location
#     size = propertery.size
#     left = location['x']
#     top = location['y']
#     right = left + size['width']
#     bottom = top + size['height']
#     image = img.crop((left, top, right, bottom))  # 左、上、右、下
#     image.save(img_path)
#     ocr = ddddocr.DdddOcr()
#     with open(img_path, 'rb') as f:
#         img_bytes = f.read()
#     res = ocr.classification(img_bytes)
#     return res

class Track(object):
    # 处理前图片
    slider = "./slider.png"
    background = "./background.png"

    # 将处理之后的图片另存
    slider_bak = "./slider_bak.png"
    background_bak = "./background_bak.png"

    def get_track(self, slider_url, background_url) -> list:
        distance = self.get_slide_distance(slider_url, background_url)
        result = self.gen_normal_track(distance)
        return result

    @staticmethod
    def gen_normal_track(distance):
        def norm_fun(x, mu, sigma):
            pdf = np.exp(-((x - mu) ** 2) / (2 * sigma ** 2)) / (sigma * np.sqrt(2 * np.pi))
            return pdf

        result = []
        for i in range(-10, 10, 1):
            result.append(norm_fun(i, 0, 1) * distance)
        result.append(sum(result) - distance)
        return result

    @staticmethod
    def gen_track(distance):  # distance为传入的总距离
        # 移动轨迹
        result = []
        # 当前位移
        current = 0
        # 减速阈值
        mid = distance * 4 / 5
        # 计算间隔
        t = 0.2
        # 初速度
        v = 1

        while current < distance:
            if current < mid:
                # 加速度为2
                a = 4
            else:
                # 加速度为-2
                a = -3
            v0 = v
            # 当前速度
            v = v0 + a * t
            # 移动距离
            move = v0 * t + 1 / 2 * a * t * t
            # 当前位移
            current += move
            # 加入轨迹
            result.append(round(move))
        return result

    @staticmethod
    def onload_save_img(slider_url, slider):
        r = requests.get(slider_url)
        with open(slider, 'wb') as f:
            f.write(r.content)

#     def get_slide_distance(self, slider_url, background_url):

#         # 下载验证码背景图,滑动图片
#         self.onload_save_img(slider_url, self.slider)
#         self.onload_save_img(background_url, self.background)
#         # 读取进行色度图片，转换为numpy中的数组类型数据
#         slider_pic = cv2.imread(self.slider, 0)
#         background_pic = cv2.imread(self.background, 0)
#         # 获取缺口图数组的形状 -->缺口图的宽和高
#         width, height = slider_pic.shape[::-1]

#         cv2.imwrite(self.background_bak, background_pic)
#         cv2.imwrite(self.slider_bak, slider_pic)
#         # 读取另存的滑块图
#         slider_pic = cv2.imread(self.slider_bak)
#         # 进行色彩转换
#         slider_pic = cv2.cvtColor(slider_pic, cv2.COLOR_BGR2GRAY)
#         # 获取色差的绝对值
#         slider_pic = abs(255 - slider_pic)
#         # 保存图片
#         cv2.imwrite(self.slider_bak, slider_pic)
#         # 读取滑块
#         slider_pic = cv2.imread(self.slider_bak)
#         # 读取背景图
#         background_pic = cv2.imread(self.background_bak)
#         # 比较两张图的重叠区域
#         result = cv2.matchTemplate(slider_pic, background_pic, cv2.TM_CCOEFF_NORMED)
#         # 获取图片的缺口位置
#         top, left = np.unravel_index(result.argmax(), result.shape)
#         # 背景图中的图片缺口坐标位置
#         return left * 340 / 552
