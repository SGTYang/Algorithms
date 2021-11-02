def solution(n, t, m, p):
    answer = ''
    numb_string = '0123456789ABCDEF'
    conv_sum = ''
    index_numb = 0
    def conversion(numb, notation):
        numb, rest = divmod(numb, notation)
        if numb == 0:
            return numb_string[rest]
        else:
            return conversion(numb, notation) + numb_string[rest]
    
    while index_numb < t*m:
        conv_sum += conversion(index_numb,n)
        index_numb += 1
            
    return conv_sum[p-1::m][:t]
