#!/usr/bin/env python3


# Complete the isBalanced function below.


if __name__ == "__main__":
    table =  {")":"(", "]":"[", "}":"{"}
    for _ in range(int(input())):
        stack = []
        for x in input():
            if stack and table.get(x) == stack[-1]:
                stack.pop()
            else:
                stack.append(x)
        print("NO" if stack else "YES")
