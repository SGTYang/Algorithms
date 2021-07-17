def solution(lottos, win_nums):
    answer = []
    
    switch(n):
        case 6: 
            rank = 1
            break
        case 5:
            rank = 2
            break
        case 4:
            rank = 3
            break
        case 3:
            rank = 4
            break
        case 2:
            rank = 5
            break
            
    set_lottos = set(lottos)
    set_win_nums = set(win_nums)
    
    print(set_lottos - set_win_nums)
    
    return answer

def min_num(lottos, win_nums):
    set_lottos = set(lottos)
    set_win_nums = set(win_nums)
    
    print(set_lotots - set_win_nums)
    return set_lottos
