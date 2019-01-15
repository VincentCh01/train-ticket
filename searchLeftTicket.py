#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/13 3:24
# @Author  : Vincent
# @File    : searchLeftTicket.py

__author__ = 'Vincent'

import yaml
from urllib import request
import os
import asyncio
import http.client
from constant.urlEntity import UrlName

dic = {}
ticket = {}

http.client.HTTPConnection._http_vsn = 10
http.client.HTTPConnection._http_vsn_str = 'HTTP/1.0'


async def _gen_GetRequest():
    currentPath = os.path.dirname(os.path.realpath(__file__))
    dictPath = os.path.join(currentPath, UrlName.dictFilePath)
    with open(dictPath, 'r', encoding='gbk') as f:
        dic = yaml.load(f.read())
    ticketPath = os.path.join(currentPath, UrlName.ticketFilePath)
    with open(ticketPath, 'r', encoding='utf-8') as f:
        ticket = yaml.load(f.read())
    startStation = ticket['from']
    endStation = ticket['to']
    startDate = ticket['date'].strftime("%Y-%m-%d")
    startStation = dic[startStation]
    endStation = dic[endStation]
    url = UrlName.searchLeftTicketUrl.replace('${from}', startStation).replace('${to}', endStation).replace('${date}',
                                                                                                            startDate)
    while True:
        await asyncio.sleep(1)
        print('开始搜索余票中...')
        req = request.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0')
        with request.urlopen(req) as inform:
            data = inform.read().decode('utf-8')
            data = data.split('result')[1].split('[')[1].split("]")[0]
            data = data.split('"')
            for i in range(len(data)):
                if (i + 1) % 8 == 0:
                    leftTicket = data[i].split('|')
                    # 26 30 31 32
                    if leftTicket[3].count('G'):
                        if leftTicket[11] == 'Y':
                            print('列车 : %s  是否有票 : %s  无座 ： %s  二等座 : %s  一等座 : %s  商务座 : %s' % (
                                leftTicket[3], leftTicket[11], leftTicket[26], leftTicket[30], leftTicket[31],
                                leftTicket[32]))
                    else:
                        # 23 26 28 29
                        # print('列车 : %s  是否有票 : %s  软卧 : %s  硬卧 : %s  硬座 : %s  无座 : %s' % (
                        # leftTicket[3], leftTicket[11], leftTicket[23], leftTicket[28], leftTicket[29], leftTicket[26]))
                        pass


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(_gen_GetRequest())
