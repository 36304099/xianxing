#!/usr/bin/python
# -*- coding: utf-8 -*-
"""这里用于测试代码片段"""
from datetime import  datetime,timedelta
def datediff(d1,d2):
    """
    '1 = datediff('2017-12-31','2017-12-30')  前面减去后面
    """
    md1 = datetime.strptime(d1, '%Y-%m-%d')
    md2 = datetime.strptime(d2, '%Y-%m-%d')
    delta = md1 - md2
    return delta.days

def xianXing(tt):
    """
    输入日期，返回北京尾号限行
    没有考虑节假日
    :param tt: datetime类型日期
    :return:限行结果
    """
    initDate="2019-7-8"
    initXX=0   #初始化 2019年7月8日，北京限行 0，5，这里配置其中一个数字

    xx={}
    dt=( tt -  datetime.strptime(initDate, '%Y-%m-%d') ).days
    weekscount=dt//7//13 #13周轮一次
    d=dt%7 + 1 #余数，周几

    for i in range(5):
        xx[ (i + 2 + weekscount)%5 +1]=[ (i+1+initXX%5)%10,(i+6+initXX%5)%10]
    xx[6]=xx[7]=['','']

    return {
        "day":tt.strftime('%Y-%m-%d')
        ,"weekday":d
        ,"xx":xx[d]
        ,"datetime":tt
        }

if __name__ == "__main__":
    for i in range(100):
        print xianXing(datetime.now()+timedelta(days=i))