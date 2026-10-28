class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def search(vector, target):
            l, r = 0, len(vector) - 1
            while l < r:
                m = (l+r) // 2
                if vector[m] == target:
                    return m
                if vector[m] < target:
                    l = m+1
                elif vector[m] > target:
                    r = m-1
            
            return l
        
        col = [row[0] for row in matrix]
        index = search(col, target)
        return matrix[index][search(matrix[index], target)] == target