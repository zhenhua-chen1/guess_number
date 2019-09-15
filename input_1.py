# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 14:22:12 2019

@author: 82548
"""

from random import randint
number=randint(1, 100)
turn=0
count=0
all_count=0
min_count=10000000000
answer=101
name=input("请输入你的名字：")
while answer!=number:
    count=count+1
    answer=eval(input("请猜一个1-100的数字："))
    if answer<number:
        print("猜小了再试试")
    elif answer>number:
        print("猜大了再试试")
    else:
        turn=turn+1
        all_count+=count
        average_count=float(all_count/turn)
        if count<min_count:
            min_count=count
        print('猜对了,你一共猜了{}轮'.format(count))
        print("{},你已经玩了{}次，最少{}轮猜出，平均{:.2f}轮猜出".format(name,turn,min_count,average_count))
        go_on=input("是否继续游戏？(输入y继续，其他退出)")
        if go_on=="y":
           number=randint(1, 100)
           answer=101
           count=0
        else:
            print("退出游戏，欢迎下次再来!")