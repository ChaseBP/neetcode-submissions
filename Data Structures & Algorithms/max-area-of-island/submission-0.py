class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        # Intialize the length of row and col and a visited HASHSET
        visited = set()
        row, col = len(grid), len(grid[0])

        # Initialize the max area variable
        maxArea = 0

        # Dfs function to traverse the grid

        def dfs(r, c, grid, visited):
            if (
                r < 0
                or r >= len(grid)
                or c < 0
                or c >= len(grid[0])
                or (r, c) in visited
                or grid[r][c] == 0
            ):
                return 0
            visited.add((r, c))

            return (
                1
                + dfs(r - 1, c, grid, visited)
                + dfs(r + 1, c, grid, visited)
                + dfs(r, c - 1, grid, visited)
                + dfs(r, c + 1, grid, visited)
            )

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1 and (r, c) not in visited:
                    currArea = dfs(r, c, grid, visited)

                    maxArea = max(maxArea, currArea)

        return maxArea