from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import pymysql
import logging
import time, os
from datetime import datetime, date


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

class list_filter(object):
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def filter_keys(self, name, path_filter, path_button, path_list, path_button_r, keys):
        try:
            self.driver.find_element_by_xpath(path_filter).send_keys(keys)
            self.driver.find_element_by_xpath(path_button).click()
            time.sleep(0.5)
            try:
                if self.driver.find_element_by_xpath(path_list).text == keys:
                    logging.info(name + "筛选校验通过")
                else:
                    logging.error(name + "筛选错误")
            except:
                logging.error(name + "筛选错误")
        except:
            logging.error(name + "xpath查找失败")
        finally:
            self.driver.find_element_by_xpath(path_button_r).click()

    def filter_list(self, name, path_filter, path_select, path_button, path_list, path_button_r, keys):
        try:
            self.driver.find_element_by_xpath(path_filter).click()
            time.sleep(0.5)
            self.driver.find_element_by_xpath(path_select).click()
            self.driver.find_element_by_xpath(path_button).click()
            time.sleep(0.5)
            try:
                if self.driver.find_element_by_xpath(path_list).text == keys:
                    logging.info(name + "筛选校验通过")
                else:
                    logging.error(name + "筛选错误")
            except:
                logging.error(name + "筛选错误")
        except:
            logging.error(name + "xpath查找失败", exc_info=True)
        finally:
            self.driver.find_element_by_xpath(path_button_r).click()


class tools(object):

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def find_ele(self, by, path):
        '''

        :param by:  "id" "xpath" "link text" "partial link text" "name" "tag name" "class name" "css selector"
        :param path:
        :return:
        '''
        try:
            ele = WebDriverWait(self.driver, 10, 0.5).until(lambda d: d.find_element(by, path))
        except Exception as e:
            logging.error("path can't find", exc_info=True)
            raise e
        else:
            return ele

    def send_key(self, selector, keys):
        try:
            # selector.clear()
            # selector.send_keys(Keys.COMMAND, "a")
            ActionChains(self.driver).double_click(selector).perform()
            selector.send_keys(keys)
        except Exception as e:
            raise e

    def get_screenshot(self, name):
        self.driver.get_screenshot_as_file('截图/商品列表.png')
        picture_path = os.path.join('截图', str(date.today()))
        if not os.path.exists(picture_path):
            os.makedirs(picture_path)  # 生成多级目录
        picture_name = picture_path + '\\' + datetime.now().strftime('%H_%M_%S') + name + '.png'
        try:
            self.driver.get_screenshot_as_file(picture_name)
        except Exception as e:
            raise e
        else:
            return picture_name

    def show_wait(self, fnuc):
        return WebDriverWait(self.driver, 5, 0.5).until(fnuc)

    def scroll(self, querySelector='.main-content', num='1000'):
        js = "var q=document.querySelector('" + querySelector + "').scrollTop = " + num
        self.driver.execute_script(js)
        time.sleep(1)
