func isAnagram(s string, t string) bool {
    t_map := make(map[rune]int)
    
    if len(s) != len(t){
        return false
    }
    
    for _, val := range t{
        if _, exsists := t_map[val]; exsists{
            t_map[val] += 1
        }else{
            t_map[val] = 1
        }
    }
    for _, val := range s{
        if _, exsists := t_map[val]; exsists{
            if t_map[val]==0{
                return false
            }
            t_map[val] -= 1
        }else{
            return false
        }
    }
    return true
}
