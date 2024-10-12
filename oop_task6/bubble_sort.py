def bubble_sot(lst):
    for i in range(len(lst)):
        swapped = False

        for j in range(0, len(lst) - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                swapped = True
        if not swapped:
            break
        
    return lst

lst = []
n = int(input("Enter count of elements: "))

for _ in range(n):
    numbers = int(input("Enter the numbers: "))
    lst.append(numbers)

print("Sorted list:", bubble_sot(lst))

# Worst Case: O(n^2)
# Best Case: O(n)
# Average Case: O(n^2)

# The outer loop runs n times, where n is the number of elements in the list.
# This loop controls how many passes through the list the algorithm performs. 
# The inner loop performs comparisons between adjacent elements and performs swaps if necessary. On the first iteration,
# it compares n-1 pairs, on the second iteration, n-2 pairs....
# (n - 1) + (n - 2) + (n - 3) +...+ 1 = (n(n - 1))/2 = (n^2 - n)/2, the highest-order term is n²

# We have O(n), when our array is already sorted. Outer loop runs n time, swapped flag remains False,
# indicating that no swaps were made.