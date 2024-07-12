def countup(n):
    if n < 0:
        print("The number must be natural.")
    else:
        def helper(num):
            if num <= n:
                print(num)
                helper(num + 1)
                
        helper(0)

n = int(input("Enter the number: "))
countup(n)
