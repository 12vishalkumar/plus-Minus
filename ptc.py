#!/bin/python3
import math
import os
import random
import re
import sys
# Complete the 'plusMinus' function below.
# The function accepts INTEGER_ARRAY arr as parameter.
def plusMinus(arr):
    # Write your code here
    P = N = Z = 0
    L = len(arr)
    for i in arr:
        if(i>0):
            P += 1
        elif(i==0):
            Z += 1
        else:
            N += 1
    print('{0: .4f}'.format(P/L))
    print('{0: .4f'.format(N/L))
    print('{0: .4f}'.format(Z/L))

if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    plusMinus(arr)