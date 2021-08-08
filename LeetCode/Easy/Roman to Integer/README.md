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

1. I can be placed before V (5) and X (10) to make 4 and 9.
2. X can be placed before L (50) and C (100) to make 40 and 90. 
3. C can be placed before D (500) and M (1000) to make 400 and 900.
4. Given a roman numeral, convert it to an integer.

# 파이썬 풀이 결과
<img width="675" alt="스크린샷 2021-08-08 오후 2 22 58" src="https://user-images.githubusercontent.com/42399580/128621821-29e334d1-7d2a-41d8-8f85-8f612503e2c7.png">
Integer to Roman 문제와 다르게 이번에는 딕셔너리를 이용하여 풀이 하였습니다. 
