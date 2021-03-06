# 문제 설명
n개의 음이 아닌 정수가 있습니다. 이 수를 적절히 더하거나 빼서 타겟 넘버를 만들려고 합니다. 예를 들어 [1, 1, 1, 1, 1]로 숫자 3을 만들려면 다음 다섯 방법을 쓸 수 있습니다.

|-1+1+1+1+1 = 3|
|:---:|
|+1-1+1+1+1 = 3|
|+1+1-1+1+1 = 3|
|+1+1+1-1+1 = 3|
|+1+1+1+1-1 = 3|

사용할 수 있는 숫자가 담긴 배열 numbers, 타겟 넘버 target이 매개변수로 주어질 때 숫자를 적절히 더하고 빼서 타겟 넘버를 만드는 방법의 수를 return 하도록 solution 함수를 작성해주세요.

# 제한사항
주어지는 숫자의 개수는 2개 이상 20개 이하입니다.
각 숫자는 1 이상 50 이하인 자연수입니다.
타겟 넘버는 1 이상 1000 이하인 자연수입니다.

# 자바 풀이 결과
<img width="254" alt="스크린샷 2021-08-01 오후 7 13 06" src="https://user-images.githubusercontent.com/42399580/127767250-ac5409d6-4599-48ec-b41a-15abb2355f18.png">
BFS를 사용하였습니다.
# 파이썬 DFS 풀이 결과
<img width="268" alt="스크린샷 2021-08-01 오후 7 06 35" src="https://user-images.githubusercontent.com/42399580/127767092-34b97781-60e0-43fe-8296-36e96c0ea084.png">

# 파이썬 BFS 풀이 결과
<img width="268" alt="스크린샷 2021-08-01 오후 7 14 21" src="https://user-images.githubusercontent.com/42399580/127767286-e683e827-5174-42f1-b498-2978bf8f5eb1.png">
