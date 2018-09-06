#!/usr/bin/env python3


def ransom_note(magazine, note):
    rlen = len(note)
    mlen = len(magazine)
    magazine.sort()
    note.sort()
    i = 0
    j = 0
    count = 0
    while i < rlen and j < mlen:
        if note[i] == magazine[j]:
            count += 1
            i += 1
        j += 1
    if count == rlen:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    mn = input().split()
    m = int(mn[0])
    n = int(mn[1])
    magazine = input().rstrip().split()
    note = input().rstrip().split()
    ransom_note(magazine, note)
