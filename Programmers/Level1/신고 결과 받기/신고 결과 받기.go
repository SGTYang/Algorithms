import(
    "strings"
)
func solution(id_list []string, report []string, k int) []int {
    var report_map map[string]string
    var check_map map[string]int
    var ans  map[string]int
    var list []int
    
    ans = make(map[string]int)
    check_map = make(map[string]int)
    report_map = make(map[string]string)
    
    for _,val := range id_list{
        check_map[val]  = 0
    }
    
    for i:=0; i<len(report); i++{
        if _, exists:=report_map[report[i]]; !exists{
            tmp_string:=strings.Split(report[i], " ")
            report_map[report[i]] = tmp_string[1]
            check_map[tmp_string[1]] += 1
        }
    }
    
    for key,_ := range report_map{
        tmp_string:=strings.Split(key, " ")
        if check_map[tmp_string[1]] >= k{
            ans[tmp_string[0]] += 1
        }
    }
    
    for _,val := range id_list{
        list = append(list, ans[val])
    }

    return list
}
