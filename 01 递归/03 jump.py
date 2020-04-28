#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员   ：Davis Niu
# 开发时间   ：4/28/2020  06:02 PM 
# 文件名称   ：03 jump.PY
# 开发工具   ：PyCharm


# def jump(n):
#     if n == 1:
#         return 1
#     if n == 2:
#         return 2
#     return jump(n-1)+jump(n-2)

# 空间复杂度O(1)，时间复杂度O(n)
def jump(n):
    if n == 1:
        return 1
    if n == 2:
        return 2

    result = 0
    pre = 1
    next = 2

    i = 3
    while i <= n:
        result = pre + next
        pre, next = next, result
        i += 1
    return result


print(jump(200))
