func searchMatrix(matrix [][]int, target int) bool {
    
    var check_idx int
    for idx, row := range matrix{
        compare := row[len(matrix[0])-1]
        if compare >= target{
            check_idx = idx
            break
        }
    }
    for _, val := range matrix[check_idx]{
        if val == target{
            return true
        }
    }
    return false
}
