from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from UI_auto.base import slnm, db_operate
import time
import logging


'''
对商品管理页面的校验：
1、列表页查看截图+筛选
2、新增商品
3、查看商品
4、编辑商品
5、上架/下架
'''

class sp(slnm):
    def __init__(self,driver:webdriver.Chrome, conn):
        super(sp, self).__init__(driver)
        self.conn = conn

    def fonc1_1(self):
        self.driver.find_element_by_xpath("//*[@id=\"/commodity-manage$Menu\"]/li[1]").click()
        # self.driver.get_screenshot_as_file('截图/商品列表.png')


        # 下滑到列表底部，校验列表总数量
        # self.driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        js = "var q=document.querySelector('.main-content').scrollTop = 10000"
        self.driver.execute_script(js)
        time.sleep(1)
        a = self.driver.find_element_by_xpath("//*[@id=\"root\"]/section/section/section/main/div/div/div/div[3]/div/"
                                              "div/ul/li[1]").text.spilt('共')[1]
        sql = "select count(*) from item"
        b = db_operate().pull_data(self.conn, sql).spilt(':')[1]
        if a == b:
            pass
        else:
            logging.error('列表总数量校验失败')

    def fonc1_2(self):
        # 分别校验列表的筛选条件
        self.driver.find_element_by_xpath("//*[@id=\"root\"]/section/section/section/main/div/div/div/div[1]/form/"
                                          "div[1]/div[2]/div/div/input").send_keys('测试商品001')
        self.driver.find_element_by_xpath("//*[@id=\"root\"]/section/section/section/main/div/div/div/div[1]/form/"
                                          "div[5]/div/div/div/div/button[1]").click()
        try:
            if self.driver.find_element_by_xpath('//*[@id="root"]/section/section/section/main/div/div/div/div[3]/'
                                                 'div/div/div/div/div/table/tbody/tr/td[3]').text == '测试商品001':
                pass
            else:
                logging.error("商品名称筛选错误")
        except:
            logging.error("商品名称筛选错误")


        self.driver.find_element_by_xpath("//*[@id=\"root\"]/section/section/section/main/div/div/div/div[1]/form/"
                                          "div[1]/div[2]/div/div/input").send_keys('测试商品001')
        self.driver.find_element_by_xpath("//*[@id=\"root\"]/section/section/section/main/div/div/div/div[1]/form/"
                                          "div[5]/div/div/div/div/button[1]").click()
        try:
            if self.driver.find_element_by_xpath('//*[@id="root"]/section/section/section/main/div/div/div/div[3]/'
                                                 'div/div/div/div/div/table/tbody/tr/td[3]').text == '测试商品001':
                pass
            else:
                logging.error("商品名称筛选错误")
        except:
            logging.error("商品名称筛选错误")

