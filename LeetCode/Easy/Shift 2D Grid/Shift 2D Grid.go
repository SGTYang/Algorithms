func shiftGrid(grid [][]int, k int) [][]int {
    k = k%(len(grid)*len(grid[0]))
    
    linear := make([]int,0)
    for _, row := range grid{
        for _, v := range row{
            linear = append(linear,v)
        }
    }
    linear = append(linear[len(linear)-k:], linear[:len(linear)-k]...)
    
    linear_index := 0
    
    for i, _ := range grid{
        for j, _ := range grid[i]{
            grid[i][j] = linear[linear_index]
            linear_index ++
        }
    }
    return grid
}
