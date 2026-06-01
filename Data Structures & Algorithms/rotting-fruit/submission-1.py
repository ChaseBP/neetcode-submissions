from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1
        
        # Take the length of rows and cols
        row, col = len(grid), len(grid[0])
        
        # timeCount for counting the minimum minutes taken
        timeCount = 0
        freshCount = 0
        
        # Initialize queue for BFS
        queue = deque()
        
        # Add the (r,c) index for rotten fruits and count fresh fruits
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    freshCount += 1
                    
        # If there are no fresh oranges to begin with, 0 minutes are needed
        if freshCount == 0:
            return 0
            
        # Direction array Down, Up, Right and Left
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        
        # Perform BFS level by level
        while queue and freshCount > 0:
            # Increment time at the start of processing a new minute's wave
            timeCount += 1
            
            # Process all currently rotten oranges for the current minute
            for _ in range(len(queue)):
                cr, cc = queue.popleft()
                
                # Check all 4 adjacent directions
                for dr, dc in directions:
                    nr, nc = cr + dr, cc + dc
                    
                    # If neighbor is within bounds and contains a fresh orange
                    if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] == 1:
                        # Make it rotten
                        grid[nr][nc] = 2
                        freshCount -= 1
                        # Append to queue to rot its neighbors in the next minute
                        queue.append((nr, nc))
                        
        # If fresh fruits still remain, it's impossible to rot them all
        return timeCount if freshCount == 0 else -1