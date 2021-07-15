import java.util.*;
class Solution {
    public long solution(int n, int[] times){
        Arrays.sort(times);
        int timeLength=times.length;
        long left = 1;
        long right = (long)times[timeLength-1]*n;
        long answer=right;
        while(left<=right){
            long mid =(left+right)/2;
            long count=0;
            for(int i=0; i<timeLength; i++){
                count+=mid/times[i];
            }
            if(count<n){
                left=mid+1;
            }
            else {
                if(mid<answer) {
                    answer = mid;
                }
            right=mid-1;
            }
        }
        return answer;
    }
}
