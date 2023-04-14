#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from os import path

class SwitchConfig:
    def __init__(self, url, headers, body):
        self.url = url
        self.headers = headers
        self.body = body

    def __str__(self):
        return f'<SwitchConfig: url<{self.url}>, headers<{self.headers}>, body<{self.body}>>'

    def is_valid(self):
        return self.url and self.headers and self.body

class SwitchConfigParser:
    url, headers, body = None, None, None

    def __init__(self, conf_path: str):
        self.conf = self.__parser_config_from_file(conf_path)
        self.__update_vals()

    def gen_switch_config(self):
        return SwitchConfig(self.url, self.headers, self.body)

    def __update_vals(self):
        if self.conf:
            # this should update self.url, self.headers, self.body
            exec(self.conf)

    def __parser_config_from_file(self, conf_path: str):
        if not path.exists(conf_path) or not path.isfile(conf_path):
            return None
        file_content = None
        with open(conf_path, 'r') as file:
            file_content = file.read()
        if not file_content:
            return None
        text = file_content.replace('`', "'")
        text = text.splitlines()
        conf = ""
        start_flag = False
        for l in text:
            if l.startswith('const '):
                l = l.replace('const ', 'self.')
            if l.startswith('self.url') or start_flag:
                if l.startswith('self.method'):
                    continue
                conf += l
                start_flag = True
            if l.startswith('self.body'):
                break
        return conf

class RemoteSwitch:

    def __init__(self, config: SwitchConfig):
        if config.is_valid():
            self.url = config.url
            self.headers = config.headers
            self.body = config.body.encode('utf-8')
        else:
            raise RuntimeError('switch config is not valid: ' + str(config))

    def do_switch(self):
        '''
        res:
        {'status': 101, 'error': {'errorCode': 2004, 'errorInfo': '设备不在线', 'debugInfo': 'SMART业务错误  [设备不在线]', 'debugMe': 'GKTWWA9Q1681453366564'}, 'result': None}
        '''
        try:
            req = requests.post(url=self.url, headers=self.headers, data=self.body)
            res = req.json()
            print(res)
            # TODO 可以抓取获取状态的接口判断插座当前开关状态，判断开关控制是否成功
        except Exception as e:
            print('do_switch error', e)

