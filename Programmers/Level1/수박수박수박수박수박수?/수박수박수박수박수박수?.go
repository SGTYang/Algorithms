func solution(n int) string {
    word:="수박"
    var answer string
    for i:=0; i<n/2; i++{
        answer += word
    }
    
    if n%2 != 0{
        answer += "수"
    }
    
    return answer
}
