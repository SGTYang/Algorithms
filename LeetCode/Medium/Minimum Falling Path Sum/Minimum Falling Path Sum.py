class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        
        length = len(matrix)
        
        path = [[0 for x in range(length)] for y in range(length)]
        
        print(path)
        print(matrix[0])
        
        path[0] = matrix[0]
        
        for i in range(1, length):
            for j in range(length):
                if 0 < j < length-1:
                    path[i][j] = min(path[i-1][j-1], path[i-1][j], path[i-1][j+1]) + matrix[i][j]
                elif j == 0:
                    path[i][j] = min(path[i-1][j], path[i-1][j+1]) + matrix[i][j]
                else:
                    path[i][j] = min(path[i-1][j-1], path[i-1][j]) + matrix[i][j]
        print(path)
        
        return min(path[-1])
