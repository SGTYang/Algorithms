import "math"

func minimumEffortPath(heights [][]int) int {
    
    m, n := len(heights), len(heights[0])
    distance := map[[2]int]float64{}
    
    for row := 0; row < m; row++ {
        for col := 0; col < n; col++ {
            distance[[2]int{row, col}] = math.Inf(1)
        }
    }
    distance[[2]int{0, 0}] = 0
    
    queue := [][2]int{{0, 0}}
    for len(queue) > 0 {
        pair := queue[0]
        x, y := pair[0], pair[1]
        queue = queue[1:]
        currCost := distance[[2]int{x, y}]
        
        for _, dir := range [4][2]int{{1, 0}, {0, 1}, {-1, 0}, {0, -1}} {
            newX, newY := x + dir[0], y + dir[1]
            
            if newX >= 0 && newY >= 0 && newX < m && newY < n {
                dist := math.Abs(float64(heights[x][y] - heights[newX][newY]))
                newCost := math.Max(float64(currCost), dist)
				
                if newCost < distance[[2]int{newX, newY}] {
                    distance[[2]int{newX, newY}] = newCost
                    queue = append(queue, [2]int{newX, newY})
                }
            }
        }
    }
	
    res := distance[[2]int{m-1, n-1}]
    if res != math.Inf(1) {
        return int(res)
    }
    return 0
}
