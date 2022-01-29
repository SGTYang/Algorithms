def solution(gems):
    answer = [0,len(gems)-1]
    left, pointer =0, 0
    gems_dict = {gems[0]:1}
    len_set = len(set(gems))
    
    while pointer < len(gems):
        if len(gems_dict) < len_set:
            pointer += 1
            if pointer == len(gems):
                break
            gems_dict[gems[pointer]] = gems_dict.get(gems[pointer],0)+1
            
            
        else:
            if pointer-left < answer[1]-answer[0]:
                answer = [left, pointer]
            if gems_dict[gems[left]] == 1:
                del gems_dict[gems[left]]
            else:
                gems_dict[gems[left]] -= 1
            left += 1

    
    return [answer[0]+1,answer[1]+1]
