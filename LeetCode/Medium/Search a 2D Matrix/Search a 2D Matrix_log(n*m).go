func searchMatrix(matrix [][]int, target int) bool {
    
    left, right := 0, len(matrix)*len(matrix[0])
    
    for left < right{
        mid := (left+right)/2
        i, j := mid/len(matrix[0]), mid%len(matrix[0])
        
        if matrix[i][j] == target{
            return true
        }else if matrix[i][j] > target{
            right = mid
        }else{
            left = mid +1
        }
    }
    
    return false
}
