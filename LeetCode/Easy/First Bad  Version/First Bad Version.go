func firstBadVersion(n int) int {
    left, right := 1, n
    var mid int
    
    for left < right{
        mid = (left+right)/2
        
        if isBadVersion(mid){
            right = mid
        }else{
            left = mid+1
        }
    }
    return right
}
