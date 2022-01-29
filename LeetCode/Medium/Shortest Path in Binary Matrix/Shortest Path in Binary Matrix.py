class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        n = len(grid)
        distance = 0
        if grid[0][0] or grid[n-1][n-1]:
            return - 1
        
        directions = [[1,0],[-1,0],[0,1],[0,-1],[-1,-1],[1,1],[1,-1],[-1,1]]
        
        visited = set()
        
        queue = collections.deque([(0,0,1)])
        visited.add((0,0))
        
        while queue:
            i,j,distance = queue.popleft()
            if i == n-1 and j == n-1:
                return distance
            for y, x in directions:
                ny,nx = i+y, j+x
                
                if 0 <= ny < n and 0 <= nx < n:
                    if (ny,nx) not in visited and grid[ny][nx] == 0:
                        visited.add((ny,nx))
                        queue.append((ny,nx, distance+1))
        return -1
