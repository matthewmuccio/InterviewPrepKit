#!/usr/bin/env python3


# Complete the maxMin function below.


if __name__ == "__main__":
    n = int(input())
    k = int(input())
    l = sorted([int(input()) for _ in range(n)])
    print(min([abs(l[i + k - 1] - l[i]) for i in range(n - k + 1)]))
