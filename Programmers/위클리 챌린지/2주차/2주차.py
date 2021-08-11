def solution(scores):
    answer = ''
    avg_score = []
    scores = list(map(list, zip(*scores)))
    for i in range(len(scores)):
        score_tmp = []
        for j in range(len(scores[i])):
            if i == j :
                if (max(scores[i]) == scores[i][j] and scores[i].count(max(scores[i]))==1) or \
                (min(scores[i]) == scores[i][j] and scores[i].count(min(scores[i]))==1):
                    continue
                else:
                    score_tmp.append(scores[i][j])
            else:
                score_tmp.append(scores[i][j])
            
        avg_score.append(sum(score_tmp)/len(score_tmp))
        
    for i in range(len(avg_score)):
        if avg_score[i]>=90:
            answer += 'A'
        elif avg_score[i]>=80:
            answer += 'B'
        elif avg_score[i]>=70:
            answer += 'C'
        elif avg_score[i]>=50:
            answer += 'D'
        else:
            answer += 'F'
        
    return answer
