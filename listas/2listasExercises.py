### 1.-Even Number Generator
# Using list comprehensions, create a function that finds all even
# numbers from 1 to the given number.
find_even_nums = lambda num: [e for e in range (1,num+1) if e %2 == 0]
# FUENTE: https://edabit.com/challenge/eJLwXpuaffjFnzENN
# print(find_even_nums(8))
# print(find_even_nums(4))
# print(find_even_nums(2))

### 2.-Moving to the End
# Write a function that moves all elements of one type to the end of the list.

move_to_end = lambda lst, el: [l for l in lst if l !=el]+[l for l in lst if l == el]
# print(move_to_end([1, 3, 2, 4, 4, 1], 1))
# print(move_to_end([7, 8, 9, 1, 2, 3, 4], 9))
# print(move_to_end(["a", "a", "a", "b"], "a"))

