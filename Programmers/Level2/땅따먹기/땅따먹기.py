def solution(land):
    answer = 0
    path = [[0 for i in range(len(land[0]))]for j in range(len(land))]
    
    for i in range(len(land[0])):
        path[0][i] = land[0][i]
        
    for i in range(1,len(land)):
        for j in range(len(land[0])):
            path[i][j] = land[i][j]+max(path[i-1][:j]+path[i-1][j+1:])
            
    return max(path[-1])
