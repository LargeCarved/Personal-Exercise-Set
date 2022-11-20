import csvv
import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from ddt import data,ddt,unpack

@ddt
class testnum3(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()

    @data(*csvv.getdata('testdata.csv'))
    @unpack
    def test_num3(self,v1,v2,v3):
        driver = self.driver
        driver.implicitly_wait(5)
        driver.get("http://116.13.1.23/ams/front/login.do")
        driver.find_element(By.ID, "taskId").send_keys(23)
        driver.find_element(By.ID, "loginName").send_keys("student2")
        driver.find_element(By.NAME, "password").send_keys("student2")
        driver.find_element(By.TAG_NAME, 'button').click()
        driver.find_element(By.PARTIAL_LINK_TEXT, '存放地点').click()
        driver.find_element(By.XPATH,'//*[@id="fmsearch"]/div/button').click()
        driver.find_element(By.XPATH,'//*[@id="title"]').send_keys(v1)
        driver.find_element(By.XPATH,'//*[@id="remark"]').send_keys(v2)
        driver.find_element(By.XPATH,'//*[@id="submitButton"]').click()
        sleep(2)
        text = driver.switch_to.alert.text
        self.assertEqual(v3,text)

if __name__=='__main__':
    unittest.main()