func containsDuplicate(nums []int) bool {
    var dict map[int]int
    dict = make(map[int]int)
    
    for _,v := range nums{
        if _, exsists := dict[v]; exsists{
            return true
        }else{
            dict[v] = 1
        }
    }
    return false
}
