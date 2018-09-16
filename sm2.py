#!/usr/bin/env python3


if __name__ == "__main__":
    for word in [input() for _ in range(int(input()))]:
        print(len([i for i in range(len(word) - 1) if word[i] == word[i + 1]]))
