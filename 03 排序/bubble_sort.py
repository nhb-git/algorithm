#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员   ：Davis Niu
# 开发时间   ：4/30/2020  10:42 PM 
# 文件名称   ：bubble_sort.PY


def bubble_sort(li):
    """
    冒泡排序算法
    :param li: 无序列表
    :return: 有序列表
    """
    for order_num_count in range(len(li)-1):    # 每趟有序区元素个数，元素个数为len(li)-1是停止
        exchange = False    # 在一趟中没有发生排序, 认为排序已经完成
        for index in range(len(li)-order_num_count-1):  # 当前主比较值的下标
            if li[index] < li[index+1]:
                li[index], li[index+1] = li[index+1], li[index]
                exchange = True
        if not exchange:
            break
    return li


li = [7, 8, 9, 3, 2, 1]
print(bubble_sort(li))
