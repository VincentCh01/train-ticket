#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/17 11:30
# @Author  : Vincent
# @File    : passengers.py

__author__ = 'Vincent'

'''
Description: passengers
'''

from url_interface import passengersUrl
import login
from login import Login

session = login.session


class Passengers:

    def __init__(self):
        self.data = {
            'pageIndex': '1',
            'pageSize': '10'
        }
        self.__get_all_passengers()

    def __get_all_passengers(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0',
            'Referer': 'https://kyfw.12306.cn/otn/view/passengers.html',
            'Content-Type': 'application/x-www-form-urlencoded',
        }
        res = session.post(passengersUrl, headers=headers, data=self.data)
        print('status: %s' % res.status_code)
        with open('passengers.json', 'w',encoding='utf-8') as f:
            f.write(res.text)
        print(session.cookies)


if __name__ == '__main__':
    Login()
    Passengers()
