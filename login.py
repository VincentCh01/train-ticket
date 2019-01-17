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
from url_interface import verifyUrl, checkCaptchaUrl, loginUrl, firstVerifyUrl, secondVerifyUrl
from user import username, password
from requests.cookies import RequestsCookieJar
import json

session = requests.Session()
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0'
}


class Login:
    def __init__(self):
        self.location = {
            '1': '45,46,',
            '2': '115,46,',
            '3': '185,46,',
            '4': '255,46,',
            '5': '45,126,',
            '6': '115,126,',
            '7': '185,126,',
            '8': '255,126,',
        }
        self.user = {
            'username': username,
            'password': password,
            'appid': 'otn'
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
        print('content: %s' % res.json())
        self.__send_username_pwd()

    def __send_username_pwd(self):
        res = session.post(loginUrl, headers=headers, data=self.user)
        print('status: %s' % res.status_code)
        print('content: %s' % res.json())
        self.__verify_token()

    def __verify_token(self):
        self.data = {
            'appid': 'otn'
        }
        print('-----------第一次验证-----------------')
        res = session.post(firstVerifyUrl, headers=headers, data=self.data)
        print('status: %s' % res.status_code)
        print('content: %s' % res.json())
        res_json = res.json()
        print('------------第二次验证----------------')
        print(res_json['newapptk'])
        self.data2 = {
            'tk': res_json['newapptk']
        }
        res2 = session.post(secondVerifyUrl, headers=headers, data=self.data2)
        print('status: %s' % res2.status_code)
        print('content: %s' % res2.json())


if __name__ == '__main__':
    login = Login()
