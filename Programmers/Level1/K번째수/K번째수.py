def solution(array, commands):
    answer = []
    
    for i in commands:
        first = i[0]
        second = i[1]
        third = i[2]
        answer.append((sorted(array[first-1:second])[third-1]))
            
    return answer
