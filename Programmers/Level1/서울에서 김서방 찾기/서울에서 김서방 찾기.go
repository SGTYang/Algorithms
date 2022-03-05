import "fmt"
func solution(seoul []string) string {
    length:= len(seoul)
    var i int
    for i=0; i<length; i++{
        if seoul[i] == "Kim"{
            break
        }
    }
    
    return fmt.Sprintf("김서방은 %d에 있다", i)
}
