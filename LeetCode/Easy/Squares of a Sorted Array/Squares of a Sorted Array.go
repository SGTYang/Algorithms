func sortedSquares(nums []int) []int {
    n := len(nums)
    res := make([]int,n)

    left, right := 0, len(nums)-1
    
    for i:=n-1; i>=0; i--{
        if Abs(nums[left]) < Abs(nums[right]){
            res[i] = nums[right]*nums[right]
            right --
        }else{
            res[i] = nums[left]*nums[left]
            left ++
        }
    }
    return res
}

func Abs(num int) int{
    if num < 0{
        return -num
    }
    return num
}
