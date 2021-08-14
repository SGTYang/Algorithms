import java.util.*;
class Solution {
    public boolean solution(String[] phone_book) {
        boolean answer = true;
       HashMap<String, String> hm = new HashMap<>();
		
		// 중복을 제거해서 해시 맵에 모두 저장
		for( String input : phone_book ) {
			hm.put(input, input);
		}
		for ( String target : phone_book) {
			for( int i=0; i< target.length(); i++) {
				if( hm.containsKey(target.substring(0,i)) ) {
					return false;
				}
			}
		}
        return answer;
    }
}
