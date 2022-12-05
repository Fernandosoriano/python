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

### 3.-Filter out Strings from an Array
# Create a function that takes a list of non-negative integers and strings and
# return a new list without the strings.
filter_list = lambda lst: [i for i in lst if isinstance(i,int)]
# print(filter_list(["w", "r", "u", 43, "s", "a", 76, "d", 88]))


### 4.-Add the Index
# Given a list of numbers, create a function which returns the list but
# with each element's index in the list added to itself. This means you add
# 0 to the number at index 0, add 1 to the number at index 1, etc...
# FUENTE: https://edabit.com/challenge/gr4ihixfTaoEmZiin
add_indexes = lambda lst: [value + index for index, value in enumerate(lst)]
# print(add_indexes([5, 4, 3, 2, 1]))

### 5.-Unpacking Lists
# Your task is to unpack the list writeyourcodehere into three variables,
# being first, middle, and last, with middle being everything in between the
# first and last element. Then print all three variables.
# Notes
# Your solution should be just one line of code.
# If your solution is longer than one line of code, please review the Resources tab.
# FUENTE: https://edabit.com/challenge/7sdNcax4GsLSrNQbM
first, *middle, last = [1, 2, 3, 4, 5, 6]
# print(first, middle, last)