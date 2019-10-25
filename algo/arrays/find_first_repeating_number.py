def first_repeating_number(arr):
    table = dict()
    for elem in arr:
        if elem in table:
            table[elem] += 1
        else:
            table[elem] = 1

    for elem in arr:
        if elem in table and table[elem] > 1:
            return elem
    return -1

arr = [1,2,3,4,4,3,5]
print(first_repeating_number(arr))

arr = [4,2,1,2,2,4]
print(first_repeating_number(arr))
