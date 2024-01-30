def get_sum(seq, n):
    return n * ((seq - 1) // n) * ((seq - 1) // n + 1) // 2


l = 100000000
print(get_sum(l, 3) + get_sum(l, 5) - get_sum(l, 15))
