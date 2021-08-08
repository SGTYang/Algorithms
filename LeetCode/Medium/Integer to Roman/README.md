# 문제 설명

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

|Symbol|Value|
|:--|--:|
|I|1|
|V|5|
|X|10|
|L|50|
|C|100|
|D|500|
|M|1000|

For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9.<br/>
X can be placed before L (50) and C (100) to make 40 and 90.<br/>
C can be placed before D (500) and M (1000) to make 400 and 900.<br/>
Given an integer, convert it to a roman numeral.<br/>

# 파이썬 풀이 결과
<img width="647" alt="스크린샷 2021-08-08 오후 2 05 13" src="https://user-images.githubusercontent.com/42399580/128621502-6635c9e4-11d9-4a2b-84cd-917de9a9ed01.png">
시간이 많이 걸리긴 하지만 재귀로 풀어봤습니다. 딕셔너리를 이용할 경우 더 빠른 풀이가 가능할 것 같습니다
