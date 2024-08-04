def bar(n):
    func_list = []

    for i in range(n):
        def make_mul(index):
            def mul(x):
                return x * index
            return mul
        func_list.append(make_mul(i))
    
    return func_list

functions = bar(5)

for i, func in enumerate(functions):
    print(f"Function {i} applied to 2: {func(2)}")
    print(f"Function {i} closure variables: ", [cell.cell_contents for cell in func.__closure__])