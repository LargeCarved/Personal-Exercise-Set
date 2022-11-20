import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep
import ddt
import csvv


@ddt.ddt
class testnum3(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()

    @ddt.data(*csvv.get_data('testdata.csv'))
    @ddt.unpack
    def test_gongying(self, value1, value2, value3):
        driver = self.driver
        driver.get('http://116.13.1.23/ams/front/login.do')
        driver.implicitly_wait(30)
        driver.find_element(By.XPATH, '//*[@id="fmedit"]/div[1]/label[2]/input').click()
        driver.find_element(By.NAME, 'taskId').send_keys(23)
        driver.find_element(By.NAME, 'loginName').send_keys('student2')
        driver.find_element(By.NAME, 'password').send_keys('student2')
        driver.find_element(By.TAG_NAME, 'button').click()
        driver.maximize_window()

        driver.find_element(By.LINK_TEXT, '供应商').click()
        sleep(1)
        driver.find_element(By.XPATH, '//*[@id="fmsearch"]/div/button').click()
        s1 = Select(driver.find_element(By.XPATH, '//*[@id="typeId"]'))
        # print(s1.first_selected_option.text)
        s1.select_by_index(1)
        driver.find_element(By.XPATH, '//*[@id="title"]').send_keys(value1)
        driver.find_element(By.XPATH, '//*[@id="providerName"]').send_keys(value2)
        driver.find_element(By.XPATH, '//*[@id="providerPhone"]').send_keys(value3)
        driver.find_element(By.ID, 'submitButton').click()

    def tearDown(self) -> None:
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
