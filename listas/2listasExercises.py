### 1.-Even Number Generator
# Using list comprehensions, create a function that finds all even
# numbers from 1 to the given number.
find_even_nums = lambda num: [e for e in range (1,num+1) if e %2 == 0]
# FUENTE: https://edabit.com/challenge/eJLwXpuaffjFnzENN
# print(find_even_nums(8))
# print(find_even_nums(4))
# print(find_even_nums(2))