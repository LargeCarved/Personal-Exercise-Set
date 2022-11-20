from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://116.13.1.23/ams/front/login.do")
driver.implicitly_wait(30)
driver.find_element(By.CSS_SELECTOR,"#taskId").send_keys(23)
driver.find_element(By.CSS_SELECTOR,"#loginName").send_keys("student2")
driver.find_element(By.ID,'password').send_keys("student2")
driver.find_element(By.XPATH,'//*[@id="fmedit"]/div[7]/button').click()
sleep(3)
driver.find_element(By.LINK_TEXT,'人员管理').click()
s1 = Select(driver.find_element(By.NAME,'assetDepartId'))
print(s1.first_selected_option.text)
s1.select_by_visible_text('总经理办公室')
print(s1.first_selected_option.text)
sleep(3)
driver.quit()