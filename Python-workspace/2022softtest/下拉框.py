import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.support.ui import Select


class SelectStudy(unittest.TestCase):

    def setUp(self):
        # 创建一个Chrome WebDriver的实例
        self.driver = webdriver.Chrome()

    # 选择页面第一个下拉框，依次选择值O1-O3
    def test_selectO1ToO3(self):
        driver = self.driver
        driver.get('http://sahitest.com/demo/selectTest.htm')
        # 实例化Select
        s1 = Select(driver.find_element(By.ID,'s1Id'))
        # 查看选择框的默认值
        print(s1.first_selected_option.text)
        # 选择第二个选项o1
        s1.select_by_index(1)
        time.sleep(3)
        # 为了方便查看效果，可以加上等待时间
        time.sleep(3)
        # 选择value="o2"的项，value是option标签的一个属性值，并不是显示在下拉框中的值
        s1.select_by_value("o2")
        # 查看选中选择框的默认值
        print(s1.first_selected_option.text)
        time.sleep(3)
        # 选择text="o3"的值，即在下拉时我们可以看到的文本，visible_text是在option标签中间的值，是显示在下拉框的值
        s1.select_by_visible_text("o3")
        time.sleep(3)
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()