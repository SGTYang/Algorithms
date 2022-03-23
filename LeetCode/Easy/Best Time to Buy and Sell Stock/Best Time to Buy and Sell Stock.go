
func Max(num1, num2 int) int{
    if num1 > num2{
        return num1
    }else{
        return num2
    }
}

func maxProfit(prices []int) int {
    hold, maxNum := prices[0], math.MinInt64
    
    for _, val := range prices{
        if val - hold < 0 {
            hold = val
        }else{
            maxNum = Max(val-hold, maxNum)
        }
    }
    return maxNum
}
