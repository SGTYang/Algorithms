func maxArea(height []int) int {
    left, right := 0, len(height)-1
    maxContainer := 0
    tmpContainer := 0
    for left < right{
        if height[right] > height[left]{
            tmpContainer = height[left]*(right-left)
            left ++
        }else{
            tmpContainer = height[right]*(right-left)
            right --
        }
        maxContainer = Max(maxContainer, tmpContainer)
    }
    return maxContainer
}

func Max (a, b int) int{
    if a>=b{
        return a
    }
    return b
}
