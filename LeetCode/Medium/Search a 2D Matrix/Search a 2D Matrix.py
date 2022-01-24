class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        if not matrix or target is None:
            return False
        
        cols, rows = len(matrix[0]), len(matrix)
        left, right = 0, cols*rows-1
        
        while left<=right:
            index = (left+right)//2
            num = matrix[index//cols][index%cols]
            
            if num == target:
                return True
            elif num > target:
                right = index-1
            else:
                left = index + 1
                
        return False
