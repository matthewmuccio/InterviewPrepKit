#!/usr/bin/env python3


# Complete the maxSubsetSum function below.
def maxSubsetSum(arr):
    if len(arr) == 0: return 0
    if len(arr) == 1: return arr[0]
    arr[0] = max(0, arr[0])
    arr[1] = max(arr[0], arr[1])
    for i in range(2, len(arr)):
        arr[i] = max(arr[i - 1], arr[i] + arr[i - 2])
    return arr[-1]


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    res = maxSubsetSum(arr)
    print(res)
