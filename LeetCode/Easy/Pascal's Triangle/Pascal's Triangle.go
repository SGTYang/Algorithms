func generate(numRows int) [][]int {
    ans:=[][]int{}
    for i:=0; i<numRows; i++{
        for j:=0; j<i+1; j++{
            if j==0{
                ans = append(ans, []int{1})
            }else{
                if j==i{
                    ans[i] = append(ans[i], 1)
                }else{
                    ans[i] = append(ans[i], ans[i-1][j]+ans[i-1][j-1])
                }
            }
        }
    }
    return ans
}
