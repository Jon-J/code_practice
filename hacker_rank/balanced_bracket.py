def isBalanced(s):
    opening = tuple('({[')
    closing = tuple(')}]')
    mapping = dict(zip(opening, closing))
    queue = []

    for letter in s:
        if letter in opening:
            queue.append(mapping[letter])
        elif letter in closing:
            if not queue or letter != queue.pop():
                return 'NO'
    if not queue:            
        return 'YES'
    else:
        return 'NO'

if __name__ == '__main__':
    in_str = '({[]})'
    t = isBalanced(in_str)
    print(t)
    in_str = '({]}[)'
    t = isBalanced(in_str)
    print(t)
