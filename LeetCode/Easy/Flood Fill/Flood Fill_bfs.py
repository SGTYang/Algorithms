class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:

        h, w = len(image), len(image[0])
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        color = image[sr][sc]
        visited = set()
        
        def bfs(r,c,newColor):
            que = collections.deque([])
            que.append((r,c))
            image[r][c] = newColor
            visited.add((r,c))
            while que:
                tr, tc = que.popleft()
                for y,x in directions:
                    nr, nc = tr+y, tc+x
                    if nr>=0 and nc>=0 and nr<h and nc<w and image[nr][nc] == color and (nr,nc) not in visited:
                        image[nr][nc] = newColor
                        que.append((nr,nc))
                        visited.add((nr,nc))
        bfs(sr,sc,newColor)

        return image
