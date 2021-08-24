def solution(n,a,b):
    answer = 1

    while True:
        if a%2 !=0 and b%2 ==0 and b-a == 1 or a%2 ==0 and b%2 !=0 and a-b ==1:
            return answer
        
        if a%2 !=0:
            a += 1
        if b%2 !=0:
            b += 1
        b /= 2
        a /= 2
        answer += 1  
