from selenium.webdriver.common.by import By
import BasePage
class LoginPage(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver)

    def open(self, url):
        self.get(url)

    def click_login(self):
        self.left_click(By.CLASS_NAME, 'blue-button')

    def click_admin(self):
        self.left_click(By.XPATH, '//*[@id="fmedit"]/div[1]/label[2]/input')

    def login(self, taskId=0, loginName='', password=''):
        self.send_text(taskId, By.ID, "taskId")
        self.send_text(loginName, By.ID, "loginName")
        self.send_text(password, By.ID, "password")
