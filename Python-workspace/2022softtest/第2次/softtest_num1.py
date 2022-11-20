from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://116.13.1.23/ams/front/login.do")
driver.find_element(By.CSS_SELECTOR,"#taskId").send_keys(23)
driver.find_element(By.CSS_SELECTOR,"#loginName").send_keys("student2")
driver.find_element(By.XPATH,'//*[@id="password"]').send_keys("student2")
driver.find_element(By.CLASS_NAME,'blue-button').click()
sleep(3)
driver.quit()