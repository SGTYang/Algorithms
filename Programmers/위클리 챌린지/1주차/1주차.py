def solution(price, money, count):
    # 100 -> 200 -> 300 -> 400,  total sum = 100 + 200 + 300 + 400 = 1,000 -> 등차수열의 합
    
    a = price # 1항
    d = price # 공차
    n = count # 항개수
    
    answer = (n*(2*a+(n-1)*d)/2) - money
    
    # 돈이 남거나 부족하지 않을때
    if answer <= 0:
        return 0
    
    return answer
