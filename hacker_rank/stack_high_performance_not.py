from collections import deque

index = int(input())
stack_list = deque() 
max_val = 0
previous_max_val = 0
for _ in range(index):
    a = [int(x) for x in input().split()]
    if a[0] == 1:
        stack_list.append(a[1])
    elif a[0] == 2:
        stack_list.pop()
    elif a[0] == 3:
        print(max(stack_list))
