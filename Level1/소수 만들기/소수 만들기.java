import java.util.*;
class Solution {
    ArrayList<Integer> list = new ArrayList<Integer>();
    public int solution(int[] nums) {
        int answer = 0;
        boolean [] visited = new boolean[nums.length];
        combination(nums,visited, 0, 3);
        for(int i=0; i<list.size(); i++){
            if(prime(list.get(i))){
                answer++;
            }
        }
        return answer;
    }
    void combination(int[] arr, boolean[] visited, int start, int r) {
        int sum=0;
        if (r==0){
            for(int i=0; i<arr.length; i++){
                if(visited[i]){
                    sum+=arr[i];
                }
            }
            list.add(sum);
            return;
        }

        for(int i=start; i<arr.length; i++){
            visited[i] = true;
            combination(arr, visited, i+1, r-1);
            visited[i] = false;
        }
        return;
    }
    
    boolean prime(int n){ 
        if(n==0 || n==1){
            return false;
        }
        for(int i=2; i<=(int)Math.sqrt(n); i++){
            if(n%i==0){
                return false;
            }
        }
        return true;
    }
    
}
