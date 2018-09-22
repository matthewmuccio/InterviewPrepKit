#!/usr/bin/env python3


# Complete the getMinimumCost function below.
def getMinimumCost(k, c):
    return sum([cost * ((i // k) + 1) for i, cost in enumerate(sorted(c, reverse=True))])


if __name__ == "__main__":
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    c = list(map(int, input().rstrip().split()))
    minimumCost = getMinimumCost(k, c)
    print(minimumCost)
