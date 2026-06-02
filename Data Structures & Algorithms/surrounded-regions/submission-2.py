class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return
        row, col = len(board), len(board[0])
        
        def dfs(r,c):
            if(
                r < 0 or
                r >= row or
                c < 0 or
                c >= col or 
                board[r][c] != "O"
            ):
                return 
            
            board[r][c] = "T"

            dfs(r-1,c)
            dfs(r+1,c)
            dfs(r,c+1)
            dfs(r,c-1)
        
        for r in range(row):
            dfs(r,0) #Left 
            dfs(r,col-1) #Right

        for c in range(col):
            dfs(0,c) #Top
            dfs(row-1,c) #Bottom

        for r in range(row):
            for c in range(col):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"
                    
        return




