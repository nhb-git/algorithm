#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员   ：Davis Niu
# 开发时间   ：4/30/2020  07:26 AM 
# 文件名称   ：02 binary_search.PY
import cal_time
import print_log


@cal_time.cal_time
@print_log.print_log
def binary_search(li, val):
    """
    二分查找
    :param li: 有序列表
    :param val: 要查找的值
    :return: 返回下标或者None
    """
    # 定义初始候选区
    left = 0
    right = len(li) - 1

    while left <= right:
        mid = (left + right) // 2
        if li[mid] == val:
            return mid
        elif li[mid] < val:  # 要查找的值在右侧可能存在
            left = mid + 1
        else:  # 要查找的值在左侧可能存在
            right = mid - 1
    else:  # 要找的值不在有序列表中
        return None


print(binary_search(list(range(10000000)), 9999999))
