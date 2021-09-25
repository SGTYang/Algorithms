class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        if not grid:
            return 0
        
        h,w = len(grid), len(grid[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        max_area = 0
        
        for i in range(h):
            for j in range(w):
                if grid[i][j] == 1:
                    area = 1
                    grid[i][j] = '#'
                    que = collections.deque([])
                    que.append((i,j))
                    while que:
                        r, c = que.popleft()
                        for y,x in directions:
                            nr = r+y
                            nc = c+x                         
                            if nr>=0 and nc>=0 and nr<h and nc<w and grid[nr][nc]==1:
                                area += 1
                                grid[nr][nc] = '#'
                                que.append((nr,nc))
                    max_area = max(max_area, area)
                    
        return max_area
