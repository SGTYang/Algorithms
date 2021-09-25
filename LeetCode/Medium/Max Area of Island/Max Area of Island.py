class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        h,w = len(grid), len(grid[0])
        visited = set()
        max_area = 0
        
        def dps(r,c):
            nonlocal max_area, area
            if r<0 or c<0 or r>=h or c>=w or grid[r][c] ==0 or (r,c) in visited:
                return
            
            grid[r][c] ='#'
            visited.add((r,c))
            area = area+1
            
            dps(r-1,c)
            dps(r+1,c)
            dps(r,c-1)
            dps(r,c+1)
            
        for i in range(h):
            for j in range(w):
                if grid[i][j]==1:
                    area=0
                    dps(i,j)
                    max_area = max(max_area, area)
                    
        return max_area     
