class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        cnt = 0
        que = collections.deque()
        visited = set()
        h,w = len(grid), len(grid[0])
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        
        for i in range(h):
            for j in range(w):
                if grid[i][j] == 2:
                    que.append((i,j,0))
                    visited.add((i,j))
        
        while que:

            tr, tc, cnt = que.popleft()
            for y,x in directions:
                nr, nc = tr+y, tc+x
                if nr>=0 and nc>=0 and nr<h and nc<w and (nr,nc) not in visited and grid[nr][nc]==1:
                    visited.add((nr,nc))
                    que.append((nr,nc,cnt+1))
                    grid[nr][nc] = 2
        
        for i in range(len(grid)):
            if 1 in grid[i]:
                return -1
        
        return cnt
