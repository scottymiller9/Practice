#!/bin/python3

import sys

arr = []
for arr_i in range(6):
    arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
    arr.append(arr_t)
total = 0
counter = 0

for j in range(1,5):
    for i in range(4):
            counter=arr[j][i]+arr[j-1][i]+arr[j+1][i]+arr[j][i+1]+arr[j][i+2]+arr[j-1][i+2]+arr[j+1][i+2]
        print(counter)
        if counter > total:
            total = counter

print(total)
