#!/usr/bin/env python3


# Complete the whatFlavors function below.
def whatFlavors(cost, money):
    m = []
    for pos in range(len(cost)):
        f1 = cost[pos]
        f2 = money - f1
        if f2 in m:
            print(cost.index(f2) + 1, pos + 1)
        else:
            m.append(f1)


if __name__ == "__main__":
    t = int(input())
    for t_itr in range(t):
        money = int(input())
        n = int(input())
        cost = list(map(int, input().rstrip().split()))
        whatFlavors(cost, money)
