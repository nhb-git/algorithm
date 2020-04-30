#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员   ：Davis Niu
# 开发时间   ：4/30/2020  02:13 PM 
# 文件名称   ：cal_time.PY
import time


def cal_time(func):
    def wraps(*args, **kwargs):
        start_time = time.clock()
        func(*args, **kwargs)
        end_time = time.clock()
        elapsed = end_time - start_time
        print('程序执行时间是: %s' % elapsed)

    return wraps
