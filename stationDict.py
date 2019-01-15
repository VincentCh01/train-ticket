#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/12 23:08
# @Author  : Vincent
# @File    : stationDict.py

__author__ = 'Vincent'

from urllib import request
import asyncio
from constant.urlEntity import UrlName

dic = {}


async def _get_station_dict():
    req = request.Request(UrlName.stationNameUrl)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0')
    with request.urlopen(req) as f:
        print('Status:', f.status, f.reason)
        for k, v in f.getheaders():
            print('%s : %s' % (k, v))
        with open(UrlName.dictFilePath, 'w+') as output:
            data = f.read().decode('utf-8')
            stattion_Dict = data.split('\'')[1].split('|')
            n = 1
            while n < len(stattion_Dict):
                dic[stattion_Dict[n]] = stattion_Dict[n + 1]
                n += 5
            for k, v in dic.items():
                output.write('%s : %s \n' % (k, v))


def _send_request():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(_get_station_dict())


if __name__ == '__main__':
    _send_request()
