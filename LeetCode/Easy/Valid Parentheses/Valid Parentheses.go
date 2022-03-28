func isValid(s string) bool {
    
    if len(s) == 0 || len(s)%2 !=0{
        return false
    }
    dict := map[rune]rune{
        '(':')',
        '[':']',
        '{':'}',
    }
    var stack []rune
    
    for _, val := range s{
        if _, exists := dict[val]; exists{
            stack = append(stack, dict[val])
        }else if len(stack) == 0 || stack[len(stack)-1] != val{
            return false
        }else{
        stack = stack[:len(stack)-1]
        }
    }
    if len(stack) !=0{
        return false
    }
    return true
}
