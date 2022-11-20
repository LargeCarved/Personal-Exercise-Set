from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import unittest
class testnum2(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()

    def test_denglu01(self):
        driver = self.driver
        driver.get('http://116.13.1.23/ams/front/login.do')
        driver.find_element(By.NAME,'taskId').send_keys(23)
        driver.find_element(By.NAME,'loginName').send_keys('student2')
        driver.find_element(By.NAME,'password').send_keys('student2')
        driver.find_element(By.XPATH,'//*[@id="fmedit"]/div[7]/button').click()
        driver.find_element(By.PARTIAL_LINK_TEXT,'取得方式').click()

    def test_denglu02(self):
        driver = self.driver
        driver.get('http://116.13.1.23/ams/front/login.do')
        driver.find_element(By.ID,'taskId').send_keys(23)
        driver.find_element(By.ID,'loginName').send_keys('student2')
        driver.find_element(By.ID,'password').send_keys('student2')
        driver.find_element(By.CSS_SELECTOR,'.blue-button').click()
        driver.find_element(By.LINK_TEXT,'个人信息').click()

    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
