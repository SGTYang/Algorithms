def solution(n):
    answer = 0
    star = n+1
    while 1:
        if bin(star).count("1") == bin(n).count("1"):
            return star
        else:
            star += 1
    return answer
