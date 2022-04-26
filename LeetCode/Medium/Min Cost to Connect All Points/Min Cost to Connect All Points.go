func minCostConnectPoints(points [][]int) int {
    nPoint := len(points)
    if nPoint < 2 {
        return 0
    }
    
    total := 0
    dists := make([]int, nPoint)
    
    // start explore from points[0]
    curPoint := 0
    for curPoint >= 0 {
        dists[curPoint] = -1 // mark as visted
        nextPoint := -1
        minEdge := -1
        // fmt.Println(curPoint, dists)
        for i, _ := range points {
            // fmt.Println(i, dists[i])
            if dists[i] >= 0 {
                d := getManhattenDistance(
                    points[curPoint][0],
                    points[curPoint][1],
                    points[i][0],
                    points[i][1],
                )
                if dists[i] == 0 || dists[i] > d {
                    dists[i] = d
                }
                if minEdge == -1 || minEdge > dists[i] {
                    minEdge = dists[i]
                    nextPoint = i
                } 
            }
        }
        // fmt.Println("min", minEdge)
        if minEdge != -1 {
            total += minEdge
        }
        curPoint = nextPoint
    }
    
    return total
}

func abs(n int) int {
    if n < 0 {
        return -n
    }
    
    return n
}

func getManhattenDistance(x1, y1, x2, y2 int) int {
    return abs(x1 - x2) + abs(y1 - y2)
}
