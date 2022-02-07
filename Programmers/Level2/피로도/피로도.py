from itertools import permutations
def solution(k, dungeons):
    arry = []
    for i in list(permutations(range(0,len(dungeons)),len(dungeons))):
        order=list(i)
        tmp = k
        cnt = 0
        for j in order:
            if dungeons[j][0]<=tmp:
                tmp-=dungeons[j][1]
                cnt +=1
        arry.append(cnt)

    return max(arry)
