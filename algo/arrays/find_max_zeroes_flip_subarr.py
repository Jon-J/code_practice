#https://www.geeksforgeeks.org/maximize-number-0s-flipping-subarray/?source=post_page-----28d67601a66----------------------
def find_max_zeroes(array):
    max_diff = 0
    original_zero = 0

    current_diff = 0
    
    for elem in array:
        if elem == 0:
            original_zero += 1

        value = 1 if elem else -1

        current_diff = max(value, current_diff+value)
        max_diff = max(max_diff, current_diff)

    max_diff = max(0, max_diff)

    return original_zero+max_diff

a = [0,1,0,0,1,1,0]
print(find_max_zeroes(a))

b = [0,0,0,1,0,1]
print(find_max_zeroes(b))

c = [0,0,0,0]
print(find_max_zeroes(c))
d = [1,0,1,1]
print(find_max_zeroes(d))
