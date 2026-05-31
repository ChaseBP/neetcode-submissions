class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowset = {}
        colset = {}
        gridset = {}

        for r in range(9):
            for c in range(9):
                value = board[r][c]

                if value == '.':
                    continue 
                
                if r not in rowset:
                    rowset[r] = set()
                if c not in colset:
                    colset[c] = set()
                if (r//3, c//3) not in gridset:
                    gridset[(r//3, c//3)] = set()

                if (
                    value in rowset[r] or
                    value in colset[c] or 
                    value in gridset[(r//3,c//3)]
                ):
                    return False
                
                rowset[r].add(value)
                colset[c].add(value)
                gridset[(r//3, c//3)].add(value)

        return True