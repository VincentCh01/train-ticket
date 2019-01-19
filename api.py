#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/16 22:43
# @Author  : Vincent
# @File    : api.py

__author__ = 'Vincent'

'''
Description: api
'''


class Api:
    # 查询站名字典
    station_name = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9090'

    # 登陆
    captcha = 'https://kyfw.12306.cn/passport/captcha/captcha-image'
    check_captcha = 'https://kyfw.12306.cn/passport/captcha/captcha-check'
    login = 'https://kyfw.12306.cn/passport/web/login'
    first_check = 'https://kyfw.12306.cn/passport/web/auth/uamtk'
    second_check = 'https://kyfw.12306.cn/otn/uamauthclient'

    # 查票
    search_ticket = 'https://kyfw.12306.cn/otn/leftTicket/queryZ'

    # 订票
    submit_order = 'https://kyfw.12306.cn/otn/leftTicket/submitOrderRequest'
    passengers = 'https://kyfw.12306.cn/otn/passengers/query'
    init_dc = 'https://kyfw.12306.cn/otn/confirmPassenger/initDc'
    check_order_info = 'https://kyfw.12306.cn/otn/confirmPassenger/checkOrderInfo'
    confirm_passengers = 'https://kyfw.12306.cn/otn/confirmPassenger/getQueueCount'
    confirm_order = 'https://kyfw.12306.cn/otn/confirmPassenger/confirmSingleForQueue'

    # 查询订票结果
    result_order = 'https://kyfw.12306.cn/otn/confirmPassenger/resultOrderForDcQueue'

    dictFilePath = 'station_name.yaml'
    ticketFilePath = 'ticket.yaml'
