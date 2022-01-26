def solution(record):
    answer = []
    uid_dict = {}
    verb_arry = []
    for i in record:
        verb, uid = i.split()[0],i.split()[1]
        if verb != 'Leave':
            name = i.split()[2]
            uid_dict[uid] = name
    for i in record:
        name = uid_dict[i.split()[1]]
        if i.split()[0] =="Enter":
            answer.append(f'{name}님이 들어왔습니다.')
        elif i.split()[0] =="Leave":
            answer.append(f'{name}님이 나갔습니다.')
            
    return answer
