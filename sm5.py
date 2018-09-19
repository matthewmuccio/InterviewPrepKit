#!/usr/bin/env python3


# Complete the commonChild function below.
def commonChild(s1, s2):
    dp = [[0]*(len(s2) + 1) for i in range(len(s1) + 1)]
    for i in range(len(s1) + 1):
        for j in range(len(s2) + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j] , dp[i][j - 1])
    return dp[len(s1)][len(s2)]


if __name__ == "__main__":
    s1 = input()
    s2 = input()
    result = commonChild(s1, s2)
    print(result)
