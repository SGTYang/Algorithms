def solution(new_id):
    answer = ''
    
    def dot_check(new_id):
        if new_id[0] == '.':
            new_id = new_id[1:]
        if len(new_id) != 0 and new_id[-1] == '.':
            new_id = new_id[:len(new_id)-1]
        return new_id
    new_id = new_id.lower()

    tmp = ''
    # 2단계
    for i in new_id:
        if (ord(i) >= ord('a') and ord(i) <= ord('z')) or i =='-' or i =='_' or i =='.' or i.isdigit():
            tmp+=i
    new_id = tmp
    # 3단계
    dot=False
    tmp = ''
    for i in new_id:
        if i == '.':
            if dot:
                pass
            else:
                dot=True
                tmp += i
        else:
            dot=False
            tmp+= i
    new_id = tmp

    # 4단계
    new_id = dot_check(new_id)
    # 5단계
    if len(new_id) == 0:
        new_id = 'a'
    # 6단계
    if len(new_id) >= 16:
        new_id = new_id[:15]
        while new_id[-1] == '.':
            new_id = new_id = new_id[:len(new_id)-1]
    # 7단계
    if len(new_id) <= 2:
        while len(new_id) <3:
            new_id += new_id[-1]
    print(new_id)
    return new_id
