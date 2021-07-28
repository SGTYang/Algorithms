import java.util.*;
class Solution {
  public String solution(int n) {
      StringBuilder compressed = new StringBuilder();
      
      String[] numbers = {"4", "1", "2"};
      while(n > 0){
          int rem = n % 3;
          n /= 3;
          if(rem == 0) n--;
          compressed.insert(0,numbers[rem]);
      }
      return compressed.toString();
  }
}
