def solution(n,a,b):
    answer = 1

    while True:
        if a%2 !=0 and b%2 ==0 and b-a == 1 or a%2 ==0 and b%2 !=0 and a-b ==1:
            return answer
        
        b = (b+1)//2
        a = (a+1)//2
        
        answer += 1  
