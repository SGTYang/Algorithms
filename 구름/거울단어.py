# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
n = int(input())

mirror_set = {"b":"d","d":"b","i":"i","l":"l","m":"m","n":"n","o":"o","p":"q","q":"p","s":"z","z":"s","u":"u","v":"v","w":"w","x":"x"}
def mirror_check(n):
	if len(n) == 1 and n[0] not in mirror_set:
		return False
	if len(n) == 1 and (n[0] == "b" or n[0] == "d" or n[0] == 'p'  or n[0] == 'q' or n[0]== 's' or n[0] =='z'):	
		return False
	for i in range(len(n)//2):
		if n[i] not in mirror_set or mirror_set[n[i]] != n[-(i+1)]:
			return False
		
	return True
		
	
for _ in range(n):
	if mirror_check(input()):
		print("Mirror")
	else:
		print("Normal")
	
		
