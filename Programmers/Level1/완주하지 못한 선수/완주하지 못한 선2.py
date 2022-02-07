def solution(participant, completion):
    answer = ''
    dic={}
    for i in range(len(participant)):
        dic[participant[i]] = dic.get(participant[i],0)+1
    
    for i in range(len(completion)):
        dic[completion[i]] -= 1
        if dic[completion[i]] == 0:
            del dic[completion[i]]
        
    return "".join(list(dic.keys()))
