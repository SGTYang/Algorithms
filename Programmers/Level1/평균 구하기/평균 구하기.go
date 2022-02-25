func solution(arr []int) float64 {
    sum:= 0
    length:= len(arr)
    for i:=0; i<length; i++{
        sum += arr[i]
    }
    return float64(sum)/float64(length)
}
