from collections import deque
def solution(priorities, location):
    answer = 0
    deq = deque([[value,index] for index,value in enumerate(priorities)])
    while deq:
        tmp = deq.popleft()
        if deq and max(deq)[0] > tmp[0]:
            deq.append(tmp)
        else:
            answer += 1
            if location == tmp[1]:
                return answer
