func matrixReshape(mat [][]int, r int, c int) [][]int {
    ans := [][]int{}
    cnt := 0
    if len(mat)*len(mat[0])!=r*c{
        return mat
    }
    for _, row := range mat{
        for _, val := range row{
            
            if cnt%c == 0{
                ans = append(ans, []int{val})
            }else{
                ans[cnt/c] = append(ans[cnt/c], val)
            }
            cnt ++
        }
    }
    return ans
}
