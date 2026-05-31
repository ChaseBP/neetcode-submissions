class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
              # If there's no value in grid
       if not grid:
        return 0
       # Get the total no of rows and cols 
       r,c = len(grid), len(grid[0])
       # hashset for maintaining coords
       visited = set()
        # count for maintaining 
       totalIslandCount = 0  

       # dfs function for traversal

       def dfs(r,c,grid, visited):
            # Conditions 
            # 1. Row out of bounds
            # 2. Col out of bounds 
            # 3. Cell is already visited or it's not a land
            if (r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or (r,c) in visited or grid[r][c] == "0"):
                return
            # ^ backtrack when fail condition met
            # Mark the current cell ad visited
            visited.add((r,c))
            #Traverse up, down, left and right
            dfs(r-1,c,grid,visited)
            dfs(r+1,c,grid,visited)
            dfs(r,c-1,grid,visited)
            dfs(r,c+1,grid,visited)
        # Loop through grid
       for row in range(r):
         for col in range(c):
         # Find a cell which is a land (i.e (row,col) == "1") and check if it's not visited
            if grid[row][col] == "1" and (row,col) not in visited:    
                # Island found -> increment count
                totalIslandCount += 1 
                #Traverse neighbours for adjacent lands 
                dfs(row,col,grid,visited)
        
       return totalIslandCount
    


