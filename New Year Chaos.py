#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    flag=0
    for i in range(1,len(q)+1):
        if((q[i-1]-i)>=3):
            print('Too chaotic')
            flag =1
            break
    count = 0
    temp=0
    count=0
    sortedlist = sorted(q)
    while(q!=sortedlist):
        for i in range(len(q)-1):
            if(q[i]>q[i+1]):
                q[i],q[i+1]=q[i+1],q[i] 
                count = count+1
    if(flag==0):
        print(count)
    

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)  
