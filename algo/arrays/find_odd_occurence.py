def find_odd_occurences(arr):
    result = 0
    for elem in arr:
        result = result ^ elem

    return result

a = [5,2,3,3,4,5,2,2,4]
print(find_odd_occurences(a))


