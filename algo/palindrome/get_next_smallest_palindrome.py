#https://www.youtube.com/watch?v=1aKjQ6Tvh2w
def inc(left_side):
    list_left = list(left_side)
    last_idx = len(list_left) - 1
    while list_left[last_idx]:
        left_side[last_idx] = '0'
        last_idx -= 1

    list_left[last_idx] = str(int(list_left[last_idx])+1)
    return ''.join(list_left)

def next_smallest_palindrome(input_val):
    size = len(input_val)
    if size % 2:
        center = input_val[size//2]
    else:
        center = ''

    left = input_val[:size//2]
    right = left[::-1]

    pal = left + center + right

    if pal > input_val:
        print(pal)
    else:
        if center < '9':
            center = str(int(center) + 1)
            print(left + center + right)
            return
        else:
            center = '0'

        if input_val == size * '9':
            print('1'+ (size-1)*'0' + '1')
            return
        else:
            left = inc(left)
            right = left[::-1]
            print(left + center + right)
        return

next_smallest_palindrome('999')
next_smallest_palindrome('123')
next_smallest_palindrome('89199')
next_smallest_palindrome('10001')
next_smallest_palindrome('11001')

