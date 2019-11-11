def solution(A, B):
    if not isinstance(A, int) or not isinstance(B, int):
        return -1

    A = str(A) 
    B = str(B) 
    len_a = len(A) 
    len_b = len(B) 

    if len_a > len_b:
        return -1
    print(A, B)
    pref_suf_arr = [0]*len_a 
    index_a = 0 # index for A[] 

    process_pre_suf_arr(A, len_a, pref_suf_arr) 
    print(pref_suf_arr)
    index = 0 
    found = False 
    while index < len_b and found is False: 
        if A[index_a] == B[index]: 
            index += 1
            index_a += 1

        if index_a == len_a: 
            index_a = pref_suf_arr[index_a-1] 
            found = True
            break

        elif index < len_b and A[index_a] != B[index]: 
            if index_a != 0: 
                index_a = pref_suf_arr[index_a-1] 
            else: 
                index += 1
    if found:
        return index-index_a
    else:
        return -1

def process_pre_suf_arr(A, len_a, pref_suf_arr): 
    lenght = 0 

    pref_suf_arr[0] 
    index = 1

    while index < len_a: 
        if A[index]== A[lenght]: 
            lenght += 1
            pref_suf_arr[index] = lenght
            index += 1
        else: 
            if lenght != 0: 
                lenght = pref_suf_arr[lenght-1] 

            else: 
                pref_suf_arr[index] = 0
                index += 1

B = 1953786 
A = 53
print(solution(A, B))

