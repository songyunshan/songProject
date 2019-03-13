# -*- coding:utf-8 -*-
#re模块使python语言拥有全部的正则表达式功能
import re
#关联函数
def fetchStringByBoundary(data, LB = None, RB = None):
    rule =LB + r"(.*?)" + RB
    slotList = re.findall(rule, data)
    return slotList[0]
def fetchStringArrayByBoundary(data, LB = None, RB = None):
    rule =LB + r"(.*?)" + RB
    slotList = re.findall(rule, data)
    return slotList