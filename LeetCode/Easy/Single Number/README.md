# 문제 설명
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.
# 파이썬 풀이 결과

비트연산을 이용하여 풀이하였습니다. A^B^C^A^C = A^A^C^C^B = 0^0^B = B
