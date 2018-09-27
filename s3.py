#!/usr/bin/env python3


# Complete the pairs function below.
def pairs(k, arr):
    return len(set(arr) & set(x + k for x in arr))


if __name__ == "__main__":
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    arr = list(map(int, input().rstrip().split()))
    result = pairs(k, arr)
    print(result)
