from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
# driver = webdriver.Chrome()
# driver.implicitly_wait(5)
# driver.get('http://116.13.1.23/ams/front/login.do')
# driver.find_element(By.NAME,'taskId').send_keys(23)
# driver.find_element(By.NAME,'loginName').send_keys('student2')
# driver.find_element(By.NAME,'password').send_keys('student1')
# # print(driver.find_element(By.TAG_NAME,'button'))
# # print(driver.find_elements(By.TAG_NAME,'button'))
# button = driver.find_element(By.TAG_NAME,'button')
# print(button.text)
# # button.click()
# ActionChains(driver).double_click(button).perform()
# driver.get_screenshot_as_file('denglu.png')

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get('http://sahitest.com/demo/clicks.htm')
click_btn = driver.find_element(By.XPATH,'//input[@value="click me"]')  # 单击按钮
doubleclick_btn = driver.find_element(By.XPATH,'//input[@value="dbl click me"]')  # 双击按钮
rightclick_btn = driver.find_element(By.XPATH,'//input[@value="right click me"]')  # 右键单击按钮
ActionChains(driver).click(click_btn).double_click(doubleclick_btn).context_click(rightclick_btn).perform()  # 链式用法
print (driver.find_element(By.NAME,'t2').get_attribute('value'))
sleep(2)
driver.quit()