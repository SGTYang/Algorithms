class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        seen = set()
        queue = collections.deque()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        m, n = len(mat), len(mat[0])
        
        for r in range(m):
            for c in range(n):
                if mat[r][c] == 0:
                    seen.add((r, c))
                    queue.append((r, c))
                    
        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in seen:
                    seen.add((nr, nc))
                    queue.append((nr, nc))
                    mat[nr][nc] = mat[r][c] + 1
                    
        return mat     
