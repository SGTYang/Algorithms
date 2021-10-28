import sys
sys.setrecursionlimit(10**5)
def solution(n):
    answer = 0
    memo = {0:0, 1:1}
    
    def fibo(n):
        if n in memo:
            return memo[n]
        if n not in memo:
            memo[n] = fibo(n-2)+fibo(n-1)
            return (fibo(n-2)+fibo(n-1))
    
    return fibo(n)%1234567
