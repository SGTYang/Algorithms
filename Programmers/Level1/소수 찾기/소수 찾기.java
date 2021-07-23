import java.util.*;
class Solution {
    public int solution(int n) {
		ArrayList<Integer> list = new ArrayList<Integer>();
		
		int answer = 0;
		if(n==2){
           return answer+1;
        }else if(n<5){
            return answer+2;
        }else if(n<7){
            return answer+3;
        }else if(n<11){
            return answer+4;
        }else{
            for(int i=2; i<=n; i++) {
                
			    if(i % 2 == 0){
                    continue;
                }
			    else if(i % 3 == 0){
                    continue;
                }
			    else if(i % 5 == 0){
                    continue;
                }
			    else if(i % 7 == 0){
                    continue;
                }
                
			    int a=0;
			    if(i >= 121) {
				    for(int j=0; j<list.size(); j++) {
					    if(i < list.get(j)*list.get(j)){
                            break;
                        }
					    if(i%list.get(j) == 0) {
						    a = 1;
						    break;
					    }
				    }
			    }
			    if(a==1){
                    continue;
                }
                    answer++;
                    list.add(i);
                }
		    return answer+4;
            }
        }
    }
