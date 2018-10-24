#!/usr/bin/env python3


# Complete the maxRegion function below.
def maxRegion(grid):
    n, m = len(grid), len(grid[0])
    max_region_size = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                max_region_size = max(max_region_size, dfs(grid, i, j))
    return max_region_size

def dfs(grid, i, j):
    n, m = len(grid), len(grid[0])
    positions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    grid[i][j] = 0
    count = 1
    for pos in positions:
        if i + pos[0] in range(n) and j + pos[1] in range(m):
            if grid[i + pos[0]][j + pos[1]] == 1:
                count += dfs(grid, i + pos[0], j + pos[1])
    return count


if __name__ == "__main__":
    n = int(input())
    m = int(input())
    grid = []
    for _ in range(n):
        grid.append(list(map(int, input().rstrip().split())))
    res = maxRegion(grid)
    print(res)
