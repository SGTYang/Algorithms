func maxSubArray(nums []int) int {
    var dp []int 
    
    dp = make([]int, len(nums))
    dp[0] = nums[0]
    
    for i:=1; i<len(nums); i++{
        if dp[i-1]+nums[i]<nums[i]{
            dp[i] = nums[i]
        }else{
            dp[i] = nums[i]+dp[i-1]
        }
    }
    
    fmt.Println(dp)
    fmt.Println(findMax(dp))
    return findMax(dp)
}

func findMax(list []int) int{
    max:=list[0]
    
    for _, val := range list[1:]{
        if val > max{
            max = val
        }
    }
    return max
}
