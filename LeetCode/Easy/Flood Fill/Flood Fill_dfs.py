class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        h, w = len(image), len(image[0])
        visited = set()
        
        def dfs(r,c, src_color, new_color):
            if r<0 or c<0 or r>=h or c>=w or (r,c) in visited or image[r][c] != src_color:
                return
            image[r][c] = new_color
            visited.add((r,c))
            dfs(r-1, c, src_color, new_color)
            dfs(r+1, c, src_color, new_color)
            dfs(r, c-1, src_color, new_color)
            dfs(r, c+1, src_color, new_color)
        
        dfs(sr, sc, image[sr][sc], newColor)
        
        return image
