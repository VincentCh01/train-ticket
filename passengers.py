#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/17 11:30
# @Author  : Vincent
# @File    : passengers.py

__author__ = 'Vincent'

'''
Description: 获取乘车人信息
pageIndex： 获取页数
pageSize： 每页数据量
'''

from login import session
from api import Api
from login import Login


class Passengers:

    def __init__(self):
        self.__page = {
            'pageIndex': '1',
            'pageSize': '10'
        }

    def output_passengers(self):
        res = session.post(Api.passengers, data=self.__page)
        with open('passengers.json', 'w', encoding='utf-8') as f:
            f.write(res.text)


if __name__ == '__main__':
    Login().login()
    Passengers().output_passengers()
