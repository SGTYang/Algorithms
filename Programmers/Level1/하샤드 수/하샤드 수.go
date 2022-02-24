
func solution(x int) bool {
    num:= x
    sum:= 0
    
    for num!=0{
        sum+= num%10
        num /= 10
    }
    if x%sum==0{
        return true
    }
    return false
}
