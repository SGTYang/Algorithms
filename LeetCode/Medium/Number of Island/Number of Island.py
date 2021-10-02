class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        h,w = len(grid), len(grid[0])
        visited = set()
        que = collections.deque()
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        cnt = 0
        def bfs(r,c):
            que.append((r,c))
            visited.add((r,c))
            
            while que:
                tr, tc = que.popleft()
                
                for y,x in directions:
                    nr, nc = y+tr, x+tc
                    
                    if nr>=0 and nc>=0 and nr<h and nc<w and grid[nr][nc] == '1' and (nr,nc) not in visited:
                        que.append((nr,nc))
                        visited.add((nr,nc))
                
        for i in range(h):
            for j in range(w):
                if grid[i][j] == '1' and (i,j) not in visited:
                    bfs(i,j)
                    cnt += 1
        return cnt
