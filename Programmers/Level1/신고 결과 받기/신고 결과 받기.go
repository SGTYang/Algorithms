import(
    "fmt"
    "strings"
)
func solution(id_list []string, report []string, k int) []int {
    var report_map map[string]string
    var check_map map[string]int
    var ans_map map[string]string
    var ans  map[string]int
    
    ans = make(map[string]int)
    ans_map = make(map[string]string)
    check_map = make(map[string]int)
    report_map = make(map[string]string)
    
    for _,val := range id_list{
        check_map[val]  = 0
    }
    
    for i:=0; i<len(report); i++{
        tmp_string:=strings.Split(report[i], " ")

        if _, exists:=report_map[report[i]]; !exists{
            ans_map[tmp_string[1]] = tmp_string[0]
            report_map[report[i]] = tmp_string[1]
            check_map[tmp_string[1]] += 1
        }
    }
    
    for key,val := range check_map{
        if val >= k{
            ans[ans_map[key]] += 1
        }
    }
    fmt.Println(check_map)
    fmt.Println(ans)

    return []int{}
}
