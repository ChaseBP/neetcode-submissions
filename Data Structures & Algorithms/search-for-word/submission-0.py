class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # 2D grid

        def dfs(r, c, count):
            if count == len(word):
                return True
            # Base conditions
            if (
                r < 0
                or r >= len(board)
                or c < 0
                or c >= len(board[0])
                or board[r][c] != word[count]
            ):
                return False
            temp = board[r][c]
            board[r][c] = "#"
            found = (
                dfs(r + 1, c, count + 1)
                or dfs(r - 1, c, count + 1)
                or dfs(r, c + 1, count + 1)
                or dfs(r, c - 1, count + 1)
            )
            board[r][c] = temp
            return found

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == word[0]:
                    res = dfs(r, c, 0)
                    if res:
                        return True
        return False
