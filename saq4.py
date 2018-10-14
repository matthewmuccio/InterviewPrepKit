#!/usr/bin/env python3


# Complete the riddle function below.
def scan_left(arr):
    n = len(arr)
    stack = []
    left = [0] * n
    for i in range(n - 1, -1, -1):
        while stack and arr[i] <= arr[stack[-1]]:
            top = stack.pop()
            left[top] = top - i - 1
        stack.append(i)
    i -= 1
    while stack:
        top = stack.pop()
        left[top] = top - i - 1
    return left

def scan_right(arr):
    n = len(arr)
    stack = []
    right = [0] * n
    for i in range(n):
        while stack and arr[i] <= arr[stack[-1]]:
            top = stack.pop()
            right[top] = i - top - 1
        stack.append(i)
    i += 1
    while stack:
        top = stack.pop()
        right[top] = i - top - 1
    return right

def riddle(arr):
    n = len(arr)
    right = scan_right(arr)
    left = scan_left(arr)
    total = [right[i] + left[i] for i in range(n)]
    res = [min(arr)] * n
    for i in range(n - 1, -1, -1):
        win_size = total[i]
        res[win_size] = max(res[win_size], arr[i])
    for i in range(n - 2, -1, -1):
        res[i] = max(res[i], res[i + 1])
    return res


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    res = riddle(arr)
    print(res)
#    print(" ".join(map(str, res)))
