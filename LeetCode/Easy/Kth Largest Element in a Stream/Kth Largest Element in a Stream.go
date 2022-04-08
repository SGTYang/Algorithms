import "container/heap"

type IntHeap []int

func (h IntHeap) Less (i,j int) bool{
    return h[i] < h[j]
}
func (h IntHeap) Swap (i,j int){
    h[i], h[j] = h[j], h[i]
}
func (h IntHeap) Len() int{
    return len(h)
}
func (h *IntHeap) Push (x interface{}) {
    *h = append(*h, x.(int))
}
func (h *IntHeap) Pop() interface{} {
    x := (*h)[len(*h)-1]
    *h = (*h)[:len(*h)-1]
    return x
}


type KthLargest struct {
    h *IntHeap
    k int
}


func Constructor(k int, nums []int) KthLargest {
    var ins KthLargest
    if len(nums) <= k {
        ins = KthLargest{h: (*IntHeap)(&nums), k: k}
        heap.Init(ins.h)
    }else{
        kNums := nums[:k]
        ins = KthLargest{h: (*IntHeap)(&kNums), k: k}
        heap.Init(ins.h)
        for i:=k; i<len(nums); i++{
            ins.Add(nums[i])
        }
    }
    return ins
    
}


func (this *KthLargest) Add(val int) int {
    if this.h.Len() < this.k{
        heap.Push(this.h, val)
    }else if val > (*this.h)[0]{
        (*this.h)[0] = val
        heap.Fix(this.h, 0)
    }
    return (*this.h)[0]
}


/**
 * Your KthLargest object will be instantiated and called as such:
 * obj := Constructor(k, nums);
 * param_1 := obj.Add(val);
 */
