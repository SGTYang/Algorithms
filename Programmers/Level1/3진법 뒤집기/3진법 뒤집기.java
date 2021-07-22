class Solution {
    public int solution(int n) {
        int answer = 0;
        int num=3;
        String string ="";
        int a=0;
        
        while(n!=0){
            string=(n%3)+string;
            n=n/3;
        }
        
        for(int i=0; i<string.length(); i++){
            if(string.charAt(i)=='1'){
                answer+=pow(3, i)*1;
            }else if(string.charAt(i)=='2'){
                answer+=pow(3, i)*2;
                }
        }
        return answer;
    }
    
    public int pow(int a, int b) {
		if(b == 0){
            return 1;
        }
		if(b == 1){
            return a;
        }
        
		int temp = pow(a, b/2);
		
		if(b % 2 == 0) {
			return (temp * temp);
		} else {
			return ((temp * temp) * a);
		}
	}
}
