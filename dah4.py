#!/usr/bin/env python3


from collections import defaultdict
#import os


# Complete the countTriplets function below.
def countTriplets(arr, r):
    d1 = defaultdict(int)
    d2 = defaultdict(int)
    count = 0
    for i in arr:
        count += d2[i]
        d2[i * r] += d1[i]
        d1[i * r] += 1
    return count


if __name__ == '__main__':
#    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    nr = input().rstrip().split()
    n = int(nr[0])
    r = int(nr[1])
    arr = list(map(int, input().rstrip().split()))
    ans = countTriplets(arr, r)
    print(ans)
#    fptr.write(str(ans) + '\n')
#    fptr.close()
