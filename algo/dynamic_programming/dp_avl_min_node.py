def min_avl_node(h):
    if h == 0:
        return 1
    elif h == 1:
        return 2

    return 1+min_avl_node(h-1)+min_avl_node(h-2)

print(min_avl_node(1))
