func rotate(nums []int, k int)  {
    n := len(nums)
    k = k%n
    res := make([]int, n)
    var idx int
    
    for i:=k; i>0; i--{
        res[idx] = nums[n-i]
        idx ++
    }
    for i:=0; i<n-k; i++{
        res[idx] = nums[i]
        idx ++
    }
    for idx, val := range res{
        nums[idx] = val
    }
}
