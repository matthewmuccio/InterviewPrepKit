#!/bin/python3


import os


def minimumSwaps(arr):
    count = 0
    i = 0
    while i < len(arr):
        if arr[i] == i + 1 or arr[i] > len(arr):
            i += 1
        else:
            temp = arr[i] - 1
            arr[i], arr[temp] = arr[temp], arr[i]
            count += 1
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    res = minimumSwaps(arr)
    fptr.write(str(res) + '\n')
    fptr.close()
