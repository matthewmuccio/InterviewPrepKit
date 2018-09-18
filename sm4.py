#!/usr/bin/env python3


# Complete the substrCount function below.
def substrCount(n, s):
    curr = None
    count = 0
    l = []
    # 1st pass:
    for i in range(n):
        if s[i] == curr:
            count += 1
        else:
            if curr is not None:
                l.append((curr, count))
            curr = s[i]
            count = 1
    l.append((curr, count))
    ans = 0
    # 2nd pass:
    for i in l:
        ans += (i[1] * (i[1] + 1)) // 2
    # 3rd pass:
    for i in range(1, len(l) - 1):
        if l[i - 1][0] == l[i + 1][0] and l[i][1] == 1:
            ans += min(l[i - 1][1], l[i + 1][1])
    return ans


if __name__ == "__main__":
    n = int(input())
    s = input()
    result = substrCount(n, s)
    print(result)
