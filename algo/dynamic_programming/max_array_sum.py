def maxSubsetSum(arr):
    dp = []
    dp.append(arr[0])
    dp.append(max(arr[:2]))
    ans = max(dp)
    for a in arr[2:]:
        dp.append(max(max(dp[-2]+a, a), ans))
        ans = max(ans, dp[-1])
    return ans

l = [3, 7, 4, 6, 5]
l = [2, 1, 5, 8, 4]
l = [3, 5, -7, 8, 10]
print(sum(l))
print(maxSubsetSum(l))
