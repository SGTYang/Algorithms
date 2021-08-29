def solution(rows, columns, queries):
    answer = []
    
    arry = [[0 for i in range(columns)] for j in range(rows)]
    t = 1
    
    for i in range(len(arry)):
        for j in range(len(arry[i])):
            arry[i][j] = t
            t += 1
    
    for x1,y1,x2,y2 in queries:
        tmp = arry[x1-1][y1-1]
        min_value = tmp
        for i in range(x1-1,x2-1):
            arry[i][y1-1] = arry[i+1][y1-1]
            min_value = min(arry[i][y1-1],min_value)
            
        for i in range(y1-1,y2-1):
            arry[x2-1][i] = arry[x2-1][i+1]
            min_value = min(arry[x2-1][i],min_value)
        for i in range(x2-1,x1-1,-1):
            arry[i][y2-1] = arry[i-1][y2-1]
            min_value = min(arry[i][y2-1],min_value)
        for i in range(y2-1,y1-1,-1):
            arry[x1-1][i] = arry[x1-1][i-1]
            min_value = min(arry[x1-1][i],min_value)
        arry[x1-1][y1] = tmp
        
        answer.append(min_value)       
            
    return answer
