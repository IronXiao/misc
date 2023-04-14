#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from remoteSwitch import SwitchConfigParser
from remoteSwitch import RemoteSwitch
import sys

def main():
    if not check_args():
        help()
        return
    switchConfig = SwitchConfigParser(sys.argv[1]).gen_switch_config()
    remote_switch = RemoteSwitch(switchConfig)
    remote_switch.do_switch()


def help():
    print('usage:')
    print('\t{} {}'.format(sys.argv[0], '<config file path>'))

def check_args():
    if len(sys.argv) == 2:
        return True
    return False

if __name__ == '__main__':
    main()

