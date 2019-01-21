#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/16 22:41
# @Author  : Vincent
# @File    : login.py
import yaml

__author__ = 'Vincent'

'''
Description: 登陆
location: 模拟用户选择验证码位置
user: 登陆账号密码
params: 获取验证码的相关参数
data: 验证用户和密码的相关参数
verify_token_1: 第一次验证的相关参数
verify_token_2: 第二次验证相关的参数（成功后生成token，token即登陆状态）
'''

import requests
from api import Api
import time
from user import username, password

session = requests.Session()


class Login:
    __slots__ = ('__location', '__user', '__params', '__data', '__verify_token_1', '__verify_token_2')

    def __init__(self):
        self.__location = {
            '1': '45,46,',
            '2': '115,46,',
            '3': '185,46,',
            '4': '255,46,',
            '5': '45,126,',
            '6': '115,126,',
            '7': '185,126,',
            '8': '255,126,'
        }
        self.__user = {
            'username': username,
            'password': password,
            'appid': 'otn'
        }
        self.__params = {
            'answer': 'login_site',
            'module': 'login',
            'rand': 'sjrand'
        }

    def __get_image(self):
        res = session.get(Api.captcha, params=self.__params)
        with open('code.png', 'wb') as f:
            f.write(res.content)

    def __send_verification(self, img_number):
        nums = img_number.split(',')
        answer = ''
        for i in nums:
            answer += self.__location[i]
        self.__data = {
            'answer': answer,
            'login_site': 'E',
            'rand': 'sjrand'
        }
        res = session.post(Api.check_captcha, data=self.__data)
        print('status: %s' % res.status_code)
        print('content: %s' % res.json())

    def __send_username_pwd(self):
        res = session.post(Api.login, data=self.__user)
        print('status: %s' % res.status_code)
        print('content: %s' % res.json())

    def __verify_token(self):
        self.__verify_token_1 = {
            'appid': 'otn'
        }
        print('-----------第一次验证-----------------')
        res = session.post(Api.first_check, data=self.__verify_token_1)
        print('status: %s' % res.status_code)
        print('content: %s' % res.json()['result_message'])
        res_json = res.json()
        print('------------第二次验证----------------')
        print(res_json['newapptk'])
        self.__verify_token_2 = {
            'tk': res_json['newapptk']
        }
        res2 = session.post(Api.second_check, data=self.__verify_token_2)
        print('status: %s' % res2.status_code)
        print('content: %s' % res2.json())

    def login(self):
        self.__get_image()
        while True:
            time.sleep(10)
            with open('captcha.yaml', 'r', encoding='utf-8') as f:
                captcha_code = yaml.load(f.read())
                print(captcha_code)
                if not captcha_code['captcha'] == '':
                    self.__send_verification(captcha_code['captcha'])
                    break
                f.close()
        self.__send_username_pwd()
        self.__verify_token()


if __name__ == '__main__':
    Login().login()
