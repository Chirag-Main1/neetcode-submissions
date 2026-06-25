from collections import deque
from typing import List

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        row, col = len(grid), len(grid[0])
        queue = deque()
        visit = set()

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 0:
                    queue.append([i,j])
                    visit.add((i,j))
        
        def addCell(r,c):
            if (r == row or c == col or r<0 or c<0 or (r,c) in visit or grid[r][c]==-1):
                return 
            queue.append([r,c])
            visit.add((r,c))
        
        dist = 0
        while queue:
            for i in range(len(queue)):
                dr, dc = queue.popleft()
                grid[dr][dc] = dist
                addCell(dr,dc+1)
                addCell(dr,dc-1)
                addCell(dr+1,dc)    
                addCell(dr-1,dc)

            dist += 1