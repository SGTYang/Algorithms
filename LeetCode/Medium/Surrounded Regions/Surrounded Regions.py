class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        h, w = len(board), len(board[0])
        visited = set()
        
        def dfs(r,c):
            if r<0 or c<0 or r>=h or c>=w or (r,c) in visited or board[r][c]=='X':
                return
            visited.add((r,c))
            board[r][c] = "#"
            dfs(r-1,c)
            dfs(r+1,c)
            dfs(r,c-1)
            dfs(r,c+1)
            
        for i in range(len(board)):
            for j in range(len(board[i])):
                if i == 0 or i == h-1 or j == 0 or j == w-1:
                    dfs(i,j)
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == '#':
                    board[i][j] = 'O'
        return board
            
