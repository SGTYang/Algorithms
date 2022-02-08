def solution(n):
    arry = []
    for i in range(1,n+1):
        tmp = []
        for j in range(1, i+1):
            tmp.append(0)
        arry.append(tmp)
    x,y = -1,0
    num=1
    for i in range(n):
        for j in range(i,n):
            if i%3==0:
                x+=1
            elif i%3==1:
                y+=1
            else:
                x-=1
                y-=1
            arry[x][y]=num
            num+=1
    return sum(arry, [])
