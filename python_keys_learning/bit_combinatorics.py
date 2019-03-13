
def count_zero(length, integer):
    b_format = "0{}b".format(length)
    return format(integer, b_format).count("0")

def get_combination(size):
    return pow(2, int(size))

def superBitstrings(n, bit_strings):
    max_comb = 0
    for single in bit_strings:
        zeros = count_zero(n, single)
        comb = get_combination(zeros)
        max_comb = max(comb, max_comb)
    return max_comb

print(superBitstrings(5, [10,26]))
