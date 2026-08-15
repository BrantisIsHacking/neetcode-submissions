class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            hash = {}

            for column in row:
                if column != ".":
                    if column in hash:
                        return False

                    hash[column] = 1

            hash.clear()
        for c in range(len(board[0])):
            hash = {}

            for r in range(len(board)):
                if board[r][c] != ".":
                    if board[r][c] in hash:
                        return False

                    hash[board[r][c]] = 1

        for r in range(0, 9, 3):
            for c in range(0, 9, 3):
                hashb = {}

                for i in range(0, 3):
                    for j in range(0, 3):
                        if board[r+i][c+j] != ".":
                            if board[r+i][c+j] in hashb:
                                return False

                            hashb[board[r+i][c+j]] = 1
        return True
            
