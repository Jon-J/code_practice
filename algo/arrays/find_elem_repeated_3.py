def find_elem_repeated_3(arr):
    res = 0
    for elem in arr:
        res = res ^ elem

    return res

a = [1,1,2,2,3,3,4,4,3,3,5,5,6,6,4,4,7,7,5,5,6,6,8,8,7,7,9,9,7,7,3]
print(find_elem_repeated_3(a))
