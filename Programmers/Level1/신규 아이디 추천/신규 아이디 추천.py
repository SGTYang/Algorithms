def solution(new_id):
    answer = ''
    new_id = new_id.lower()
    tmp = []
    for i in range(len(new_id)):
        if (ord(new_id[i])>=97 and ord(new_id[i])<=122) or \
        (ord(new_id[i])==45 or ord(new_id[i])==95 or \
         ord(new_id[i]) ==46) or (ord(new_id[i]) >=48 and ord(new_id[i])<=57):
            tmp.append(new_id[i])
            
    new_id = "".join(tmp)
    
    check = False
    tmp = []
    for i in range(len(new_id)):
        if new_id[i] == '.' and not check:
            check = True
            tmp.append(new_id[i])
        elif new_id[i] != '.':
            check = False
            tmp.append(new_id[i])
            
    if tmp[0] == '.' or tmp[-1] == '.':
        if len(tmp) < 1:
            tmp = []
        else:
            if tmp[0] == '.':
                tmp = tmp[1:]
            else:
                tmp = tmp[:-1]
    if len(tmp) == 0:
        tmp.append('a')
    
    if len(tmp) > 15:
        tmp = tmp[:15]
    
    while tmp[-1] == '.':
        tmp = tmp[:-1]
    
    while len(tmp)<3:
        tmp.append(tmp[-1])
        
    return ''.join(tmp)
