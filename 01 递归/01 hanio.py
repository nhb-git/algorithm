#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员   ：Davis Niu
# 开发时间   ：4/28/2020  02:57 PM 
# 文件名称   ：01 hanio.PY
# 开发工具   ：PyCharm


def hanio(n, a, b, c):
    """
    递归实现汉罗塔算法
    :param n: 圆盘数量
    :param a: 柱子
    :param b: 柱子
    :param c: 柱子
    :return: None
    """
    if n > 0:
        hanio(n-1, a, c, b)
        print('move from %s to %s' % (a, c))
        hanio(n-1, b, a, c)


hanio(1, 'A', 'B', 'C')
