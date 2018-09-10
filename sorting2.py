#!/usr/bin/env python3


# Complete the maximumToys function below.
def maximumToys(prices, k):
    count = 0
    cost = 0
    for price in prices:
        if cost + price <= k:
            count += 1
            cost += price
        else:
            break
    print(count)


if __name__ == '__main__':
    n, k = [int(v) for v in input().split()]
    prices = sorted([int(v) for v in input().split()])
    maximumToys(prices, k)
