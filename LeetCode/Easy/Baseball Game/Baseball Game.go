func calPoints(ops []string) int {
    container := make([]int,len(ops))
    var ans int
    
    
    for _,v := range ops{
        if v == "C"{
            container = container[:len(container)-1]
        }else if v == "D"{
            container = append(container, container[len(container)-1]*2)
        }else if v == "+"{
            container = append(container, container[len(container)-1]+container[len(container)-2])
        }else{
            num, _ := strconv.Atoi(v)
            container = append(container, num)
        }
    }
    
    
    for _, v:= range container{
        ans += v
    }
    
    return ans
}
