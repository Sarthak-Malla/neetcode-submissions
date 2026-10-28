class Solution:
    def isValidBox(self, x, y, box):
        dp = set()
        for i in range(x, x + 3):
            for j in range(y, y + 3):
                if box[i][j] in dp and box[i][j] != ".":
                    return False
                dp.add(box[i][j])
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 3x3 blocks
        n = len(board)

        for i in range(0, n, 3):
            for j in range(0, n, 3):
                if not self.isValidBox(i, j, board):
                    return False
        
        # rows
        for i in range(n):
            dp = set()
            for j in range(n):
                if board[i][j] in dp and board[i][j] != ".":
                    print("rows")
                    return False
                dp.add(board[i][j])
        
        # columns
        for i in range(n):
            dp = set()
            for j in range(n):
                if board[j][i] in dp and board[j][i] != ".":
                    return False
                dp.add(board[j][i])

        return True