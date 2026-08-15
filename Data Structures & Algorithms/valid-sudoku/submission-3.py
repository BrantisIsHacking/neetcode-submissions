class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            hashr = {}

            for column in row:
                if column != ".":
                    if column in hashr:
                        return False

                    hashr[column] = 1

        for c in range(len(board[0])):
            hashc = {}

            for r in range(len(board)):
                if board[r][c] != ".":
                    if board[r][c] in hashc:
                        return False

                    hashc[board[r][c]] = 1

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
            
