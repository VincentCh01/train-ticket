#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Vincent'

from url_interface import searchLeftTicketUrl
import requests
from urllib import parse

session = requests.session()
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0'
}
import json


class LeftTicket:

    def __init__(self):
        self.url = searchLeftTicketUrl
        self.params = {
            'leftTicketDTO.train_date': '2019-02-04',
            'leftTicketDTO.from_station': 'HYQ',
            'leftTicketDTO.to_station': 'JNK',
            'purpose_codes': 'ADULT'
        }
        self.data = self.__get_left_ticket()
        self.__parse_ticket()

    def __get_left_ticket(self):
        res = session.get(self.url, params=self.params)
        res_json = json.loads(res.content.decode('utf-8'))
        return parse.unquote(str(res_json['data']['result']), 'utf-8')

    def __parse_ticket(self):
        tickets = self.data.split(',')
        for i in range(0, len(tickets)):
            if has_ticket(tickets[i]):
                prue_ticket = tickets[i].replace('\n', '')
                secretStr = prue_ticket[2:prue_ticket.find('|')]
                print()
                print(prue_ticket)

    def output_data(self):
        with open('ticket.txt', 'w+', encoding='utf-8') as f:
            f.write(self.data)


def has_ticket(ticket):
    return not ticket.startswith(" \'|")


if __name__ == '__main__':
    left_ticket = LeftTicket()
    left_ticket.output_data()
