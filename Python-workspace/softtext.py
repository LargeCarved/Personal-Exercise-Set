# from selenium import webdriver
# browser = webdriver.Chrome()
# print(type(browser))
# browser.get('https://www.baidu.com')

# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys

# driver = webdriver.Chrome()
# driver.get("http://www.python.org")
# assert "Python" in driver.title
# elem = driver.find_element_by_name("q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()


# 测试
# import unittest
# from ddt import *


# @ddt
# class TestCan(unittest.TestCase):

#     @data(1, 2, 3, 4)
#     def test_int(self, i):
#         print("test_int", i)

#     @data("a", "b", "c", "d")
#     def test_str(self, s):
#         print("test_str", s)

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from time import sleep
# browser = webdriver.Chrome()
# browser.get('https://www.taobao.com')
# sleep(5)  # 强制等5s
# browser.maximize_window()  # 窗口最大化
# sleep(3)
# a = browser.find_element(
#     By.XPATH, '//*[@id="J_SiteNavLogin"]/div[1]/div[1]/a[2]').click()
# b = browser.find_element(
#     By.XPATH, '//*[@id = "container"]/div/div[2]/div[1]/div/div/div[2]/input').send_keys("15338912608")
# c = browser.find_element(
#     By.XPATH, '//*[@id="container"]/div/div[2]/div[2]/div/div/div[1]/input').send_keys("114514")
# browser.get_screenshot_as_file("sev.png")
# # 点击按钮事件与操作
# sleep(3)
# # browser.implicitly_wait(3)  # 智能等待3秒，也就隐式等待。
# browser.find_element(
#     By.XPATH, '//*[@id="container"]/div/div[2]/div[2]/div/div/div[2]/a').click()

# a = browser.find_element(By.ID, 'q')
# c = browser.find_element(By.XPATH, '//*[@id="q"]',)
# d = browser.find_element(By.CSS_SELECTOR, '#q')
# print(a, b, c, d)
# print(a == b == c == d)
# browser.close()

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# 实例化浏览器
driver = webdriver.Chrome()

# 打开网址，且放大页面
driver.get('https://www.baidu.com/')
driver.maximize_window()
sleep(2)
driver.set_window_size(800,800)
sleep(1)
driver.set_window_position(500,200)
sleep(1)
print(driver.title,driver.current_url)


# 需求
ele = driver.find_element(By.CSS_SELECTOR,'#kw')
ele.send_keys('易烊千玺')
sleep(2)

# 清空
ele.clear()
ele.send_keys('王嘉尔')

# 时间轴看效果
sleep(3)

# 关闭页面
driver.quit()

# 方法
"""
1、driver.maximize_window()  # 最大化浏览器
2、driver.set_window_size(w,h)  # 设置浏览器大小 单位像素 【了解】
3、driver.set_window_position(x,y)  # 设置浏览器位置  【了解】
4、driver.back() # 后退操作
5、driver.forward() # 前进操作
6、driver.refrensh() # 刷新操作
7、driver.close() # 关闭当前主窗口（主窗口：默认启动那个界面，就是主窗口）
8、driver.quit() # 关闭driver对象启动的全部页面
9、driver.title # 获取当前页面title信息
10、driver.current_url # 获取当前页面url信息
"""

