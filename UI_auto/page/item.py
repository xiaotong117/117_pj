from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from UI_auto.base import db_operate, list_filter, tools
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

class sp(object):
    def __init__(self,driver:webdriver.Chrome, conn):
        self.driver = driver
        self.conn = conn
        self.tools = tools(self.driver)

    def fonc1_1(self):
        self.driver.find_element_by_xpath('//*[@id="/commodity-manage$Menu"]/li[1]').click()
        self.tools.get_screenshot('商品列表')
        # self.driver.get_screenshot_as_file('截图/商品列表.png')
        time.sleep(1)


        # 下滑到列表底部，校验列表总数量
        # self.driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        js = "var q=document.querySelector('.main-content').scrollTop = 10000"
        self.driver.execute_script(js)
        time.sleep(1)
        a = self.driver.find_element_by_xpath('//*[@id="root"]/section/section/section/main/div/div/div/div[3]/div/'
                                              'div/ul/li[1]').text.split('共')[1].split('条')[0]
        sql = "select count(*) as a from item"
        b = db_operate().pull_data(self.conn, sql)[0].get('a')
        if str(a) == str(b):
            logging.info('列表总数量校验成功')
        else:
            logging.error('列表总数量校验失败')
        js2 = "var q=document.querySelector('.main-content').scrollTop = 0"
        self.driver.execute_script(js2)

    def fonc1_2(self):
        self.driver.find_element_by_xpath('//*[@id="/commodity-manage$Menu"]/li[1]').click()

        # 分别校验列表的筛选条件

        path_button = '//*[@id="root"]/section/section/section/main/div/div/div/div[1]/form/div[5]/div/div/div/div/button[1]'
        path_button_r = '//*[@id="root"]/section/section/section/main/div/div/div/div[1]/form/div[5]/div/div/div/div/button[2]'

        path_filter1 = '//*[@id="root"]/section/section/section/main/div/div/div/div[1]/form/div[1]/div[2]/div/div/input'
        path_list1 = '//*[@id="root"]/section/section/section/main/div/div/div/div[3]/div/div/div/div/div/table/tbody/tr/td[3]'
        list_filter(self.driver).filter_keys('商品名称', path_filter1, path_button, path_list1, path_button_r, '测试商品001')

        path_filter2 = '//*[@id="root"]/section/section/section/main/div/div/div/div[1]/form/div[2]/div[2]/div/div/input'
        path_list2 = '//*[@id="root"]/section/section/section/main/div/div/div/div[3]/div/div/div/div/div/table/tbody/tr[1]/td[4]'
        list_filter(self.driver).filter_keys('商品编码', path_filter2, path_button, path_list2, path_button_r, 'sp0000000026')

        path_filter3 = '//*[@id="root"]/section/section/section/main/div/div/div/div[1]/form/div[3]/div[2]/div/div/div/div/span[1]'
        path_list3 = '//*[@id="root"]/section/section/section/main/div/div/div/div[3]/div/div/div/div/div/table/tbody/tr[1]/td[5]'
        path_select3 = '//*[@id="root"]/section/section/section/main/div/div/div/div[1]/form/div[3]/div[2]/div/div/div/div[2]/div/div/div/div[2]/div/div/div[@title="公文"]'
        list_filter(self.driver).filter_list('商品类别', path_filter3, path_select3, path_button, path_list3, path_button_r, '公文')

        path_filter4 = '//*[@id="root"]/section/section/section/main/div/div/div/div[1]/form/div[4]/div[2]/div/div/div/div[1]/span[1]'
        path_list4 = '//*[@id="root"]/section/section/section/main/div/div/div/div[3]/div/div/div/div/div/table/tbody/tr[1]/td[6]'
        path_select4 = '//*[@id="root"]/section/section/section/main/div/div/div/div[1]/form/div[4]/div[2]/div/div/div/div[2]/div/div/div/div[2]/div/div/div[@title="已上架"]'
        list_filter(self.driver).filter_list('商品状态', path_filter4, path_select4, path_button, path_list4, path_button_r, '已上架')

    def fonc2(self):
        self.driver.find_element_by_xpath('//*[@id="/commodity-manage$Menu"]/li[1]').click()
        time.sleep(0.5)
        self.driver.find_element_by_xpath('//*[@id="root"]/section/section/section/main/div/div/div/div[2]/div[1]/button').click()
        time.sleep(0.5)

        # 输入商品信息
        self.driver.find_element_by_xpath('//*[@id="root"]/section/section/section/main/div/div/div[2]/article[1]/h2/button').click()
        self.driver.find_element_by_xpath('//*[@id="root"]/section/section/section/main/div/div/div[2]/article[1]/div/div/form/div[1]/div[2]/div/div/div[1]/div[2]/div/div/input').click()
        self.driver.execute_script('document.querySelector("input[placeholder=\'请输入\']").value="";')
        self.tools.send_key(self.tools.find_ele('xpath', '//*[@id="root"]/section/section/section/main/div/div/div[2]/article[1]/div/div/form/div[1]/div[2]/div/div/div[1]/div[2]/div/div/input'), '自动测试商品')
        self.driver.find_element_by_xpath('//*[@id="root"]/section/section/section/main/div/div/div[2]/article[1]/div/div/form/div[1]/div[2]/div/div/div[2]/div[2]/div/div/div').click()
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/div/div/div[@title="公文"]').click()

        self.driver.find_element_by_xpath('//*[@id="root"]/section/section/section/main/div/div/div[2]/article[1]/div/div/form/div[1]/div[2]/div/div/div[3]/div[2]/div/div/div').click()
        self.driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div[2]/div/div/div[@title="勿动-张童测试支付收款方"]').click()

        self.driver.find_element_by_xpath('//*[@id="root"]/section/section/section/main/div/div/div[2]/article[1]/div/div/form/div[1]/div[2]/div/div/div[4]/div[2]/div/div/div').click()
        self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[2]/div/div/div[@title="线上购买线上办理"]').click()

        self.driver.find_element_by_xpath('//*[@id="root"]/section/section/section/main/div/div/div[2]/article[1]/div/div/form/div[1]/div[2]/div/div/div[5]/div[2]/div/div/div').click()
        self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[2]/div/div/div').click()

        self.driver.find_element_by_xpath('//*[@id="root"]/section/section/section/main/div/div/div[2]/article[1]/div/div/form/div[1]/div[2]/div/div/div[6]/div[2]/div/div/div').click()
        self.driver.find_element_by_css_selector('div.ant-select-item[title="企业全员"]').click()

        self.driver.find_element_by_css_selector('input[placeholder="请输入30字符以内说明"]').click()
        self.driver.execute_script('document.querySelector("input[placeholder=\'请输入30字符以内说明\']").value="";')
        self.tools.send_key(self.tools.find_ele('css selector', 'input[placeholder="请输入30字符以内说明'), '商品说明123123123123')
        self.driver.find_element_by_css_selector('input[type="file"]').send_keys('/Users/zhangtong/Documents/图片/云商城/desktop_gaitubao_255x255.jpg')

        self.driver.find_element_by_xpath('//*[@id="root"]/section/section/section/main/div/div/div[2]/article[1]/div/div/form/div[2]/div/div/div/div/button[1]').click()
        time.sleep(0.5)

        # 输入商品简介
        self.driver.find_element_by_xpath('//article[2]//h2[1]//button[1]').click()
        self.tools.scroll('.main-content', '350')
        self.driver.find_element_by_css_selector('div[aria-label="富文本编辑器， main"]').send_keys('商品简介123123123')
        self.driver.find_element_by_xpath("//body/div[@id='root']/section/section/section/main/div/div/div/article[2]/div[1]/div[1]/form[1]/div[2]/div[1]/div[1]/div[1]/div[1]/button[1]").click()

        # 新增产品
        self.driver.find_element_by_xpath("//div[@class='ant-form-item-control-input-content']//button[@class='ant-btn ant-btn-link']").click()
        self.tools.send_key(self.tools.find_ele('xpath', "//textarea[@placeholder='请输入产品名称']"), '自动产品001')
        self.driver.find_element_by_css_selector('div.input-range > div:nth-child(1) > div > input').send_keys('1')
        self.driver.find_element_by_css_selector('div.input-range > div:nth-child(3) > div > input').send_keys('100')
        self.driver.find_element_by_xpath("//body/div/div/div/div/div/div/div/form/div/div/div/div/div/div/div/div/div/div/input[1]").send_keys('1024')
        self.driver.find_element_by_xpath('//body/div/div/div/div/div/div/div/form/div/div/div/div/div/div/div/div/div/div/div/input[1]').send_keys('100')
        self.driver.find_element_by_xpath("//div[@class='ant-input-number-input-wrap']//input[@placeholder='请输入8位以内正整数']").send_keys('1')
        self.driver.find_element_by_xpath("//div[5]//div[2]//div[1]//div[1]//div[1]//div[3]//div[1]//div[1]//div[1]//div[1]//div[1]//div[1]").click()
        self.driver.find_element_by_css_selector("div[title='年']").click()

        self.tools.send_key(self.tools.find_ele('xpath', "//input[@placeholder='请输入收款方标价，最多保留两位小数']"), '12.34')
        self.tools.send_key(self.tools.find_ele('xpath', "//input[@placeholder='请输入产品标价，最多保留两位小数']"), '6')
        self.tools.find_ele('xpath', "//body/div/div/div/div/div/div/div/form/div/div/div/div/div/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]").click()
        self.tools.find_ele('css selector', 'div[title="支持"]').click()
        self.tools.send_key(self.tools.find_ele('xpath', "//input[@placeholder='请输入，最多保留两位小数']"), '0.01')
        self.tools.send_key(self.tools.find_ele('xpath', "//input[@placeholder='请输入正整数']"), '88')
        self.tools.send_key(self.tools.find_ele('xpath', "//textarea[@placeholder='请输入30字以内备注']"), '测试备注信息123123123')
        self.tools.find_ele('xpath', "//div[@class='ant-modal-footer']//button[@class='ant-btn ant-btn-primary']").click()
        time.sleep(0.5)


        # 编辑预约管理
        self.tools.scroll('.main-content', '500')
        self.tools.find_ele('xpath', "//article[@class='ant-typography form reservation-info']//h2[@class='ant-typography']//span").click()
        self.tools.find_ele('xpath', "//label[@class='ant-radio-wrapper']").click()
        self.tools.scroll('.main-content', '500')
        self.tools.find_ele('xpath', "//div[@class='ant-checkbox-group']//label[1]").click()
        self.tools.find_ele('xpath', "//div[@class='ant-checkbox-group']//label[2]").click()
        self.tools.find_ele('xpath', "//div[@class='ant-checkbox-group']//label[3]").click()
        self.tools.find_ele('xpath', "//div[@class='ant-checkbox-group']//label[4]").click()
        self.tools.find_ele('xpath', "//div[@class='ant-checkbox-group']//label[5]").click()
        self.tools.find_ele('xpath', "//div[@class='ant-checkbox-group']//label[6]").click()
        self.tools.find_ele('xpath', "//div[@class='ant-checkbox-group']//label[7]").click()
        self.tools.find_ele('xpath', "//div[@class='sc-bdVaJa jDpllU form__footer']//button[@class='ant-btn ant-btn-primary']").click()
        self.tools.scroll('.main-content', '500')
        self.tools.find_ele('xpath', "//div[contains(@class,'page-footer')]//button[@class='ant-btn ant-btn-primary']").click()
        time.sleep(0.5)

        try:
            assert '新增成功' in self.driver.page_source
            logging.info('新建商品校验成功')

        except Exception:
            logging.error('新建商品校验失败')

    def fonc3(self):
        self.driver.find_element_by_xpath('//*[@id="/commodity-manage$Menu"]/li[1]').click()
        time.sleep(0.5)

        # 进入商品详情
        self.tools.send_key(self.tools.find_ele('xpath', '//*[@id="root"]/section/section/section/main/div/div/div/div[1]/form/div[2]/div[2]/div/div/input'), 'sp0000000050')
        self.tools.find_ele('xpath', '//*[@id="root"]/section/section/section/main/div/div/div/div[1]/form/div[5]/div/div/div/div/button[1]').click()
        time.sleep(0.5)
        self.tools.find_ele('xpath', "//td[@class='ant-table-cell ant-table-selection-column']//span[@class='ant-checkbox']").click()
        self.tools.find_ele('xpath', "//div[@class='ant-space ant-space-horizontal ant-space-align-center']//div[2]//button[1]").click()
        time.sleep(0.5)

        try:
            assert '商品详情' in self.driver.page_source
            logging.info('进入商品详情页成功')

        except Exception as e:
            logging.error('进入商品详情页失败，输出信息如下：{}'.format(e))

        sql = "select item_code '商品编码',item.name '商品名称',category.name '商品类别',supplier.name '收款方公司',buy_type" \
              " '购买方式',caiyun_type '彩云省份',user_type '用户类别',item.remark '商品说明',introduction '商品简介'," \
              "pre_manager_flag '预约管理' from item, category, supplier where item.cat_id = category.id and item.supplier_id = supplier.id and item_code = 'sp0000000050'"
        sql_data = db_operate().pull_data(self.conn, sql)[0]

        web_data = {}
        web_data['商品编码'] = self.tools.find_ele('xpath', "//div[@class='ant-card-body']//div[1]//div[2]//div[1]//div[1]//span[1]").text
        web_data['商品名称'] = self.tools.find_ele('xpath', "//div[@class='ant-col ant-col-20']//div[2]//div[2]//div[1]//div[1]//span[1]").text
        web_data['商品类别'] = self.tools.find_ele('xpath', "//div[3]//div[2]//div[1]//div[1]//p[1]").text
        web_data['收款方公司'] = self.tools.find_ele('xpath', "//div[4]//div[2]//div[1]//div[1]//p[1]").text
        buy_type = self.tools.find_ele('xpath', "//div[5]//div[2]//div[1]//div[1]//p[1]").text
        if buy_type == '线上购买线上办理':
            web_data['购买方式'] = 1
        elif buy_type == '线上购买线下办理':
            web_data['购买方式'] = 2
        elif buy_type == '线上预约':
            web_data['购买方式'] = 3

        caiyun_type = self.tools.find_ele('xpath', "//div[6]//div[2]//div[1]//div[1]//p[1]").text
        if caiyun_type == '移动彩云':
            web_data['彩云省份'] = 1
        elif caiyun_type == '广西':
            web_data['彩云省份'] = 18

        user_type = self.tools.find_ele('xpath', "//div[7]//div[2]//div[1]//div[1]//p[1]").text
        if user_type == '企业管理员':
            web_data['用户类别'] = 1
        elif user_type == '企业全员':
            web_data['用户类别'] = 2

        web_data['商品说明'] = self.tools.find_ele('xpath', "//div[8]//div[2]//div[1]//div[1]//span[1]").text
        # self.tools.scroll('.main-content', '350')
        web_data['商品简介'] = self.driver.execute_script("return document.querySelector('div.ck-content').innerHTML")
        if self.tools.find_ele('xpath', "//div[@class='ant-form-item-control-input-content']//div//p[contains(@class,'preview-text')]").text == '不支持':
            web_data['预约管理'] = 0
        else:
            web_data['预约管理'] = 1
            if '公司名称' in self.driver.page_source:
                web_data['预约管理'] += 2
            if '联系人姓名' in self.driver.page_source:
                web_data['预约管理'] += 4
            if '身份证号' in self.driver.page_source:
                web_data['预约管理'] += 8
            if '身份证正反面' in self.driver.page_source:
                web_data['预约管理'] += 16
            if '联系电话' in self.driver.page_source:
                web_data['预约管理'] += 32
            if '联系地址' in self.driver.page_source:
                web_data['预约管理'] += 64
            if '预约时间' in self.driver.page_source:
                web_data['预约管理'] += 128

        if web_data == sql_data:
            logging.info('查看商品校验成功')
        else:
            logging.error('查看商品校验失败')

    def fonc4(self):
        self.driver.find_element_by_xpath('//*[@id="/commodity-manage$Menu"]/li[1]').click()
        time.sleep(0.5)

        # 进入商品详情
        self.tools.send_key(self.tools.find_ele('xpath',
                                                '//*[@id="root"]/section/section/section/main/div/div/div/div[1]/form/div[2]/div[2]/div/div/input'),
                            'sp0000000050')
        self.tools.find_ele('xpath',
                            '//*[@id="root"]/section/section/section/main/div/div/div/div[1]/form/div[5]/div/div/div/div/button[1]').click()
        time.sleep(0.5)
        self.tools.find_ele('xpath',
                            "//td[@class='ant-table-cell ant-table-selection-column']//span[@class='ant-checkbox']").click()
        self.tools.find_ele('xpath',
                            "//div[3]//button[1]").click()
        time.sleep(0.5)

        try:
            assert '编辑商品' in self.driver.page_source
            logging.info('进入商品编辑页成功')

        except Exception as e:
            logging.error('进入商品编辑页失败，输出信息如下：{}'.format(e))

        # 输入商品信息
        self.driver.find_element_by_xpath('//*[@id="root"]/section/section/section/main/div/div/div[2]/article[1]/h2/button').click()
        self.driver.find_element_by_css_selector("input[placeholder='请输入']").click()
        self.driver.find_element_by_xpath().clear()
        # self.driver.execute_script('document.querySelector("input[placeholder=\'请输入\']").value="";')
        self.tools.send_key(self.tools.find_ele('css selector', "input[placeholder='请输入']"), '自动测试商品-1')
        self.driver.find_element_by_xpath('//div[3]//div[2]//div[1]//div[1]//div[1]//div[1]//span[2]').click()
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/div/div/div[@title="云盘"]').click()

        self.driver.find_element_by_xpath('//div[4]//div[2]//div[1]//div[1]//div[1]//div[1]//span[2]').click()
        self.driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div[2]/div/div/div[@title="陈凯丽测试供应商"]').click()

        self.driver.find_element_by_xpath('//div[5]//div[2]//div[1]//div[1]//div[1]//div[1]//span[2]').click()
        self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[2]/div/div/div[@title="线上预约"]').click()

        self.driver.find_element_by_xpath('//div[6]//div[2]//div[1]//div[1]//div[1]//div[1]//span[2]').click()
        self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[2]/div/div/div').click()

        self.driver.find_element_by_xpath('//div[7]//div[2]//div[1]//div[1]//div[1]//div[1]//span[2]').click()
        self.driver.find_element_by_css_selector('div.ant-select-item[title="企业管理员"]').click()

        self.driver.find_element_by_css_selector('input[placeholder="请输入30字符以内说明"]').click()
        # self.driver.execute_script('document.querySelector("input[placeholder=\'请输入30字符以内说明\']").value="";')
        self.tools.send_key(self.tools.find_ele('css selector', 'input[placeholder="请输入30字符以内说明'), '商品说明123123123123')
        self.driver.find_element_by_css_selector('input[type="file"]').send_keys('/Users/zhangtong/Documents/图片/云商城/desktop_gaitubao_255x255.jpg')

        self.driver.find_element_by_xpath('//*[@id="root"]/section/section/section/main/div/div/div[2]/article[1]/div/div/form/div[2]/div/div/div/div/button[1]').click()
        time.sleep(0.5)

        # # 输入商品简介
        # self.driver.find_element_by_xpath('//article[2]//h2[1]//button[1]').click()
        # self.tools.scroll('.main-content', '350')
        # self.tools.send_key(self.tools.find_ele('css selector', 'div[aria-label="富文本编辑器， main"]'), '商品简介123123123')
        # # self.driver.find_element_by_css_selector('div[aria-label="富文本编辑器， main"]').send_keys('商品简介123123123')
        # self.driver.find_element_by_xpath("//body/div[@id='root']/section/section/section/main/div/div/div/article[2]/div[1]/div[1]/form[1]/div[2]/div[1]/div[1]/div[1]/div[1]/button[1]").click()
        #
        # # 新增产品
        # self.driver.find_element_by_xpath(
        #     "//div[@class='ant-form-item-control-input-content']//button[@class='ant-btn ant-btn-link']").click()
        # self.tools.send_key(self.tools.find_ele('xpath', "//textarea[@placeholder='请输入产品名称']"), '自动产品002')
        # self.driver.find_element_by_css_selector('div.input-range > div:nth-child(1) > div > input').send_keys('1')
        # self.driver.find_element_by_css_selector('div.input-range > div:nth-child(3) > div > input').send_keys('100')
        # self.driver.find_element_by_xpath(
        #     "//body/div/div/div/div/div/div/div/form/div/div/div/div/div/div/div/div/div/div/input[1]").send_keys(
        #     '1024')
        # self.driver.find_element_by_xpath(
        #     '//body/div/div/div/div/div/div/div/form/div/div/div/div/div/div/div/div/div/div/div/input[1]').send_keys(
        #     '100')
        # self.driver.find_element_by_xpath(
        #     "//div[@class='ant-input-number-input-wrap']//input[@placeholder='请输入8位以内正整数']").send_keys('1')
        # self.driver.find_element_by_xpath(
        #     "//div[5]//div[2]//div[1]//div[1]//div[1]//div[3]//div[1]//div[1]//div[1]//div[1]//div[1]//div[1]").click()
        # self.driver.find_element_by_css_selector("div[title='年']").click()
        #
        # self.tools.send_key(self.tools.find_ele('xpath', "//input[@placeholder='请输入收款方标价，最多保留两位小数']"), '12.34')
        # self.tools.send_key(self.tools.find_ele('xpath', "//input[@placeholder='请输入产品标价，最多保留两位小数']"), '6')
        # self.tools.find_ele('xpath',
        #                     "//body/div/div/div/div/div/div/div/form/div/div/div/div/div/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]").click()
        # self.tools.find_ele('css selector', 'div[title="支持"]').click()
        # self.tools.send_key(self.tools.find_ele('xpath', "//input[@placeholder='请输入，最多保留两位小数']"), '0.01')
        # self.tools.send_key(self.tools.find_ele('xpath', "//input[@placeholder='请输入正整数']"), '88')
        # self.tools.send_key(self.tools.find_ele('xpath', "//textarea[@placeholder='请输入30字以内备注']"), '测试备注信息123123123')
        # self.tools.find_ele('xpath',
        #                     "//div[@class='ant-modal-footer']//button[@class='ant-btn ant-btn-primary']").click()
        # time.sleep(0.5)
        #
        # # 编辑产品
        # self.driver.find_element_by_xpath("//tr[1]//td[8]//a[1]").click()
        # self.tools.send_key(self.tools.find_ele('xpath', "//textarea[@placeholder='请输入产品名称']"), '自动产品003')
        # self.tools.find_ele('xpath', "//div[3]//div[2]//div[1]//div[1]//div[1]//div[3]//div[1]//div[1]//div[1]//div[1]//div[1]//label[1]//span[1]//input[1]")
        # self.tools.find_ele('xpath', "//div[4]//div[2]//div[1]//div[1]//div[1]//div[4]//div[1]//div[1]//div[1]//div[1]//div[1]//label[1]//span[1]//input[1]")
        # self.tools.find_ele('xpath', "//div[5]//div[2]//div[1]//div[1]//div[1]//div[3]//div[1]//div[1]//div[1]//div[1]//div[1]//label[1]//span[1]//input[1]")
        # self.tools.find_ele('xpath', "//span[@class='ant-checkbox']//input[@class='ant-checkbox-input']")
        # self.tools.send_key(self.tools.find_ele('xpath', "//input[@placeholder='请输入收款方标价，最多保留两位小数']"), '9.23')
        # self.tools.send_key(self.tools.find_ele('xpath', "//input[@placeholder='请输入产品标价，最多保留两位小数']"), '4')
        # self.tools.find_ele('xpath',
        #                     "//body/div/div/div/div/div/div/div/form/div/div/div/div/div/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]").click()
        # self.tools.find_ele('css selector', 'div[title="不支持"]').click()
        # self.tools.send_key(self.tools.find_ele('xpath', "//textarea[@placeholder='请输入30字以内备注']"), '修改测试备注信息123123123')
        # self.tools.find_ele('xpath',
        #                     "//div[@class='ant-modal-footer']//button[@class='ant-btn ant-btn-primary']").click()
        # time.sleep(0.5)
        #
        # # 产品排序
        # ele = self.tools.find_ele('xpath', '//body//tr[2]')
        # ActionChains(self.driver).drag_and_drop_by_offset(ele, 0, 50).perform()
        #
        # # 删除产品
        # self.tools.find_ele('xpath', '//tr[1]//td[8]//a[2]').click()
        # self.tools.find_ele('xpath', "//div[@class='ant-modal-confirm-btns']//button[@class='ant-btn ant-btn-primary']").click()
        #
        # # 编辑预约管理
        # self.tools.scroll('.main-content', '500')
        # self.tools.find_ele('xpath', "//article[@class='ant-typography form reservation-info']//h2[@class='ant-typography']//span").click()
        # self.tools.find_ele('xpath', "//label[@class='ant-radio-wrapper']").click()
        # self.tools.find_ele('xpath', "//div[@class='sc-bdVaJa jDpllU form__footer']//button[@class='ant-btn ant-btn-primary']").click()
        # self.tools.scroll('.main-content', '500')
        # self.tools.find_ele('xpath', "//div[contains(@class,'page-footer')]//button[@class='ant-btn ant-btn-primary']").click()
        # time.sleep(0.5)
        #
        # try:
        #     assert '修改成功' in self.driver.page_source
        #     logging.info('修改商品校验成功')
        #
        # except Exception:
        #     logging.error('修改商品校验失败')

