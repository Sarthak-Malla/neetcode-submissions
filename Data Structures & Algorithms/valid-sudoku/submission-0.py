import numpy as np

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def hasDup(lis: List[str]) -> bool:
            dic = {}
            for n in lis:
                if n == ".":
                    continue
                if dic.get(n) != None:
                    return True
                dic[n] = 1
            
            return False
        
        def getGrid(grid):
            x, y = len(grid), len(grid[0])
            out = []
            size = 3
            for i in range(0, x, size):
                rows = [*zip(*grid[i: i + size])]
                for j in range(0, y, size):
                    out.append([*chain(*zip(*rows[j: j + size]))])
            return out
        
        mat = np.array(board)

        # Rows
        for row in mat:
            if hasDup(row):
                return False
        # Columns
        for column in mat.T:
            if hasDup(column):
                return False
        
        # 3x3
        grid = getGrid(mat)
        for row in grid:
            if hasDup(row):
                return False
        
        return True
        


        