#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''数据库连接配置'''
DB_CONFIG_BUY = {
    'host': '10.0.10.42',
    'port': 3306,
    'user': 'root',
    'passwd': 'shinemo123',
    'db': 'buy'
}

DB_CONFIG_TC = {
    'host': '10.0.10.42',
    'port': 3306,
    'user': 'root',
    'passwd': 'shinemo123',
    'db': 'tc'
}

DB_CONFIG_WELFARE = {
    'host': '10.0.10.42',
    'port': 3306,
    'user': 'root',
    'passwd': 'shinemo123',
    'db': 'shinemo_welfare'
}

'''订单表数据SQL查询语句'''
SQL_order_price = 'select order_id as A,order_sub_status as B,source_app as C,price as D,update_user_name ' \
                  'as E,gmt_create as F from buy_order_new where biz_type = 3 and order_sub_status in %s ' \
                  'order by id desc'

# '''第三方数据SQL查询语句'''
# SQL_third_data = 'select order_id,price,update_user_name,gmt_pay from buy_order_new where biz_type = 3 ' \
#                   'and order_status = 12'

'''拉取buy_order_new数据'''
SQL_buy_order_new1 = 'select order_id,order_type,order_status,third_id,price,source_app from buy_order_new where order_id in %s'
SQL_buy_order_new2 = 'select order_id,order_type,order_status,third_id,gmt_pay,gmt_settlement_time,price,should_price,integral_price,source_app from buy_order_new where order_id in %s'


'''拉取car_order数据'''
SQL_car_order1 = 'select order_id,biz_type,ride_type,car_type,car_order_type,start_address,end_address,passenger_name,' \
                'passenger_phone,order_create_time,order_usage_time,order_expire_time,start_longitude,start_latitude,' \
                'start_city_code,start_city_name,end_longitude,end_latitude,end_city_code,end_city_name ' \
                'from car_order where order_id in %s'
SQL_car_order2 = 'select order_id,biz_type,ride_type,car_type,car_order_type,start_address,end_address,passenger_name,' \
                'passenger_phone,order_create_time,order_usage_time,order_expire_time,start_longitude,start_latitude,' \
                'start_city_code,start_city_name,end_longitude,end_latitude,end_city_code,end_city_name,drive_name,drive_phone,driver_car_type,driver_car_color,driver_card,driver_avatar,driver_score ' \
                'from car_order where order_id in %s'
SQL_car_order3 = 'select order_id,biz_type,ride_type,car_type,car_order_type,start_address,end_address,passenger_name,' \
                'passenger_phone,order_create_time,order_usage_time,order_expire_time,start_longitude,start_latitude,' \
                'start_city_code,start_city_name,end_longitude,end_latitude,end_city_code,end_city_name,drive_name,drive_phone,driver_car_type,driver_car_color,driver_card,driver_avatar,driver_score,driver_arrived_time ' \
                'from car_order where order_id in %s'
SQL_car_order4 = 'select order_id,biz_type,ride_type,car_type,car_order_type,start_address,end_address,passenger_name,' \
                'passenger_phone,order_create_time,order_usage_time,order_expire_time,start_longitude,start_latitude,' \
                'start_city_code,start_city_name,end_longitude,end_latitude,end_city_code,end_city_name,drive_name,' \
                'drive_phone,driver_car_type,driver_car_color,driver_card,driver_avatar,driver_score,driver_arrived_time,service_start_time ' \
                'from car_order where order_id in %s'
SQL_car_order5 = 'select order_id,biz_type,ride_type,car_type,car_order_type,start_address,end_address,passenger_name,' \
                'passenger_phone,order_create_time,order_usage_time,order_expire_time,start_longitude,start_latitude,' \
                'start_city_code,start_city_name,end_longitude,end_latitude,end_city_code,end_city_name,drive_name,' \
                'drive_phone,driver_car_type,driver_car_color,driver_card,driver_avatar,driver_score,driver_arrived_time,' \
                'service_start_time,service_finished_time,order_paid_time,travel_distance,travel_time,order_price_details,pay_price_details ' \
                'from car_order where order_id in %s'

'''拉取tc.user_frezen_detail数据'''
SQL_user_frezen_detail = 'select order_id,biz_type,money,frozen_status from user_frozen_detail where order_id in %s'

'''拉取tc.pay_detail数据'''
SQL_pay_detail = 'select order_id,biz_type,price,pay_status from pay_detail where order_id in %s'

'''拉取shinemo_welfare.account_freeze数据'''
SQL_account_freeze = 'select third_id,amount,freeze_status from account_freeze where third_id in %s'

'''拉取shinemo_welfare.welfare_turnover数据'''
SQL_welfare_turnover = 'select third_id,account_type,turnover_type,turnover_sub_type,remark,amount,' \
                       'turnover_status from welfare_turnover where third_id in %s'


#订单校验白名单
white_list = ['010031805040000001463623']
