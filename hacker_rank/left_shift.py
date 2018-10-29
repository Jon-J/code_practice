def right_shift(seq, n=0):
    a = n % len(seq)
    return seq[-a:] + seq[:-a]

def left_shift(seq, n=0):
    a = n % len(seq)
    print(a)
    return seq[a:] + seq[:a]

if  __name__ == '__main__':
    result = left_shift([1,2,3,4,5], 4)
    print(*result, sep=' ')
    print(*result)
