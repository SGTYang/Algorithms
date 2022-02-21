
func solution(arr1 [][]int, arr2 [][]int) [][]int {
    row := len(arr1)
    col := len(arr1[0])
    ans := make([][]int, row)
    
    for i := range result {
        ans[i] = make([]int, col)
    }
    
    for i := 0; i < row; i++ {
        for j := 0; j < col; j++ {
            ans[i][j] = arr1[i][j] + arr2[i][j]
        }
    }

    return ans
}
