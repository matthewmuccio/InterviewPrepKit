#!/usr/bin/env python3


# Complete the candies function below.
def candies(n, arr):
    def f(a):
        b = [1]
        for i in range(1, len(a)):
            b.append(b[i - 1] + 1 if a[i] > a[i - 1] else 1)
        return b
    b = f(arr)
    arr.reverse()
    c = f(arr)
    c.reverse()
    return sum(max(u, v) for (u, v) in zip(b, c))


if __name__ == "__main__":
    n = int(input())
    arr = []
    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)
    result = candies(n, arr)
    print(result)
