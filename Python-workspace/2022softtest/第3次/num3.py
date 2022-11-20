from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import unittest
import ddt
import csvv

@ddt.ddt
class testnum2(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
    @ddt.data(*csvv.getdata('testdata.csv'))
    @ddt.unpack
    def test_denglu01(self,v1,v2,v3):
        driver = self.driver
        driver.implicitly_wait(5)
        driver.get('http://116.13.1.23/ams/front/login.do')
        driver.find_element(By.NAME,'taskId').send_keys(23)
        driver.find_element(By.ID,'loginName').send_keys('student2')
        driver.find_element(By.NAME,'password').send_keys('student2')
        driver.find_element(By.TAG_NAME,'button').click()
        driver.find_element(By.PARTIAL_LINK_TEXT,'存放地点').click()
        driver.find_element(By.XPATH,'//*[@id="fmsearch"]/div/button').click()
        driver.find_element(By.XPATH,'//*[@id="title"]').send_keys(v1)
        driver.find_element(By.XPATH, '//*[@id="remark"]').send_keys(v2)
        driver.find_element(By.XPATH,'//*[@id="submitButton"]').click()
        text = driver.switch_to.alert.text
        self.assertEqual(v3,text)

    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
