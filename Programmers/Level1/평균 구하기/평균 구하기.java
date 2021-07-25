class Solution {
    public double solution(int[] arr) {
        double answer = 0;
        int sum=0;
        for(int i=0; i<arr.length;i++){
            sum+=arr[i];
        }
        answer = sum*(1.0)/arr.length;
        return answer;
    }
}
