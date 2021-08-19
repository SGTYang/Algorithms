from collections import deque
def solution(priorities, location):
    answer = 0
    deq = deque([(value,index) for index,value in enumerate(priorities)])

    while len(deq):
        point = deq.popleft()
        if deq and max(deq)[0] > point[0]:
            deq.append(point)
        else:
            answer += 1
            if point[1] == location:
                break
    return answer
