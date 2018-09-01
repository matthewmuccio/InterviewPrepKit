#!/usr/bin/env python3


def rotLeft(a, k):
    return a[k:]+a[:k]


if __name__ == "__main__":
    n, k = map(int, input().strip().split(" "))
    a = list(map(int, input().strip().split(" ")))
    answer = rotLeft(a, k);
    print(*answer, sep=" ")
