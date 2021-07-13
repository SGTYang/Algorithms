def solution(board, moves):
    answer = 0
    emp_stack = []
    
    for i in range(0, len(board)):
        globals()['stack{}'.format(i)] = []
        
    for i in range(0, len(board[0])):
        for j in range(0, len(board)):
            if board[len(board)-j-1][i]!=0:
                globals()['stack{}'.format(i)].append(board[len(board)-j-1][i])
            
    for i in moves:
        if len(globals()['stack{}'.format(i-1)]) >= 1:
            emp_stack.append(globals()['stack{}'.format(i-1)].pop())
            if len(emp_stack)>=2:
                if emp_stack[-2] == emp_stack[-1]:
                    answer+=2
                    emp_stack.pop()
                    emp_stack.pop()
            
    return answer
