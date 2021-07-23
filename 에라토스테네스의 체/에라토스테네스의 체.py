def finding_prime(n):
    num_set = set(2:range(n)+1)
    if i in num_set:
        num_set -= set(range(i*2,n+1,i))
