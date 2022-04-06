func threeSumMulti(arr []int, target int) int {
    ans := 0
    var doCheck func(index, num int, visited *[]bool)
    doCheck = func(index, num int, visited *[]bool) {
        if &visited[index] || arr[index] != num{
                return
            }
        fmt.Println("index: ", index, "visited: " ,visited)
        ans ++
        visited[index] = true
        doCheck(index-1,num, *visited)
        doCheck(index+1,num, *visited)
    }
    
    left, right := 0, len(arr)-1
    
    for left<right{
        find := target-(arr[left]+arr[right])
        
        mid_left, mid_right := left, right
        
        for mid_left<mid_right{
            mid := (mid_left+mid_right)/2
            fmt.Println(mid_left, mid_right, mid)
            if arr[mid] == find{
                visited := make([]bool,len(arr))
                doCheck(mid, arr[mid], &visited)
            }else if arr[mid] < find{
                mid_left = mid+1
            }else{
                mid_right = mid-1
            }
        }
        left++
        right--
    }
    return ans
}
