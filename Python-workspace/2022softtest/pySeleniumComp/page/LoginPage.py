# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     LoginPage
   Description :
   Author :       xiao
   date：          2022/11/14
-------------------------------------------------
   Change Activity:
                   2022/11/14:
-------------------------------------------------
"""
import datetime
import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import BasePage


def loginAction(browser, uname: str, upass: str) -> str:
    browser.get(BasePage.url)
    browser.implicitly_wait(3)
    user = browser.find_element(by=By.XPATH, value='//input[@id="fm-login-id"]')
    user.click()
    user.clear()
    time.sleep(random.randint(1, 3))
    user.send_keys(uname)  # 输入你的账号
    time.sleep(random.randint(2, 5))
    pwd = browser.find_element(by=By.XPATH, value='//input[@id="fm-login-password"]')
    pwd.click()
    pwd.clear()
    time.sleep(random.randint(1, 3))
    pwd.send_keys(upass)  # 输入你的密码
    time.sleep(random.randint(2, 5))
    login = browser.find_element(by=By.XPATH, value='//*[@id="login-form"]/div[4]/button')
    login.click()
    time.sleep(random.randint(5, 10))
    cookie = browser.get_cookies()
    return cookie


def cookieLogin(self, cookies: str, goodselem: str, baseurl: str, searchcnt: int) -> dict:
    self.browser.get(baseurl)
    for cookie in cookies:
        self.browser.add_cookie(cookie)
    self.browser.refresh()  # 刷新
    time.sleep(random.randint(3, 6))
    search_input = self.browser.find_element(by=By.XPATH, value='//*[@id="q"]')
    shop_name = goodselem
    search_input.send_keys(shop_name)
    print("现在正搜索商品:" + shop_name)
    time.sleep(random.randint(1, 3))
    search_submit = self.browser.find_element(by=By.XPATH, value='//*[@id="J_TSearchForm"]/div[1]/button')
    search_submit.click()
    element = WebDriverWait(self.browser, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="mainsrp'
                                                                                              '-pager"]/div/div/div/div[1]')))
    sum_page = self.browser.find_element(by=By.XPATH, value='//*[@id="mainsrp-pager"]/div/div/div/div[1]').text
    print("目前搜索到该类产品:" + sum_page)
    ## ………………
