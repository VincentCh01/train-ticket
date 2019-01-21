#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Vincent'

'''
Description: 查票
train_date: 出发日期
from_station: 出发地代号
to_station: 到达地代号
purpose_codes： 票种（学生、成人、军人）
'''

import requests
from urllib import parse
import json
from api import Api
import yaml
import user

session = requests.session()
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0'
}


class LeftTicket:
    __slots__ = ('ticket', 'params')

    def __init__(self):
        self.ticket = []

    def __parse__station_name(self):
        with open('station_name.yaml', 'r', encoding='gbk') as f:
            station_dict = yaml.load(f.read())
            self.params = {
                'leftTicketDTO.train_date': user.train_date,
                'leftTicketDTO.from_station': station_dict[user.from_station_name],  # 衡阳
                'leftTicketDTO.to_station': station_dict[user.to_station_name],  # 济南
                'purpose_codes': 'ADULT'
            }

    def __search_ticket(self):
        self.__parse__station_name()
        res = session.get(Api.search_ticket, params=self.params)
        content = res.content.decode('utf-8')
        if not content.startswith('{'):
            return
        res_json = json.loads(content)
        tickets = parse.unquote(str(res_json['data']['result']), 'utf-8').split(',')
        ticket_list = []
        for i in range(0, len(tickets)):
            if has_ticket(tickets[i]):
                pure_ticket = tickets[i].replace('\n', '')
                # point = pure_ticket.find('|')
                # secret_str = pure_ticket[2:point]
                # train = pure_ticket[point + 17:].split('|')[0]
                # print(pure_ticket)
                # self.ticket[train] = secret_str
                ticket_list.append(pure_ticket)

        self.ticket = ticket_list

    def find_ticket(self):
        self.ticket = []
        self.__search_ticket()
        return self.ticket


def has_ticket(ticket):
    if ticket.startswith(" \'|"):
        return False
    else:
        if ticket.startswith("["):
            if ticket[1:].startswith("\'|"):
                return False
    return True


if __name__ == '__main__':
    left_ticket = LeftTicket()
