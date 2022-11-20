from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("http://116.13.1.23/ams/front/login.do")
driver.find_element(By.NAME,"taskId").send_keys(23)
driver.find_element(By.NAME,"loginName").send_keys("student2")
driver.find_element(By.NAME,"password").send_keys("student2")
driver.find_element(By.TAG_NAME,"button").click()
# driver.get_screenshot_as_file('denglu.png')