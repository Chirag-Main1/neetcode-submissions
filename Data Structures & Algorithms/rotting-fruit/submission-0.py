from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        queue = deque()
        rotten = set()
        fresh = 0

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    queue.append([i, j])
                    rotten.add((i, j))
                elif grid[i][j] == 1:
                    fresh += 1

        if fresh == 0:
            return 0
        if not queue:
            return -1

        def addCell(r, c):
            nonlocal fresh
            if (
                r < 0 or c < 0 or r >= row or c >= col or
                (r, c) in rotten or grid[r][c] != 1
            ):
                return  
            fresh -= 1
            queue.append([r, c])
            rotten.add((r, c))

        dist = -1

        while queue:
            for _ in range(len(queue)):
                dr, dc = queue.popleft()
                addCell(dr, dc + 1)
                addCell(dr, dc - 1)
                addCell(dr + 1, dc)
                addCell(dr - 1, dc)
            dist += 1

        return dist if fresh == 0 else -1