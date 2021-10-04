from collections import deque
def solution(maps):
    answer = 0
    que = deque()
    h,w = len(maps), len(maps[0])
    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    visited = set()
    result = []
    
    que.append(((0,0),1))
    visited.add((0,0))
    
    while que:
        (tr, tc), cnt = que.popleft()
        if tr == h-1 and tc == w-1:
            result.append(cnt)
            
        for y,x in directions:
            nr, nc = y+tr, x+tc
            
            if nr>=0 and nc>=0 and nr<h and nc<w and maps[nr][nc] ==1 and (nr,nc) not in visited:
                que.append(((nr,nc),cnt+1))
                visited.add((nr,nc))
    
    print(result)
    if len(result)==0:
        return -1
    answer = min(result)
    return answer
