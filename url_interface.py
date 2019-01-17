#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/16 22:43
# @Author  : Vincent
# @File    : url_interface.py

__author__ = 'Vincent'

'''
Description: url
'''

stationNameUrl = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9090'
searchLeftTicketUrl = 'https://kyfw.12306.cn/otn/leftTicket/queryZ?leftTicketDTO.train_date=${date}&leftTicketDTO.from_station=${from}&leftTicketDTO.to_station=${to}&purpose_codes=ADULT'
verifyUrl = 'https://kyfw.12306.cn/passport/captcha/captcha-image?login_site=E&module=login&rand=sjrand&0.7829358367975209'
checkCaptchaUrl = 'https://kyfw.12306.cn/passport/captcha/captcha-check'
loginUrl = 'https://kyfw.12306.cn/passport/web/login'
passengersUrl = 'https://kyfw.12306.cn/otn/passengers/query'
firstVerifyUrl ='https://kyfw.12306.cn/passport/web/auth/uamtk'
secondVerifyUrl ='https://kyfw.12306.cn/otn/uamauthclient'
dictFilePath = 'station_name.yaml'
ticketFilePath = 'ticket.yaml'