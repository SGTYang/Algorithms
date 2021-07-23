def solution(n):
	# 2부터 n까지의 숫자 배열 만들기
    num_set = set(range(2, n+1))

    for i in range(2, n+1):
      #에라토스테네스의 체 이용
        if i in num_set: # 배수 제거
            num_set -= set(range(i*2, n+1, i))

    answer = len(num_set)

    return answer
