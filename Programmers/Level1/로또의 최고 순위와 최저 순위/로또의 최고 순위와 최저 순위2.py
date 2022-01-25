def solution(lottos, win_nums):
    answer = []
    win_nums = set(win_nums)
    
    rank = {6:1,5:2,4:3,3:4,2:5,1:6,0:6}
    correct_nums = 0
    zero_nums = 0
    
    for i in range(len(lottos)):
        if lottos[i] in win_nums:
            correct_nums+=1
        elif lottos[i] == 0:
            zero_nums += 1
    return [rank[correct_nums+zero_nums], rank[correct_nums]]
