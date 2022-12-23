# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     BasePage
   Description :
   Author :       xiao
   date：          2022/11/14
-------------------------------------------------
   Change Activity:
                   2022/11/14:
-------------------------------------------------
"""
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import csv


url = "https://www.taobao.com"


def initTest():
    s = Service("chromedriver1.exe")
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument('--ignore-certificate-errors')
    options.add_argument("blink-settings=imagesEnabled=false")
    options.add_experimental_option('excludeSwitches', ['enable-automation'])  # 开启开发者模式
    options.add_experimental_option('useAutomationExtension', False)
    browser = webdriver.Chrome(service=s, options=options)
    browser.maximize_window()
    wait = WebDriverWait(browser, 5)
    return browser