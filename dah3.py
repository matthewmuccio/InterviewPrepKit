#!/usr/bin/env python3


if __name__ == "__main__":
    n = int(input().strip())
    for a0 in range(n):
        s = input().strip()
        anagram_pairs = 0
        m = {}
        for i in range(len(s)):
            for j in range(len(s) - i):
                s1 = "".join(sorted(s[j:j + i + 1]))
                m[s1] = m.get(s1, 0) + 1
        for key in m:
            anagram_pairs += (m[key] - 1) * m[key] // 2
        print(anagram_pairs)
