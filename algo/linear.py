#Implenting linear function....

def linear_function(list_elements, target_element):
    position = 0
    found = False
    len_list = len(list_elements)
    while position < len_list and not found:
        if list_elements[position] == target_element:
            found = True
        position+=1
    return found

if __name__ == '__main__':
    num_list = [1,2,3,4,5,6,7,8]
    target_num = 3
    is_element = linear_function(num_list, target_num)
    if is_element:
        print("Found the number in list")
    else:
        print("Not found the number in list")
