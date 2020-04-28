#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员   ：Davis Niu
# 开发时间   ：4/28/2020  03:21 PM 
# 文件名称   ：01 linear_search.PY
# 开发工具   ：PyCharm


def linear_search(li, val):
    """
    顺序查找算法
    :param li: 列表
    :param val: 查找的元素
    :return: 元素下标或者None
    """
    for index, v in enumerate(li):
        if v == val:
            return index
    else:
        return None
