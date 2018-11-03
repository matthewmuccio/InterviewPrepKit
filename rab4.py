#!/usr/bin/env python3


# Complete the superDigit function below.
def superDigit(n, k):
    x = int(n) * k % 9
    return x if x else 9


if __name__ == "__main__":
    nk = input().split()
    n = nk[0]
    k = int(nk[1])
    result = superDigit(n, k)
    print(result)
