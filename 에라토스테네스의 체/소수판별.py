def is_prime_number(x):
        if x == 1:
            return False
        for i in range(2, int(math.sqrt(x))+1):
            if x % i == 0:
                return False 
        return True 
