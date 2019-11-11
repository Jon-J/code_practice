def remove_adj_duplicates(string):
    res = []
    index = 0 
    while index < len(string):
        if not res:
            res.append(string[index])
        else:
            if string[index] == res[-1]:
                res.pop()
            else:
                res.append(string[index])
        index += 1

    print(''.join(res))

a = 'careermonk'
remove_adj_duplicates(a)

a = 'mississippi'
remove_adj_duplicates(a)
