# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
user_input = int(input())

full_length = user_input*(user_input+1)//2

full_length=full_length%1000000007
print(full_length*full_length%1000000007)
