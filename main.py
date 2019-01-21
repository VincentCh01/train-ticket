#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/18 22:54
# @Author  : Vincent
# @File    : main.py

__author__ = 'Vincent'

'''
Description: 程序入口
'''

from login import Login
from search_ticket import LeftTicket
from ticket_order import Order

left_ticket = LeftTicket()


def login():
    Login().login()


def create_order(count):
    count += 1
    print('第 %s 次查票...' % count)
    tickets = __find_ticket()
    if __has_ticket(tickets):
        submit_order(tickets, count)


def submit_order(tickets, count):
    for i in range(0, len(tickets)):
        results = __parse_data(tickets[i])
        if str(results['train_code']).startswith('G'):
            Order(results)


def __find_ticket():
    return left_ticket.find_ticket()


def __has_ticket(tickets):
    if len(tickets) > 0:
        return True
    return False


def __parse_data(ticket):
    results = {}
    point = ticket.find('|')
    secret_str = ticket[2:point]
    ticket_list = ticket[point:].split('|')
    train_no = ticket_list[2]
    train_code = ticket_list[3]
    from_station = ticket_list[6]
    to_station = ticket_list[7]
    train_location = ticket_list[15]
    results['train_no'] = train_no
    results['train_code'] = train_code  # 车次
    results['secret_str'] = secret_str
    results['from'] = from_station
    results['to'] = to_station
    results['train_location'] = train_location
    return results


init_count = 0
login()
flag = True
while flag:
    create_order(init_count)
