#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/15 23:45
# @Author  : Vincent
# @File    : verification_code.py

__author__ = 'Vincent'

'''
Description: 
'''

import requests
from json import loads
from user import username, password
from urllib3 import disable_warnings
from urllib3.exceptions import InsecureRequestWarning

disable_warnings(InsecureRequestWarning)
locate = {
    '1': '44,44,',
    '2': '114,44,',
    '3': '185,44,',
    '4': '254,44,',
    '5': '44,124,',
    '6': '114,124,',
    '7': '185,124,',
    '8': '254,124,',
}
head = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'
}
now_session = requests.Session()
now_session.verify = False


def login():
    print('-----------------验证码验证-----------------')
    resp1 = now_session.get(
        'https://kyfw.12306.cn/passport/captcha/captcha-image?login_site=E&module=login&rand=sjrand&0.8430851651301317',
        headers=head)
    with open('code.png', 'wb') as f:
        f.write(resp1.content)
    print('请输入验证码坐标代号：')
    code = input()
    write = code.split(',')
    codes = ''
    for i in write:
        codes += locate[i]
    data = {
        'answer': codes,
        'login_site': 'E',
        'rand': 'sjrand'
    }
    resp = now_session.post('https://kyfw.12306.cn/passport/captcha/captcha-check', headers=head, data=data)
    html = loads(resp.content)
    if html['result_code'] == '4':
        print('验证码校验成功！')
        print('-----------------登录中-----------------')
        login_url = 'https://kyfw.12306.cn/passport/web/login'
        user = {
            'username': username,
            'password': password,
            'appid': 'otn'
        }
        resp2 = now_session.post(login_url, headers=head, data=user)
        html = loads(resp2.content)
        print(html)
        if html['result_code'] == 0:
            print('登陆成功！')
            yzdata = {
                'appid': 'otn'
            }
            tk_url = 'https://kyfw.12306.cn/passport/web/auth/uamtk'
            resp3 = now_session.post(tk_url, data=yzdata, headers=head)
            print('-----------------第一次验证-----------------')
            print(resp3.text)
            login_message = resp3.json()['newapptk']
            print('loginMessage=', login_message)
            yz2data = {
                'tk': login_message
            }
            client_url = 'https://kyfw.12306.cn/otn/uamauthclient'
            resp4 = now_session.post(client_url, data=yz2data, headers=head)
            print('-----------------第二次验证-----------------')
            print(resp4.text)
        else:
            print('登陆失败！')
    else:
        print('验证码校验失败，正在重新请求页面...')
        login()
    pass


login()
