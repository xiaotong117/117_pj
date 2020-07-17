#!/usr/bin/python
# -*- coding: UTF-8 -*-

from didi_order_check import tools,config
import logging
import openpyxl
import time

def get_db_price(file):
    try:
        db_buy = tools.db_connect(config.DB_CONFIG_BUY)
        data = tools.pull_data(db_buy, [config.SQL_order_price], (20001, 20003, 20007, 20009, 20017, 20019, 20021))
        tools.db_disconnect(db_buy)

        wb = openpyxl.Workbook()
        ws = wb.create_sheet()
        ws.title = '滴滴订单'
        ws.append(['订单号', '订单状态', '订单类型', '订单金额', '下单人', '下单时间'])

        for row in data[0]:
            ws.append(row)

        tools.sheet_layout(ws)
        for col in ['A', 'F']:
            ws.column_dimensions[col].width = 30
        for col in ['B', 'C', 'D', 'E']:
            ws.column_dimensions[col].width = 20

        wb.remove_sheet(wb.get_sheet_by_name("Sheet"))
    except:
        logging.error("Error: unable to fetch data", exc_info=True)

    wb.save(file)

# file = '业务金额核对2019-05-09.xlsx'
# get_db_price(file)