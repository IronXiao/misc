#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import sys

BARK_BASE_URL = 'https://api.day.app/{key}/{args}'


def send_bark(key: str, args: str):
    url = BARK_BASE_URL.format(key=key, args=args)
    try:
        req = requests.get(url)
        res =  req.json()
        print(res)
        return res['message'] == 'success'
    except Exception as e:
        print('bark msg send error: ', e)
    return False

def check_args():
    if len(sys.argv) == 3:
        return True
    return False

def help():
    print('usage:')
    print('\t{} {} {}'.format(sys.argv[0], '<bark api key>', '<bark content>'))

def main():
    if not check_args():
        help()
        return
    if send_bark(sys.argv[1], sys.argv[2]):
        print('Bark msg sent success!')
    else:
        print('Bark msg send failed!')

if __name__ == '__main__':
    main()


