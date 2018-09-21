#!/usr/bin/env python3


# Complete the luckBalance function below.
def luckBalance(k, contests):
    sorted_contests = sorted(contests, key=lambda x: x[0], reverse= True)
    total = 0
    for l, ir in sorted_contests:
        if ir == 1 and k > 0:
            total += l
            k -= 1
        elif ir == 0:
            total += l
        else:
            total -= l
    return total


if __name__ == "__main__":
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    contests = []
    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))
    result = luckBalance(k, contests)
    print(result)
