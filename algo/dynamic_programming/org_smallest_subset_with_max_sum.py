from itertools import chain, combinations

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)  # allows duplicate elements
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))


stuff = [1, 2, 3]
stuff = [1,6,5,3]
stuff = [4, 2, 5, 1, 6]
from itertools import chain, combinations
max_sum = sum(stuff)
res_sum = 0
res_list = []
for i, combo in enumerate(powerset(stuff), 1):
    print('combo #{}: {}'.format(i, combo))
    curr_sum = sum(combo)
    diff = max_sum - curr_sum
    if curr_sum > diff:
        if (res_sum == 0 or curr_sum > res_sum) and ( len(res_list) == 0 or len(combo) <= len(res_list)):
            res_sum = curr_sum
            res_list = list(combo)
print(res_sum, res_list)


