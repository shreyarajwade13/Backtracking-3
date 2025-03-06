# BT Approach --
# TC - Exponential --> m * n * (3 ^ L )
# m * n because we are traversing the array to find the first character frim the word in the matrix
# 3^L since we are looking in three directions to find each character for the word of length L so 3^L

# SC - O(L) where L is length of the word

class Solution:
    def __init__(self):
        self.m = 0
        self.n = 0

    def exist(self, board: List[List[str]], word: str) -> bool:
        if board is None or len(board) == 0: return True

        self.m = len(board)
        self.n = len(board[0])

        for i in range(self.m):
            for j in range(self.n):
                if self.backtrack(board, i, j, word, 0):
                    return True

        return False

    def backtrack(self, board, r, c, word, index):
        # base
        if index == len(word): return True

        if r < 0 or c < 0 or r == self.m or c == self.n or board[r][c] == '#':
            return False

        # logic
        # T-L-D-R
        dirs = [[-1, 0], [0, -1], [1, 0], [0, 1]]
        # look for the first char from the word in matrix
        if board[r][c] == word[index]:
            # store the character in a variable before replacing it with '#'
            ch = board[r][c]
            # action
            board[r][c] = '#'
            # recurse
            # check in 3 dirs
            for direc in dirs:
                nr = r + direc[0]
                nc = c + direc[1]
                if self.backtrack(board, nr, nc, word, index + 1):
                    return True
            # backtrack
            board[r][c] = ch

        return False
