from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
from UI_auto.base import tools


class slnm(object):

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.tools = tools(self.driver)

    def openurl(self, url):
        self.driver.get(url)
        self.driver.maximize_window()

    def login(self, mobile, password):
        '''
        输入账号密码
        :param mobile: 账号
        :param password: 密码
        :return:
        '''
        self.tools.send_key(self.tools.find_ele('class name', 'ant-input'), mobile)
        self.tools.send_key(self.tools.find_ele(
            'xpath', '//*[@id="root"]/div/div[2]/div[1]/form/div[2]/div/div/div/input'), password)
        self.tools.find_ele('xpath', '//*[@id="root"]/div/div[2]/div[1]/form/button').click()

    def logot(self):
        wode = self.tools.find_ele('xpath', '//*[@id="root"]/section/header/div[2]/span[1]')
        ActionChains(self.driver).move_to_element(wode).perform()
        time.sleep(0.5)
        self.tools.find_ele('css selector', 'ul.ant-dropdown-menu > li:nth-child(2)').click()

    def closeurl(self):
        self.driver.quit()


if __name__ == '__main__':
    pass
