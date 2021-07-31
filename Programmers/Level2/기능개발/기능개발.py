def solution(progresses, speeds):
    answer = []
    i = (100-progresses[0])//speeds[0]
    if (100-progresses[0])%speeds[0] != 0:
        i += 1
    progresses.pop(0)
    speeds.pop(0)
    cnt = 1

    while len(progresses) != 0:
        if 100-progresses[0] <= speeds[0]*i:
            cnt += 1
            progresses.pop(0)
            speeds.pop(0)
        else:
            answer.append(cnt)
            i = (100-progresses[0])//speeds[0]
            if (100-progresses[0])%speeds[0] != 0:
                i += 1
            progresses.pop(0)
            speeds.pop(0)
            cnt = 1
    answer.append(cnt)   
    return answer
