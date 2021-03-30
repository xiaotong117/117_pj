# -*- coding: utf-8 -*-
# @Time : 2018/5/15 10:27
# @Author : didi_order_check
# @Email : xup@shinemo.com
# @File : plandispose.py
# @Software: PyCharm Community Edition

import configparser
import mysql.connector
import sys
from global_func.global_log import logger

log_config = './config/dbconfig.conf'
class MysqlFunction:

    def __init__(self,DBSelection):
        #生成config对象
        conf = configparser.ConfigParser()
        #读配置文件
        conf.read(log_config,encoding='utf-8')
        # 指定section，option读取值
        try:
            #取host
            self.host = conf.get(DBSelection, 'host')
            # 取端口
            self.port = conf.get(DBSelection, 'port')
            # 取数据库用户名
            self.user = conf.get(DBSelection, 'user')
            # 取数据库密码
            self.passwd = conf.get(DBSelection, 'passwd')
            # 取数据库table名称
            self.dbname = conf.get(DBSelection, 'dbname')
            # 取encodeing
            self.charset = conf.get(DBSelection, 'charset')
        except Exception as e:
            logger.error('初始化数据参数失败：%s' % e)
            sys.exit()
        try:
            # 打开数据库连接
            self.dbconnect = mysql.connector.connect(host=self.host, port=self.port, user=self.user, password=self.passwd, database=self.dbname, charset=self.charset)
        except Exception as e:
            logger.error('初始化数据连接失败：%s' % e)
            sys.exit()
    def getDBConnect(self):
        return self.dbconnect
    def getHost(self):
        return self.host
    def getPort(self):
        return self.port
    def getUser(self):
        return self.user
    def getPasswd(self):
        return self.passwd
    def getDbname(self):
        return self.dbname
    def getCharset(self):
        return self.charset
    #关闭数据库
    def close(self):
        self.dbconnect.close
    #创建数据库表
    def createSqlTable(self, sqlTable):
        try:
            # 使用cursor()方法获取操作游标
            dbCursor = self.dbconnect.cursor()
            #使用execute方法执行SQL语句
            dbCursor.execute(sqlTable)
            #提交保存
            dbCursor.execute('commit')
            #关闭
            dbCursor.close()
            return True
        except Exception as e:
            logger.error('创建数据库表操作失败：%s' % e)
            dbCursor.execute('rollback')
            dbCursor.close()
            exit()
    #更新数据库表
    def updateSqlTable(self, query, data):
        query = query % data
        try:
            dbCursor = self.dbconnect.cursor()
            dbCursor.execute(query)
            dbCursor.execute('commit')
            dbCursor.close()
            return ('',True)
        except Exception as e:
            logger.error('执行数据库更新操作失败：%s' % e)
            dbCursor.execute('rollback')
            dbCursor.close()
            return (e, False)
    #插入数据库数据
    def insertSqlTable(self, query, data):
        try:
            dbCursor = self.dbconnect.cursor()
            dbCursor.execute(query, data)
            dbCursor.execute('commit')
            dbCursor.close()
            return True
        except Exception as e:
            logger.error('执行数据库插入操作失败：%s' % e)
            dbCursor.execute('rollback')
            dbCursor.close()
            exit()
    def selectOneRecord(self, query, data=""):
        '''返回结果只包含一条记录'''
        try:
            dbCursor = self.dbconnect.cursor()
            if data:
                dbCursor.execute(query, data)
            else:
                dbCursor.execute(query)
            query_result = dbCursor.fetchone()
            dbCursor.close()
            return (query_result,True)
        except Exception as e:
            logger.error('执行数据库查询操作失败：%s' % e)
            dbCursor.close()
            return(e,False)

    def selectMoreRecord(self, query, data=""):
        '''返回结果只包含多条记录'''
        try:
            dbCursor = self.dbconnect.cursor()
            if data:
                dbCursor.execute(query, data)
            else:
                dbCursor.execute(query)
            query_result = dbCursor.fetchall()
            dbCursor.close()
            return query_result
        except Exception as e:
            logger.error('执行数据库查询操作失败：%s' % e)
            dbCursor.close()
            exit()
