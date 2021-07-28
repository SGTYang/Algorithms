def solution(record):
    answer = []
    dic = {}
    for i in range(len(record)):
        if record[i].split(' ')[0] != 'Leave':
            dic[record[i].split(' ')[1]] = record[i].split(' ')[2]
            
    for i in range(len(record)):
        if record[i].split(' ')[0] == 'Enter':
            answer.append('{}님이 들어왔습니다.'.format(dic[record[i].split(' ')[1]]))
        if record[i].split(' ')[0] == 'Leave':
            answer.append('{}님이 나갔습니다.'.format(dic[record[i].split(' ')[1]]))

    return answer
