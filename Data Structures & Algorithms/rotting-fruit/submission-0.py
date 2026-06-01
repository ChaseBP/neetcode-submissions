class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1
        # Take the length of rows and cols
        row, col = len(grid), len(grid[0])
        # timeCount for counting the minimum minutes taken
        timeCount = 0
        freshCount =0
        # Initialize queue for BFS
        queue = deque()

        # Add the (r,c) index for rotten fruits
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    freshCount += 1
        
        if freshCount == 0:
            return 0 

        # Direction array Down, Up, Right and Left
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        # Perform BFS
        while queue and freshCount > 0:
            # Pop coords of rotten fruit
            
            for _ in range(len(queue)):
                cr, cc = queue.popleft()
                for dr, dc in directions:
                    # Get the nextRow and nextCol indices
                    nr, nc = cr + dr, cc + dc

                    # Check bounds and neighbour is a fresh fruit
                    if (
                        0 <= nr < row
                        and 0 <= nc < col
                        and grid[nr][nc] == 1
                    ):
                        # Decrement fresh count 
                        freshCount -= 1
                        # Convert the fresh banana to rotten banana (1->2)
                        grid[nr][nc] = 2
                        # Append index to queue
                        queue.append((nr, nc))
                       
            # Increment count by 1 after 1 level of bfs completes
            timeCount += 1
        return timeCount if freshCount == 0 else -1
        