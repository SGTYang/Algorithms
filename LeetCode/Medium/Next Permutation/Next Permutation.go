func nextPermutation(nums []int)  {
    leng := len(nums)
    
    if leng <= 1 {
		return
	}
    k:= -1
    l:= 0
    
    for i:=leng-2; i>=0; i--{
        if nums[i] < nums[i+1]{
            k = i
            break
        }
    }
    
    if k==-1{
        nums = reverse(nums, 0, leng-1)
        return 
    }else{
        for i:=leng-1; i>=0; i--{
            if nums[i]>nums[k]{
                l = i
                break
            }
        }
    }
    
    nums[k], nums[l] = nums[l], nums[k]
    
    nums = reverse(nums, k+1, leng-1)
    return
}

func reverse(nums []int, s, e int) []int{ 
    for s<e{
        nums[s], nums[e] = nums[e], nums[s]
        s ++
        e --
    }
    return nums
}
