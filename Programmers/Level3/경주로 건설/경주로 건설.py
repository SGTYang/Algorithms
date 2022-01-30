from collections import deque
def solution(board):
    answer = 0
    h = len(board)
    w = len(board[0])
    
    def bfs(start):
        cost_arry = []
        for i in range(len(board)):
            tmp = []
            for j in range(len(board[0])):
                tmp.append(float('inf'))
            cost_arry.append(tmp)
            
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        cost_arry[0][0] = 0
        que = deque([])
        que.append(start)
        while que:
            i,j,cost,head = que.popleft()
            for k in range(len(directions)):
                if k == head:
                    n_cost = cost+100
                else:
                    n_cost = cost+600
                y,x = directions[k]
                ny, nx = y+i, x+j
                if 0<=ny<h and 0<=nx<w and board[ny][nx] != 1 and (ny,nx) and cost_arry[ny][nx]> n_cost:
                    que.append((ny,nx,n_cost,k))
                    cost_arry[ny][nx] = n_cost
        return cost_arry[-1][-1]
    
    return min(bfs((0,0,0,1)),bfs((0,0,0,3)))
 
