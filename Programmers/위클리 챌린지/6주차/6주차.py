from collections import Counter
def solution(weights, head2head):
    answer = []
    beat = []
    win_rate = []
    win_cnt = 0
    win_rate = []
    for i in range (len(head2head)):
        head2head[i] = list(head2head[i])
        
    for i in range(len(head2head)):
        total_round = 0
        total_win = 0
        for j in range(len(head2head[i])):
            if head2head[i][j] != 'N':
                total_round +=1
            if head2head[i][j] == 'W':
                total_win += 1
        if total_round == 0 :
            win_rate.append(0)
        else:
            win_rate.append(total_win/total_round)
    
    for i in range(len(head2head)):
        cnt = 0
        for j in range(len(head2head[i])):
            if head2head[i][j] == 'W' and head2head[i][j] != 'N':
                if weights[i] < weights[j]:
                    cnt += 1
        beat.append(cnt)
    
    for i in range(len(head2head)):
        head2head[i] = (i+1,win_rate[i],beat[i],weights[i])

    t=sorted(head2head, key = lambda x: (-x[1],-x[2],-x[3],x[0]))
    
    for i in t:
        answer.append(i[0])
    return answer
