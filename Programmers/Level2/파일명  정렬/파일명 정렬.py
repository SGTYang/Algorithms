def solution(files):
    answer = []
    for i in range(len(files)):
        head, number, tail= '','',''
        check = True
        cnt = 0
        for j in range(len(files[i])):
            if files[i][j].isdigit() and check:
                head = files[i][:j]
                a = j
                check = False
                
            if files[i][j].isdigit() and not check:
                number += files[i][j]
                cnt += 1
            if  not files[i][j].isdigit() and not check or(cnt >5):
                tail = files[i][j:]
                break
                
        answer.append([head,number,tail])
    answer.sort(key = lambda x : (x[0].upper(),int(x[1])))
    for i in range(len(answer)):
        answer[i] = "".join(answer[i])
    return answer
