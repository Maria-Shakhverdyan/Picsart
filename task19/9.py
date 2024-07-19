def new_line(st):
    if not st:
        return
    print(st[0])
    new_line(st[1:])
    
new_line("hello")