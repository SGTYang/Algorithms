import "unicode"

func solution(s string) string {
    str := []rune(s)
    var index int
    for i:=0; i<len(str); i++{
        if unicode.IsSpace(str[i]) {
            index = 0
        }else if index%2==0{
            str[i] = unicode.ToUpper(str[i])
            index += 1
        }else{
            str[i] = unicode.ToLower(str[i])
            index += 1
        }
    }
    return string(str)
}
