#!/usr/bin/env python3


from collections import Counter


# Complete the reverseShuffleMerge function below.
def reverseShuffleMerge(s):
    word = []
    freqs = Counter(s)
    reqs = {k: v/2 for k, v in freqs.items()}
    avail_skips = {k: v/2 for k, v in freqs.items()}
    skipped = []

    for c in reversed(s):
        if reqs[c] == 0:
            continue
        if avail_skips[c] > 0:
            avail_skips[c] -= 1
            skipped.append(c)
        elif len(skipped) == 0:
            word.append(c)
        else:
            i = 0
            skipped.append(c)
            avail_skips[c] -= 1
            min_c = chr(ord("a") - 1)
            while i < len(skipped):
                i = index_of(skipped, find_min_bounded(skipped, i, min_c), i)
                sc = skipped[i]
                if reqs[sc] == 0:
                    min_c = sc
                    continue
                word.append(sc)
                reqs[sc] -= 1
                avail_skips[sc] += 1
                i += 1
                if sc == c:
                    break
            skipped = skipped[i:]

    return "".join(word)

def find_min_bounded(arr, start, mn_c):
    mn = "z"
    for i in range(start, len(arr)):
        if arr[i] < mn and arr[i] > mn_c:
            mn = arr[i]
    return mn

def index_of(arr, v, start):
    for i in range(start, len(arr)):
        if arr[i] == v:
            return i


if __name__ == "__main__":
    s = input()
    result = reverseShuffleMerge(s)
    print(result)
