def solution(numbers):
    answer = 0
    i = 0
    while i < 10:
        if i not in numbers:
            answer += i
        i += 1
    return answer
