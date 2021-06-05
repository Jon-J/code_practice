# https://www.geeksforgeeks.org/majority-element/
# https://medium.com/swlh/finding-the-majority-element-is-your-solution-efficient-enough-2a6b49a75cb8
# https://afteracademy.com/blog/find-the-majority-element-in-an-array
def find_major_element(list_elem):
    maj_idx = 0
    count = 0
    length = len(list_elem)
    for idx in range(length):
        if list_elem[maj_idx] == list_elem[idx]:
            count += 1
        else:
            count -= 1

        if count <= 0:
            count = 1
            maj_idx = idx
    return list_elem[maj_idx]

def is_major(list_elem, elem):
    count = 0
    for val in list_elem:
        if val == elem:
            count += 1

    if count > len(list_elem)/2:
        return True
    else:
        return False

def check_majority_in_elem(list_elem):
    cand = find_major_element(list_elem)

    if is_major(list_elem, cand):
        print(cand)
    else:
        print("No Majority Elements!!!")

if __name__ == '__main__':
    list_1 = [2,1,4,2,1,2,3,2,2]
    list_2 = [3,2,5,1,4,3,3,3]

    check_majority_in_elem(list_1)
    check_majority_in_elem(list_2)
