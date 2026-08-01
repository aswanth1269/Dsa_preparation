class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        fresh, minutes = 0, 0
        rows, cols = len(grid), len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append([r, c])
                if grid[r][c] == 1:
                    fresh += 1
        direction = [[0,1],[0, -1], [1,0], [-1, 0]]
        
        while q and fresh > 0:
            for i in range(len(q)):
                r,c = q.popleft()
                for dr, dc in direction:
                    ro, co = dr + r, dc + c
                    if (ro < 0 or ro == len(grid) or co < 0 or co == len(grid[0]) or grid[ro][co] != 1):
                        continue
                    grid[ro][co] = 2
                    q.append([ro, co])
                    fresh -= 1
            minutes += 1
        return minutes if fresh == 0 else -1