func check (s string, left, right int) bool{
        for left < right{
            if s[left] != s[right]{
                return false
            }
            left ++
            right --
        }
        return true
    }

func validPalindrome(s string) bool {
    left, right := 0, len(s)-1
    
    for left < right{
        if s[left] != s[right]{
            return check(s, left+1, right) || check(s, left, right-1)
        }
        left++
        right--
    }
    return true
}
