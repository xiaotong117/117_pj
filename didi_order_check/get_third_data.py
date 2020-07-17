#!/usr/bin/python
# -*- coding: UTF-8 -*- 


from didi_order_check import config, tools
import pymysql, openpyxl

# def get_third_price(file):
#     conn = pymysql.connect(**config.DB_CONFIG)
#     cursor = conn.cursor()
#
#     try:
#         cursor.execute(config.SQL_third_data)
#         results = cursor.fetchall()
#
#         wb = openpyxl.load_workbook(file)
#         ws = wb.create_sheet()
#         ws.title = '预期数据'
#         ws.append(['订单号', '订单金额', '下单人', '支付时间'])
#
#         for row in results:
#             ws.append(row)
#             # print(row)
#         tools.sheet_layout(ws)
#         for col in ['A', 'B', 'C', 'D']:
#             ws.column_dimensions[col].width = 30
#
#     except:
#         print ("Error: unable to fetch data")
#
#
#     conn.close()
#     wb.save(file)
