#!/usr/bin/env python3


def fibonacci(n):
    if n == 0 or n == 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Alternative implementation using dynamic programming.
memory = {}
def fibonacci2(n):
    if n < 2:
        return n
    if not n in memory.keys():
        memory[n] = fibonacci2(n - 1) + fibonacci2(n - 2)
    return memory[n]


if __name__ == "__main__":
    n = int(input())
    print(fibonacci(n))
