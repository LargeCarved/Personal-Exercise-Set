# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     test_Add
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
import csv
import sys

sys.path.append("..\\")
from page.LoginPage import loginAction
from page.BasePage import initTest

Browser = initTest()
loginAction(Browser, "xiao", "888888")
