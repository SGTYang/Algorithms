# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
n = int(input())
arry = [[0 for i in range(n)] for j in range(n)]

y,x = 0,-1
index = 0
first = True
for i in range(n):
	if i%4==1: 
		if first:
			index+=1
			first = False
		else:
			index+=2
	elif i%4==3:
		index+=2
		
	tmp = index
	while tmp<n:
		if i%4==0:
			x+=1
		elif i%4==1:
			y+=1
		elif i%4==2:
			x-=1
		elif i%4==3:
			y-=1
		arry[y][x] = 1
		tmp+=1

for i in range(n):
	tmp = ""
	for j in range(n):
		if arry[i][j] == 1:
			tmp +="# "
		else:
			tmp += "  "
	print(tmp)
