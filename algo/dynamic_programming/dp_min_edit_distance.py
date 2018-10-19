def min_edit_distance(str1, str2, m, n):
    med = [[0 for x in range(n+1)] for x in range(m+1)]

    for i  in range(m+1):
        for j in  range(n+1):
            if i == 0:
                med[i][j] = j
            elif j == 0:
                med[i][j] = i

            elif str1[i-1] == str2[j-1]:
                med[i][j] = med[i-1][j-1]
            else:
                med[i][j] = 1+ min(med[i-1][j],   #Remove
                                  med[i][j-1],   #Insert
                                  med[i-1][j-1]) #Replace
    return med[m][n]

str1 = "sunday"
str2 = "saturday"

print(min_edit_distance(str1, str2, len(str1), len(str2)))
