#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/16 22:41
# @Author  : Vincent
# @File    : login.py

__author__ = 'Vincent'

'''
Description: Login
answer = 40, 43, 106, 40, 180, 40, 254, 47, 46, 110, 116, 110, 178, 108, 262, 107

'''

import requests
from url_interface import verifyUrl, checkCaptchaUrl

session = requests.Session()
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0'
}


class Login:
    def __init__(self):
        self.location = {
            '1': '44,44,',
            '2': '114,44,',
            '3': '185,44,',
            '4': '254,44,',
            '5': '44,124,',
            '6': '114,124,',
            '7': '185,124,',
            '8': '254,124,',
        }
        self.__get_image()

    def __get_image(self):
        res = session.get(verifyUrl, headers=headers)
        with open('verifyImage.png', 'wb') as f:
            f.write(res.content)
        self.__set_data(input('请输入验证码：'))

    def __set_data(self, img_number):
        nums = img_number.split(',')
        answer = ''
        for i in nums:
            answer += self.location[i]
        self.data = {
            'answer': answer,
            'login_site': 'E',
            'rand': 'sjrand'
        }
        print(self.data)
        self.__send_verification()

    def __send_verification(self):
        res = session.post(checkCaptchaUrl, headers=headers, data=self.data)
        print('status: %s' % res.status_code)
        print('headers: %s' % res.headers)
        print('content: %s' % res.content.decode('utf-8'))


if __name__ == '__main__':
    Login()
