#!/usr/bin/env python3


# Complete the flippingBits function below.
def flippingBits(n):
    return int("".join(["0" if i == "1" else "1" for i in "{:032b}".format(n)]), 2)


if __name__ == "__main__":
    q = int(input())
    for q_itr in range(q):
        n = int(input())
        result = flippingBits(n)
        print(result)
