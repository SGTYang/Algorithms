func intersect(nums1 []int, nums2 []int) []int {
    var ans []int
    dict := make(map[int]int)
    l1, l2 := len(nums1), len(nums2)
    
    if l1 < l2{
        nums1, nums2 = nums2, nums1
    }
    
    for _, val := range nums2{
        if _, exists := dict[val]; exists{
            dict[val] += 1
        }else{
            dict[val] = 1
        }
    }
    
    for _, val := range nums1{
        if _, exists := dict[val]; exists{
            if dict[val] > 0{
                dict[val] -= 1
                ans = append(ans,val)
            }
        }
    }
    return ans
}
