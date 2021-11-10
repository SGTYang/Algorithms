def solution(board):
    answer = 0
    
    dp = [[0 for i in range(len(board[0]))] for j in range(len(board))]
    
    for i in range(len(board)):
        for j in range(len(board[i])):
            if (i == 0 or j == 0) and board[i][j]==1:
                dp[i][j] = 1
            elif board[i][j] == 1:
                dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1
    
    for i in range(len(dp)):
        for j in range(len(dp[i])):
            answer = max(answer, dp[i][j])

    return answer**2
