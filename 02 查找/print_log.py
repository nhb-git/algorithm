#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员   ：Davis Niu
# 开发时间   ：4/30/2020  02:46 PM 
# 文件名称   ：print_log.PY


def print_log(func):
    def wrapper(*args, **kwargs):
        print('程序开始执行')
        func(*args, **kwargs)
        print('程序结束执行')
    return wrapper
