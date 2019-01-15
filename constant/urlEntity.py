#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/12 23:18
# @Author  : Vincent
# @File    : urlEntity.py


class UrlName:
    stationNameUrl = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9090'
    searchLeftTicketUrl = 'https://kyfw.12306.cn/otn/leftTicket/queryZ?leftTicketDTO.train_date=${date}&leftTicketDTO.from_station=${from}&leftTicketDTO.to_station=${to}&purpose_codes=ADULT'
    dictFilePath = 'station_name.yaml'
    ticketFilePath = 'ticket.yaml'
