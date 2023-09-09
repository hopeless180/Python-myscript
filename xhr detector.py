from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests

# 配置 Chrome WebDriver 的路径
webdriver_service = Service('path/to/chromedriver')

# 创建 Chrome WebDriver 实例
driver = webdriver.Chrome(service=webdriver_service)

# 打开网页并进行登录
driver.get('https://bbs.mihoyo.com/sr/wiki/channel/map/17/18?bbs_presentation_style=no_header')

# 等待登录成功后的某个元素出现，可根据实际情况修改选择器
# element = WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.CSS_SELECTOR, '.success-element'))
# )
# 等待XHR请求完成
wait = WebDriverWait(driver, 10)
wait.until(lambda driver: driver.execute_script('return jQuery.active == 0'))

# 获取登录到某个时间为止的所有XHR请求
performance = driver.execute_script("return window.performance.getEntriesByType('network')")
xhr_requests = [entry['name'] for entry in performance if entry['initiatorType'] == 'xmlhttprequest']

# 打印XHR请求的URL
for request in xhr_requests:
    print(request)

keywords = ['景元']

# 遍历XHR请求
for request in xhr_requests:
    response = requests.get(request)  # 发起GET请求获取XHR的响应

    # 检查响应是否包含关键词
    if any(keyword in response.text for keyword in keywords):
        # 响应中包含关键词，可能包含网页内容
        print('XHR Request:', request)
        print('Response:', response.text)
        print('-------------------')