import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
class loginDemo2(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()

    def test_denglu01(self):
        self.driver.get('http://116.13.1.23/ams/front/login.do')
        self.driver.find_element(By.ID,'taskId').send_keys('23')
        self.driver.find_element(By.ID,'loginName').send_keys('student2')
        self.driver.find_element(By.ID,'password').send_keys('student2')
        self.driver.find_element(By.XPATH,'//*[@id="fmedit"]/div[7]/button').click()
        self.driver.find_element(By.PARTIAL_LINK_TEXT,'取得方式').click()

    def tearDown(self) -> None:
        sleep(2)
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()