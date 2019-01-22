#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/18 23:11
# @Author  : Vincent
# @File    : ticket_order.py

__author__ = 'Vincent'

import time
from user import from_station_name, to_station_name, train_date
from login import session, Login
from api import Api
from search_ticket import LeftTicket
import send_email

'''
Description: 订票
secretStr: 表示选择的车辆，从查票接口中获得
train_date: 出发日期
back_train_date: 订票日期
'''


class Order:
    __slots__ = (
        'data', '__dc', 'repeat_submit_order', 'left_ticket_str', '__check', 'sub_session', 'train_no', 'train_code',
        'from_station', 'to_station', 'train_location', 'seats', 'confirm_order', 'result_order', 'key_check_ischange')

    def __init__(self, results):
        self.data = {
            'secretStr': results['secret_str'],
            'train_date': train_date,
            'back_train_date': time.strftime('%Y-%m-%d', time.localtime(time.time())),
            'tour_flag': 'dc',
            'purpose_codes': 'ADULT',
            'query_from_station_name': from_station_name,
            'query_to_station_name': to_station_name
        }
        self.train_no = results['train_no']
        self.train_code = results['train_code']
        self.from_station = results['from']
        self.to_station = results['to']
        self.train_location = results['train_location']
        self.__submit_order_request()
        self.__init_dc()

    def __submit_order_request(self):
        session.post(Api.submit_order, data=self.data)

    def __init_dc(self):
        self.__dc = {
            '_json_att': ''
        }
        res = session.post(Api.init_dc, data=self.__dc)
        content = res.content.decode('utf-8')
        # with open('dc.html', 'w', encoding='utf-8') as f:
        #    f.write(content)
        point = content.find('globalRepeatSubmitToken')
        repeat_submit_token = res.content.decode('utf-8')[point + 27:point + 59]
        point2 = content.find('leftTicketStr')
        if point2 != -1:
            middle_data = content[point2 + 16:]
            left_ticket_str = middle_data[0:middle_data.find('\'')]
            self.left_ticket_str = left_ticket_str
        self.repeat_submit_order = repeat_submit_token

        point3 = content.find('key_check_isChange')
        key_check_ischange = content[point3 + 21:point3 + 77]
        print(key_check_ischange)
        self.key_check_ischange = key_check_ischange

        if hasattr(self, 'left_ticket_str'):
            self.__check_order_info()

    def __check_order_info(self):
        self.__check = {
            'cancel_flag': 2,
            'bed_level_order_num': '000000000000000000000000000000',
            'passengerTicketStr': 'O,0,1,张霖,1,430223199501291851,13813456184,N',
            'oldPassengerStr': '张霖,1,430223199501291851,1_',
            'tour_flag': 'dc',
            'randCode': '',
            '_json_att': '',
            'whatsSelect': '1',
            'REPEAT_SUBMIT_TOKEN': self.repeat_submit_order
        }
        res = session.post(Api.check_order_info, data=self.__check)
        print('res.content : %s ' % res.content.decode('utf-8'))
        self.__get_queue_count()

    def __get_queue_count(self):
        self.seats = {
            'train_date': 'Wed Jan 23 2019 00:00:00 GMT+0800 (中国标准时间)',
            'train_no': self.train_no,
            'stationTrainCode': self.train_code,
            'seatType': 'O',
            'fromStationTelecode': self.from_station,
            'toStationTelecode': self.to_station,
            'leftTicket': self.left_ticket_str,
            'purpose_codes': '00',
            'train_location': self.train_location,
            '_json_at': '',
            'REPEAT_SUBMIT_TOKEN': self.repeat_submit_order
        }
        res = session.post(Api.confirm_passengers, data=self.seats)
        print(res.content.decode('utf-8'))
        #self.__confirm_submit_order()

    def __confirm_submit_order(self):
        self.confirm_order = {
            'passengerTicketStr': 'O,0,1,张霖,1,430223199501291851,13813456184',
            'oldPassengerStr': '张霖,1,430223199501291851,1_',
            'randCode': '',
            'purpose_codes': '00',
            'key_check_isChange': self.key_check_ischange,
            'leftTicketStr': self.left_ticket_str,
            'train_location': self.train_location,
            'choose_seats': '1F',
            'seatDetailType': '000',
            'roomType': '00',
            'dwAll': 'N',
            '_json_att': '',
            'whatsSelect': '1',
            'REPEAT_SUBMIT_TOKEN': self.repeat_submit_order
        }
        res = session.post(Api.confirm_order, data=self.confirm_order)
        print(res.content.decode('utf-8'))
        send_email.send_email()
        self.__search_result_order()

    def __search_result_order(self):
        self.result_order = {
            'orderSequence_no': 'EC16649156',
            '_json_att': '',
            'REPEAT_SUBMIT_TOKEN': self.repeat_submit_order
        }
        res = session.post(Api.result_order, data=self.result_order)
        print(res.content.decode('utf-8'))


if __name__ == '__main__':
    print(time.strftime('%Y-%m-%d', time.localtime(time.time())))
    Login().login()
    tickets = LeftTicket().find_ticket()
