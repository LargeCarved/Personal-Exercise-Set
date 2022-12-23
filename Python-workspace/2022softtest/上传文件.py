import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

class testnum4(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()

    def test_gongying(self):
        driver = self.driver
        driver.get('http://116.13.1.23/ams/front/login.do')
        driver.implicitly_wait(30)
        driver.find_element(By.ID, 'taskId').send_keys(23)
        driver.find_element(By.ID, 'loginName').send_keys('student2')
        driver.find_element(By.ID, 'password').send_keys('student2')
        driver.find_element(By.TAG_NAME, 'button').click()
        driver.maximize_window()
        driver.find_element(By.LINK_TEXT, '资产入库').click()
        sleep(1)
        driver.find_element(By.XPATH, '//*[@id="fmsearch"]/div/button[2]').click()
        sleep(1)
        driver.find_element(By.XPATH, '//*[@id="rt_rt_1gialj7p45ub1pgh13vl1trl1kak1"]/label').send_keys('D/桌面/test.jpg')
        sleep(4)
        # text = driver.switch_to.alert.text
        # try:
        # self.assertEqual(value2,text)
        # except:
        #     print('不是预期结果')

    def tearDown(self) -> None:
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
