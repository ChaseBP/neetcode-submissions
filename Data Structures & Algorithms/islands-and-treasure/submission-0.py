class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid:
            return 
        
        # Find row and col lengths
        row,col = len(grid), len(grid[0])
        # Visited for maintaining visited cells
        visited = set()
        # Initialize queue for BFS
        queue = deque()

        # Append treasure cells to queue

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 0:
                    queue.append((r,c))
                    visited.add((r,c))

        # Perform BFS
        while queue:
            # Pop the first cell from the queue
            cr,cc = queue.popleft()

            directions = [[1,0],[-1,0],[0,1],[0,-1]]

            for dr, dc in directions:
                nr, nc = cr + dr, cc + dc

                # If it is in bounds, not visited and not water cell, then add to queue and update distance
                if(0<= nr < row and 0<= nc < col and (nr,nc) not in visited and grid[nr][nc] != -1):

                    visited.add((nr,nc))
                    grid[nr][nc] = grid[cr][cc] + 1 
                    queue.append((nr,nc))

