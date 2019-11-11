def get_nos_0s_trailing(n):
    count = 0
    i = 5
    while n/i >= 1:
        count += int(n/i)
        i *= 5
    return count

print(get_nos_0s_trailing(5))
print(get_nos_0s_trailing(100))
print(get_nos_0s_trailing(20))
