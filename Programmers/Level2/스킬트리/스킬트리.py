def solution(skill, skill_trees):
    answer = 0
    dic = {}
    for i in range(len(skill)):
        dic[skill[i]] = i

    for i in range(len(skill_trees)):
        check = 0
        wrong = False
        for j in range(len(skill_trees[i])):
            if skill_trees[i][j] in dic:
                if dic[skill_trees[i][j]] == check:
                    check +=1
                else:
                    wrong = True
        if not wrong:
            answer +=1

    return answer
