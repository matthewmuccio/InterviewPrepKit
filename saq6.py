#!/bin/python3


# Complete the poisonousPlants function below.


if __name__ == "__main__":
    n = int(input())
    p = list(map(int, input().split(' ')))
    days = [0] * n
    s = [0]
    mn = p[0]
    mx = 0
    for i in range(1, n):
        if p[i] > p[i - 1]:
            days[i] = 1
        mn = min(mn, p[i])
        while s and p[s[-1]] >= p[i]:
            if p[i] > mn:
                days[i] = max(days[i], days[s[-1]] + 1)
            s.pop()
        mx = max(mx, days[i])
        s += [i]
    result = mx
    print(result)
