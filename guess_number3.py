# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 14:22:12 2019

@author: 82548
"""

"""打开上次游戏文件"""
f = open('output.txt')
lines=f.readlines()
f.close()
name=input("请输入你的名字：")

"""数据初始化"""
data_dict={}
turn='0'                          #游戏进行次数
count='0'                         #单次游戏进行轮数   
all_count='0'                     #游戏进行总轮数
average_count='0'                 #平均游戏次数
min_count='10000000000'           #单次游戏最小轮数
if  lines == []:
     data_dict={name:[turn,min_count,average_count,all_count]}
for line in lines:
    data=line.split()
    if data[0] == name:         #判断是否为老用户
        data_dict={data[0]:data[1:5]}
        break
    data_dict={name:[turn,min_count,average_count,all_count]}



""" 输入数据 """
from random import randint
number=randint(1, 100)          #随机生成游戏数字
answer=101                      #玩家输入答案
for key in data_dict:           #提取文件数据          
    name=key                    #玩家输入名字
    turn=eval(data_dict[name][0])
    min_count=eval(data_dict[name][1])
    average_count=eval(data_dict[name][2])
    all_count=eval(data_dict[name][3])
if min_count==10000000000 :  
   print("{},你已经玩了{}次，最少0轮猜出，平均{:.2f}轮猜出".format(name,turn,average_count))
else :
   print("{},你已经玩了{}次，最少{}轮猜出，平均{:.2f}轮猜出".format(name,turn,min_count,average_count))

""" 开始游戏 """
while answer!=number:
    count=int(count)+1      #记录单次游戏次数
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
data_3=''
data="{} {} {} {:.2f} {}\n".format(name,turn,min_count,average_count,all_count)       
f = open('output.txt', 'w')
if lines==[]:
    f.writelines(data)
    f.close()    
else: 
    for line in lines:
        data_2=line.split()
        if data_2[0] == name:         #判断是否为老用户
            data_3=data_3+data
        else:
            data_3=data_3+line+"\n"
    f.writelines(data_3)
    f.close()