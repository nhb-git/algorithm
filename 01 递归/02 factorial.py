#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员   ：Davis Niu
# 开发时间   ：4/28/2020  05:06 PM 
# 文件名称   ：02 factorial.PY
# 开发工具   ：PyCharm


def factorial(n):
    """
    递归实现阶乘
    :param n: 阶乘系数
    :return: 阶乘结果
    """
    if n <= 1:
        return 1
    return n * factorial(n-1)


print(factorial(0))
