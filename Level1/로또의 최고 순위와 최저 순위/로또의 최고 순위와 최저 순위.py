def solution(lottos, win_nums):
    answer = []
    answer.append(determine(max_num(lottos, win_nums)))
    answer.append(determine(min_num(lottos, win_nums)))
    return answer

def determine(number):
    if number == 6:
        return 1
    elif number == 5:
        return 2
    elif number == 4:
        return 3
    elif number == 3:
        return 4
    elif number == 2:
        return 5
    else:
        return 6
def min_num(lottos, win_nums):
    set_lottos = set(lottos)
    set_win_nums = set(win_nums)
    return len(set_win_nums)-len(set_win_nums - set_lottos)

def max_num(lottos, win_nums):
    set_lottos = set(lottos)
    set_win_nums = set(win_nums)
    return len(set_win_nums)-len(set_win_nums - set_lottos)+lottos.count(0)
