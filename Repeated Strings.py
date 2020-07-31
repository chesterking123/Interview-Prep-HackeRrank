#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    x1 = s.count('a')
    s1 = x1 * (n//len(s))
    s2 = s[:n%len(s)].count('a')
    result = s2 + s1
    return(result)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
