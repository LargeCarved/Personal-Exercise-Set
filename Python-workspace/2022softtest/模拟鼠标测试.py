from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()

driver.get('http://sahitest.com/demo/label.htm')

input1 = driver.find_elements(By.TAG_NAME,'input')[3]
input2 = driver.find_elements(By.TAG_NAME,'input')[4]

action = ActionChains(driver)
input1.click()
action.send_keys('Test Keys').perform()
sleep(2)
action.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()  # ctrl+a
sleep(2)
action.key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()  # ctrl+c
sleep(2)
action.key_down(Keys.CONTROL, input2).send_keys('v').key_up(Keys.CONTROL).perform()  # ctrl+v
sleep(2)
print(input1.get_attribute('value'))
print(input2.get_attribute('value'))
driver.quit()