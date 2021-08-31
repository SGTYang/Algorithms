from collections import Counter
def solution(str1, str2):
    answer = 0
    str1 = str1.lower()
    str2 = str2.lower()

    str1_arr = []
    str2_arr = []
    for i in range(len(str1)-1):
        if str1[i:i+2].isalpha():
            str1_arr.append(str1[i:i+2])
    
    for i in range(len(str2)-1):
        if str2[i:i+2].isalpha():
            str2_arr.append(str2[i:i+2])
    
    count1 = Counter(str1_arr)
    count2 = Counter(str2_arr)
    
    ry = [min(count1[i],count2[i])*[i] for i in list(set(count1) & set(count2))]
    gkq = [max(count1[i],count2[i])*[i] for i in list(set(count1) | set(count2))]
    a1 = 0
    for i in range(len(ry)):
        for j in range(len(ry[i])):
            a1 += 1
    a2 = 0
    for i in range(len(gkq)):
        for j in range(len(gkq[i])):
            a2 += 1
    if a1 ==0 and a2 ==0:
        return 65536
    else:
        return int(a1/a2*65536)
