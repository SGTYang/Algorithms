def solution(board, moves):
    answer = 0
    stack = []
    
    for i in range(len(moves)):
        for j in range(len(board)):
            if board[j][moves[i]-1] != 0:
                if len(stack)==0:
                    stack.append(board[j][moves[i]-1]) 
                else:
                    if stack[-1] == board[j][moves[i]-1]:
                        stack.pop()
                        answer += 2
                    else:
                        stack.append(board[j][moves[i]-1])
                board[j][moves[i]-1] = 0
                break
    return answer
