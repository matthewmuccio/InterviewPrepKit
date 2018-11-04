#!/bin/python3


import math


# Complete the primality function below.
def primality(n):
    if n < 2:
        return "Not prime"
    elif n <= 3:
        return "Prime"
    elif n % 2 == 0 or n % 3 == 0:
        return "Not prime"
    else:
        for i in range(3, int(math.sqrt(n) + 1), 2):
            if n % i == 0:
                return "Not prime"
    return "Prime"


if __name__ == "__main__":
    p = int(input())
    for p_itr in range(p):
        n = int(input())
        result = primality(n)
        print(result)
