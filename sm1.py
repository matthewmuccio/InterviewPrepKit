#!/usr/bin/env python3


# Complete the makeAnagram function below.
def makeAnagram(a, b):
    count = 0
    for i in range(97, 123):
        ia = sum(letter == chr(i) for letter in a)
        ib = sum(letter == chr(i) for letter in b)
        count += abs(ia - ib)
    return count


if __name__ == '__main__':
    a = input()
    b = input()
    res = makeAnagram(a, b)
    print(res)
