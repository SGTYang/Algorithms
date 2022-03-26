func canConstruct(ransomNote string, magazine string) bool {
    magazine_map:=make(map[rune]int)
    
    for _, val:=range magazine{
        if _, exsists:=magazine_map[val]; exsists{
            magazine_map[val] += 1
        }else{
            magazine_map[val] = 1
        }
    }
    for _, val:=range ransomNote{
        if _, exsists:=magazine_map[val]; exsists{
            if magazine_map[val] == 0{
                return false
            }
            magazine_map[val] -= 1
        }else{
            return false
        }
    }
    return true
}
