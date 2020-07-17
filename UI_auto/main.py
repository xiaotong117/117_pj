from UI_auto.item import sp
from UI_auto.base import db_operate
from selenium import webdriver
import time

DB_CONFIG = {
    'host': '10.0.10.42',
    'port': 3306,
    'user': 'root',
    'passwd': 'shinemo123',
    'db': 'csm'
}

if __name__ == "__main__":
    t = time.strftime("%H-%M-%S", time.localtime())
    conn = db_operate().db_connect(DB_CONFIG)

    a = sp(webdriver.Chrome(), conn)
    a.openurl(url='http://admin.jituancaiyun.net/cloud-mall-admin/index.html#/login')
    a.login('15958032925', '888888')
    time.sleep(1)
    a.fonc1_1(t)



    a.logot()
    a.closeurl()
    db_operate().db_disconnect(conn)