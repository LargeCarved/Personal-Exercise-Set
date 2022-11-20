import unittest
from selenium import webdriver
from AddPage import AddPage
from LoginPage import LoginPage
class Test_Add(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
    def test_login_add(self):
        url = 'http://116.13.1.23/ams/front/login.do'
        lg = LoginPage(self.driver)
        lg.open(url)
        lg.click_admin()
        lg.login(23, 'student1', 'student1')
        lg.click_login()
        add = AddPage(self.driver)
        add.click_brand()
        add.click_add()
        add.add_brand('测试数据', 'pp1007')
        add.click_submit()
    @classmethod
    def tearDownClass(cls) -> None:
        time.sleep(2)
        cls.driver.quit()
if __name__ == '__main__':
    unittest.main()