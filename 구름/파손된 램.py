import math
# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
rams = int(input())
memory = list(map(int, input().split()))

dest = 0
ans = ""
for i in range(len(memory)):
	if memory[i] & (memory[i]-1):
		dest += 1
		ans += str(i+1)+" "
print(dest)
print(ans)
