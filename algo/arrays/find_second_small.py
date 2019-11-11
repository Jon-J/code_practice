def find_second_smallest(arr):
    m1 = m2 = float('inf')
    for elem in arr:
        if elem <= m1:
            m2 = m1
            m1 = elem
        elif elem < m2:
            m2 = elem
    return m2

a = [9,3,4,6,2,5]
print(find_second_smallest(a))

a = [3,2,3,1,4,5]
print(find_second_smallest(a))

