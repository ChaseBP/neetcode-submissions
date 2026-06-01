class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []
        row, col = len(heights), len(heights[0])
        pacificVisited = set()
        atlanticVisited = set()
        result = []
        def dfs(r,c,visited, prevHeight):
            # Base condition Bounds check, visited check and height check 
            if(
                r < 0  or
                r >= row or
                c < 0 or
                c >= col  or 
                (r,c) in visited or 
                heights[r][c] < prevHeight 
            ):
                return 
            
            visited.add((r,c))

            dfs(r-1,c,visited, heights[r][c])
            dfs(r+1,c,visited, heights[r][c])
            dfs(r,c-1,visited, heights[r][c])
            dfs(r,c+1,visited, heights[r][c])

        for r in range(row):
            #Pacific left 
            dfs(r,0,pacificVisited, heights[r][0])
            #Atlantic right
            dfs(r,col-1,atlanticVisited, heights[r][col-1])
        
        for c in range(col):
            # Pacific top
            dfs(0, c,pacificVisited, heights[0][c])
            # Atlantic bottom
            dfs(row-1, c, atlanticVisited, heights[row-1][c])
        
        for r in range(row):
            for c in range(col):
                if ((r,c) in pacificVisited and (r,c) in atlanticVisited):
                    result.append([r,c])
        
        return result
