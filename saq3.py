#!/usr/bin/env python3


# Complete the largestRectangle function below.
def largestRectangle(h):
    max_area = 0
    for i in range(len(h)):
        count = 0
        for j in range(i, -1, -1):
            if h[j] >= h[i]:
                count += 1
            else:
                break
        for k in range(i+1, len(h)):
            if h[k] >= h[i]:
                count += 1
            else:
                break
        area = h[i] * count
        if area > max_area:
            max_area = area
    return max_area


if __name__ == "__main__":
    n = int(input())
    h = list(map(int, input().rstrip().split()))
    result = largestRectangle(h)
    print(result)
