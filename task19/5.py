def print_ls(ls):
    if not ls:
        return
    print(ls[0])
    print_ls(ls[1:])

print_ls(ls = [1, 2, 3])