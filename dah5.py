#!/usr/bin/env python3


from collections import Counter
import os


# Complete the freqQuery function below.
def freqQuery(queries):
    freq = Counter()
    count = Counter()
    arr = []
    for q in queries:
        if q[0] == 1:
            count[freq[q[1]]] -= 1
            freq[q[1]] += 1
            count[freq[q[1]]] += 1
        elif q[0] == 2:
            if freq[q[1]] > 0:
                count[freq[q[1]]] -= 1
                freq[q[1]] -= 1
                count[freq[q[1]]] += 1
        else:
            arr.append(1) if count[q[1]] > 0 else arr.append(0)
    return arr


if __name__ == '__main__':
    q = int(input().strip())
    queries = []
    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))
    ans = freqQuery(queries)
    for i in ans:
        print(i)
