import "fmt"

func solution(x int, n int) []int64 {
    fmt.Println(x)
    var result []int64
	var sum int64
	for idx := 0; idx < n; idx++ {
        sum += int64(x)
		result = append(result, sum)
	}
    
    return result
}
