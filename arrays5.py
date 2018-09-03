#!/usr/bin/env python3


if __name__ == '__main__':
    n, m = map(int, input().split())
    numbers = [0] * n
    value, mx = 0, 0
    for _ in range(m):
        a, b, k = map(int, input().split())
        numbers[a - 1] += k
        if b < n:
            numbers[b] -= k
    for number in numbers:
        value += number
        if value > mx:
            mx = value
    print(mx)
