def solution(A, B):
    if not isinstance(A, int) or not isinstance(B, int):
        return -1

    A = str(A) 
    B = str(B) 
    len_a = len(A) 
    len_b = len(B) 

    if len_a > len_b:
        return -1

    pattern_matched_list = [i for i in range(len(B)) if B.startswith(A, i)] 

    if len(pattern_matched_list) > 0:
        return pattern_matched_list[0]
    else:
        return -1

B = 1953786 
A = 86
print(solution(A, B))

