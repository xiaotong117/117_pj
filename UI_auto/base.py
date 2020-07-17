from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import pymysql
import logging


class slnm(object):

    def __init__(self,driver:webdriver.Chrome):
        self.driver = driver

    def openurl(self, url):
        self.driver.get(url)
        self.driver.maximize_window()

    def login(self, mobile, password):
        # 输入账号密码
        self.driver.find_element_by_class_name("ant-input").send_keys(mobile)
        self.driver.find_element_by_xpath("//*[@id=\"root\"]/div/div[2]/div[1]/form/div[2]/div/div/div/input").send_keys(
            password)
        self.driver.find_element_by_xpath("//*[@id=\"root\"]/div/div[2]/div[1]/form/button").click()


    def logot(self):
        wode = self.driver.find_element_by_xpath('//*[@id="root"]/section/header/div[2]/span[1]')
        ActionChains(self.driver).move_to_element(wode).perform()
        self.driver.implicitly_wait(1)
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div/ul/li[2]').click()


    def closeurl(self):
        self.driver.quit()



class db_operate():

    def db_connect(self, DB_CONFIG):
        try:
            conn = pymysql.connect(**DB_CONFIG)
            return conn
        except:
            logging.error("DB连接错误", exc_info=True)

    def db_disconnect(self, conn):
        try:
            conn.close()
        except:
            logging.error("DB连接错误", exc_info=True)

    def pull_data(self, conn, sql):
        try:
            cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
            cursor.execute(sql)
            result = cursor.fetchall()
            return result

        except:
            cursor.close()
            logging.error("DB连接错误", exc_info=True)