import ("fmt")
func solution(phone_number string) string {
    number:= []rune(phone_number)
    fmt.Print(number)
    length:= len(phone_number)
    
    for i:=0; i<length-4; i++{
        number[i] = '*'
    }
    return string(number)
}
