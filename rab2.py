#!/usr/bin/env python3


# Complete the stepPerms function below.
seen = {0: 1}
def stepPerms(n):
    if n < 0:
        return 0
    if n in seen:
        return seen[n]
    ret = stepPerms(n - 1)
    ret += stepPerms(n - 2)
    ret += stepPerms(n - 3)
    seen[n] = ret
    return ret


if __name__ == "__main__":
    s = int(input())
    output = []
    for s_itr in range(s):
        n = int(input())
        res = stepPerms(n)
        output.append(res)
    [print(_) for _ in output]
