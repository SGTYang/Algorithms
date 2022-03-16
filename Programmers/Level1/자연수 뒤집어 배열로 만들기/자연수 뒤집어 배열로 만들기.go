import (
    "strconv"
)
func solution(n int64) []int {
    answer := []int{}
    str := strconv.Itoa(int(n))
    for i := len(str) - 1; i >= 0; i-- {
        plus, _ := strconv.Atoi(string(str[i]))
        answer = append(answer, plus)
    }
    return answer
}
