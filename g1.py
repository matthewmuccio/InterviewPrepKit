#!/usr/bin/env python3


def dfs(s):
    global visited, alist, val_count
    visited[s] = 1
    l = len(alist[s])
    val_count += 1
    if l != 0:
        for i in range(l):
            if visited[alist[s][i]] == 0:
                dfs(alist[s][i])


if __name__ == "__main__":
    q = int(input().strip())
    val_count = 0
    for a0 in range(q):
        n, m, clib, croad = map(int, input().split())
        visited = [0 for i in range(n + 1)]
        alist = [[] for i in range(n + 1)]
        count = 0
        roads = 0
        road = []
        current = 0
        for a1 in range(m):
            city_1, city_2 = map(int, input().split())
            alist[city_1].append(city_2)
            alist[city_2].append(city_1)
        if m == 0 or croad >= clib:
            print(n * clib)
        else:
            for i in range(1, n + 1):
                if visited[i] == 0:
                    val_count = 0
                    dfs(i)
                    road.append(val_count)
            ans = 0
            p = len(road)
            for i in range(p):
                ans += min((road[i] - 1) * croad + clib, road[i] * clib)
            print(ans)
