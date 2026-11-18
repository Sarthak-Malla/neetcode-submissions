class Solution:
    def isValidNine(self, nine):
        df = Counter(nine)
        for k, v in df.items():
            if k != "." and v > 1:
                return False
        
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        m = n = 9

        # check all rows
        for i in range(m):
            if not self.isValidNine(board[i]): return False
        
        # check all columns:
        for j in range(n):
            col = [board[0][j]]
            for i in range(1, m):
                col.append(board[i][j])
            
            if not self.isValidNine(col): return False
        
        # check all boxes
        for k in range(0, m, 3):
            for l in range(0, n, 3):
                nine = []

                for i in range(k, k + 3):
                    for j in range(l, l + 3):
                        nine.append(board[i][j])
                
                if not self.isValidNine(nine): return False
        

        return True



