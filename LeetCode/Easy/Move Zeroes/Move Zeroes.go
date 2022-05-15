func moveZeroes(nums []int)  {
    n := len(nums)
    left, right := 0, n-1
    res := make([]int, n)
    
    for _, val := range nums{
        if val == 0{
            res[right] = 0
            right --
        }else{
            res[left] = val
            left ++
        }
    }
    for idx, val := range res{
        nums[idx] = val
    }
}
