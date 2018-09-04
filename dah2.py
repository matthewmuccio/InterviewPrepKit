#!/usr/bin/env python3


if __name__ == '__main__':
    for _ in range(int(input())):
        s1 = set(input())
        s2 = set(input())
        result = s1.intersection(s2)
        print("NO") if not result else print("YES")
