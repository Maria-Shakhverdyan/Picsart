def selection_sort(lst):
    for i in range(len(lst)):
        min_index = i

        for j in range(i + 1, len(lst)):
            if lst[j] < lst[min_index]:
                min_index = j

        lst[i], lst[min_index] = lst[min_index], lst[i]
    
    return lst

lst = []
n = int(input("Enter count of elements: "))

for _ in range(n):
    numbers = int(input("Enter the numbers: "))
    lst.append(numbers)

print("Sorted list:", selection_sort(lst))

# Worst-Case, Best-Case, and Average-Case Time Complexity: O(n²)
# The outer loop runs n times, where n is the number of elements in the list.
# For each iteration, the algorithm selects the next smallest (or largest) element. 
# The inner loop finds the minimum (or maximum) element from the unsorted portion of the list.
# In the first iteration, it compares n - 1 elements, in the second iteration it compares n - 2 elements...
# (n - 1) + (n - 2) + (n - 3) +...+ 1 = (n(n - 1))/2 = (n^2 - n)/2, the highest-order term is n²
