func moveZeroes(nums []int)  {
    var noneZ int
    
    for idx, _ := range nums{
        if nums[idx] != 0{
            nums[noneZ], nums[idx] = nums[idx], nums[noneZ]
            noneZ ++
        }
    }
    
}
