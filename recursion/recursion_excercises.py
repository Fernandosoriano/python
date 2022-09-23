### 1.-Find the Highest Integer in the List Using Recursion
# Create a function that finds the highest integer in the list using recursion.
def find_highest(lst):
    if len (lst) == 1:
        return lst[0]
    else:
        max = find_highest(lst[1:])
        print(max)
        return max if max > lst[0] else lst[0]
# find_highest = lambda lst:

# print(find_highest([-1, 3, 5, 6, 99, 12, 2]))
factorial = lambda n: 1 if n == 1 else 1 if n == 0 else n * factorial(n-1)
print(factorial(5))

