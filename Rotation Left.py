#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotLeft(n, a, d):
    new=[]
    for i in range(d):
        f=1
        for j in range(2):
            if(f==1):
                first = a[0]
                a.remove(first)
                f=0
            
            new = a

            if(j==1):
                new.append(first)
                a = new
    return a
            


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(n, a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
