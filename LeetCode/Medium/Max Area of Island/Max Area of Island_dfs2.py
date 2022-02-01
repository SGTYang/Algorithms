class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        h,w = len(grid), len(grid[0])
        area_arry = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        def dfs(i,j,grid,cnt):
            
            if i<0 or j<0 or i>=h or j>=w or grid[i][j] == 0:
                return 0
            
            grid[i][j] = 0
            
            return 1 + dfs(i+1,j,grid,cnt) + dfs(i-1,j,grid,cnt) + dfs(i,j+1,grid,cnt) + dfs(i,j-1,grid,cnt)
    
        
        max_area = 0
        for i in range(h):
            for j in range(w):
                if grid[i][j] == 1:
                    max_area = max(max_area,dfs(i,j,grid,0))
                    
        return max_area
