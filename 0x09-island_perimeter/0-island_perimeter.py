#!/usr/bin/python3
"""Island perimeter computing module.
"""


def island_perimeter(grid: list[list[int]]) -> int:
    """Computes the perimeter of an island with no lakes.
    """
    N = len(grid)
    M = len(grid[0])
    def dfs(r, c):
        if r < 0 or r >= N or c >= M or grid[r][c] == 0:
            return 1
        if grid[r][c] == 1:
            grid[r][c] = 2
            return dfs(r - 1, c) + dfs(r + 1, c) + dfs(r, c - 1) + dfs(r, c + 1)
        return 0

    perimeter = 0
    for r in range(N):
        for c in range(M):
            if grid[r][c] == 1:
                perimeter += dfs(r, c)

    return perimeter
