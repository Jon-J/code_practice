#https://realpython.com/python-itertools/

### ZIP & UNZIP:
def better_grouper(inputs, n):
    iters = [iter(inputs)] * n
    for i in iters:
        print(i)
    print(iters)
    return zip(*iters)
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(better_grouper(nums, 2)))


### MAP with ZIP

print(list(map(sum, zip([1, 2, 3], [4, 5, 6]))))
