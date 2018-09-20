#!/usr/bin/env python3


# Complete the minimumAbsoluteDifference function below.
def minimumAbsoluteDifference(arr):
    if len(arr) != len(list(set(arr))):
        result = 0
    a = sorted(arr)
    result = min(abs(x - y) for x, y in zip(a, a[1:]))
    return result


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    result = minimumAbsoluteDifference(arr)
    print(result)
