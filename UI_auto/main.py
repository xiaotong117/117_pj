from UI_auto.page.login import slnm
from UI_auto.page.item import sp
from UI_auto.base import db_operate
from selenium import webdriver
import time, logging

DB_CONFIG = {
    'host': '10.0.10.42',
    'port': 3306,
    'user': 'root',
    'passwd': 'shinemo123',
    'db': 'csm'
}

if __name__ == "__main__":
    # t = time.strftime("%H-%M-%S", time.localtime())
    logging.basicConfig(level=logging.INFO)
    conn = db_operate().db_connect(DB_CONFIG)
    drive = webdriver.Chrome()
    a = slnm(drive)
    b = sp(drive, conn)

    a.openurl(url='http://admin.jituancaiyun.net/cloud-mall-admin/index.html#/login')
    a.login('15958032925', '888888')
    time.sleep(1)
    # b.fonc1_1()
    # b.fonc1_2()
    # b.fonc2()
    # b.fonc3()
    b.fonc4()



    a.logot()
    a.closeurl()
    db_operate().db_disconnect(conn)