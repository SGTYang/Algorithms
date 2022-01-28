def solution(m, n, board):
    answer = 0
    loop = True
    
    for i in range(len(board)):
        tmp = []
        for j in range(len(board[i])):
            tmp.append(board[i][j])
        board[i] = tmp
    
    while loop:
        block = []
        for i in range(len(board)-1):
            for j in range(len(board[i])-1):
                if board[i][j] != 'x' and board[i][j] == board[i][j+1]:
                    if board[i+1][j] == board[i][j] and board[i+1][j+1] == board[i][j]:
                        block.append((i,j))
                        block.append((i,j+1))
                        block.append((i+1,j))
                        block.append((i+1,j+1))  
        
        if len(block) == 0:
            break
        answer += len(list(set(block)))
        
        for i in list(set(block)):
            a,b = i
            board[a][b] = 'x'
        check = True
        while check:
            check = False
            for i in range(len(board)-1,0,-1):
                for j in range(len(board[i])):
                    if board[i][j] == 'x' and board[i-1][j] != 'x':
                        board[i][j], board[i-1][j] = board[i-1][j], 'x'
                        check = True
                    
        
    return answer
