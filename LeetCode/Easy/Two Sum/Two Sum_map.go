func twoSum(nums []int, target int) []int {
    var dict map[int]int
    
    dict = make(map[int]int)
    
    for i,v := range nums{
        find := target-v
        if val, exists := dict[find]; exists{
            return []int{val,i}
        }
        dict[v] = i
    }
    return []int{}
}
