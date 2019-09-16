# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 14:22:12 2019

@author: 82548
"""

"""读取上次游戏文件"""
f = open('output.txt')
data=f.read()
f.close
data=data.split()
data_dict={data[0]:data[1:4]}


""" 游戏准备 """
from random import randint
number=randint(1, 100)          #随机生成游戏数字
turn=0                          #游戏进行次数
count=0                         #单次游戏进行轮数   
all_count=0                     #游戏进行总轮数
min_count=10000000000           #单次游戏最小轮数
answer=101                      #玩家输入答案
for key in data_dict:           #提取文件数据          
    name=key                    #玩家输入名字
    turn=eval(data_dict['阿花'][0])
    min_count=eval(data_dict['阿花'][1])
    average_count=eval(data_dict['阿花'][2])
all_count=int(average_count*turn)
print("{},你已经玩了{}次，最少{}轮猜出，平均{:.2f}轮猜出".format(name,turn,min_count,average_count))

""" 开始游戏 """
while answer!=number:
    count=count+1      #记录单次游戏次数
    answer=eval(input("请猜一个1-100的数字：")) #输入单次游戏答案
    if answer<number:  #判断数字是否正确
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
        if go_on=="y":  #重置答案
           number=randint(1, 100)
           answer=101
           count=0
        else:           #退出游戏
            print("退出游戏，欢迎下次再来!")
            
""" 写入文件 """  
data="{} {} {} {:.2f}".format(name,turn,min_count,average_count)        
f = open('output.txt', 'w')
f.write(data)
f.close()