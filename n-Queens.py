# BT Approach --
# TC - O(n!)
# SC - O(n^2)

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n is None or n == 0: return []

        result = []

        grid = [[False for j in range(n)] for i in range(n)]

        def backtrack(row):
            # base
            # when all rows are processed
            if row == n:
                ans = []
                for i in range(n):
                    string = ""
                    for j in range(n):
                        if grid[i][j] == True:
                            string += "Q"
                        else:
                            string += "."
                    ans.append(string)
                result.append(ans)
                return

            # logic
            for col in range(n):
                if isSafe(row, col):
                    # action
                    grid[row][col] = True
                    # recurse
                    backtrack(row + 1)
                    # backtrack
                    grid[row][col] = False

        def isSafe(row, col):
            # check all cols
            for i in range(row - 1, -1, -1):
                if grid[i][col]:
                    return False
            # check upper left diagonals
            i, j = row, col
            while i >= 0 and j >= 0:
                if grid[i][j] == True:
                    return False
                i -= 1
                j -= 1
            # check upper right diagonal
            i, j = row, col
            while i >= 0 and j < n:
                if grid[i][j] == True:
                    return False
                i -= 1
                j += 1
            return True

        backtrack(0)
        return result
