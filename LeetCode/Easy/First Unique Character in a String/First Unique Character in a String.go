func firstUniqChar(s string) int {
    string_map := make(map[rune]int)
    
    for _, val:= range s{
        if _, exsists := string_map[val]; exsists{
            string_map[val] += 1
        }else{
            string_map[val] = 1
        }
    }
    for idx, val := range s{
        if string_map[val] == 1{
            return idx
        }
    }
    return -1
}
