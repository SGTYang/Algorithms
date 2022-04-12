func gameOfLife(board [][]int)  {
    for i:=0; i<len(board); i++{
        for j:=0; j<len(board[0]); j++{
            if l:=check(board,i,j); (board[i][j] & 1 == 1 && l == 2) || l == 3 {
                board[i][j] |= 2
            }
        }
    }
    
    for i:=0; i<len(board); i++{
        for j:=0; j<len(board[0]); j++{
            fmt.Print(board[i][j], " ")
            board[i][j] >>= 1
        }
        fmt.Println("")
    }
}

func check(board [][]int, i,j int ) int {
    live := 0
	neighbors := [][2]int{
		[2]int{i - 1, j - 1},
		[2]int{i - 1, j},
		[2]int{i - 1, j + 1},
		[2]int{i, j - 1},
		[2]int{i, j + 1},
		[2]int{i + 1, j - 1},
		[2]int{i + 1, j},
		[2]int{i + 1, j + 1},
	}
    for _, v := range neighbors{
        if x, y := v[0], v[1]; x>=0 && y>=0 && x < len(board) && y < len(board[0]) && board[x][y] & 1 == 1 {
            live ++
        }
    }
        return live
}
