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

# 6.-Inclusive List Ranges
# Write a function that, given the start start_num and end end_num values,
# return a list containing all the numbers inclusive to that range. 
inclusive_list = lambda n1,n2:[i for i in range(n1,n2+1)] if n1<n2 else n1
# print(inclusive_list(1, 5))
# print(inclusive_list(2, 8))
# print(inclusive_list(10, 20))
# print(inclusive_list(17, 5))
# FUENTE:https://edabit.com/challenge/bHTb8p5nybCrjFPze

# 7.- Example
def ordenAsc (lst):
    l = []
    min = lst[len(lst)-1]
    for el in lst:      
        if min<el:
            l.append(min)
        else:
            min = el  
            l.append(min)
    return(l)  

# print(ordenAsc([1,4,3,2,5]))

# 8.-Let's Sort This List!
# Resource = https://edabit.com/challenge/NM8JbG5K2ajKjkqpj
# Create a function that takes a list of numbers lst, a string s and return
# a list of numbers as per the following rules:
# "Asc" returns a sorted list in ascending order.
# "Des" returns a sorted list in descending order.
# "None" returns a list without any modification.

def asc_des_none(lst:list, s:str) ->list:
    """Function that orders a list of numbers
    in ascending or descending order, acording
    with the text that is received as a second
    partamter 

    Args:
        lst (list): list to be ordered
        s (str): text that defines if the list is goin to be
        ordered in ascending or descending way

    Returns:
        list: list oredered
    """
    if s == 'Asc':
        lst = sorted(lst)
    elif s == 'Des':
        lst = sorted(lst, reverse=True)
    return lst

# print(asc_des_none([4, 3, 2, 1], "Asc" ))
# print(asc_des_none([7, 8, 11, 66], "Des"))
# print(asc_des_none([1, 2, 3, 4], "None"))
# print(asc_des_none([1, 0, 1, 0], "Asc"))
# print(asc_des_none([1, 2, 2, 2, 2, 2, 2], "Des"))
# print(asc_des_none([9, 7, 43, 11, 16, 111, 19], "Asc"))

# Extra code that surged from the example number 8
# here i leraned the concept of namedtuple, that it's like
# a type of a class, but more simple:
from collections import namedtuple

Runner = namedtuple('Runner', 'bibnumber duration')
runners = []
runners.append(Runner('2528567', 1500))
runners.append(Runner('7575234', 1420))
runners.append(Runner('2666234', 1600))
# print(Runner('2528567', 1500))
# print(':::::runners:', runners)

# Now i'm going to experiment with the concept of
# slices in lists, also as a consequence of the
# documentation that i  saw in example number 8:

list_example = [1,2,3,4,5,6,7,8,9,10]
# print(list_example[-1:-10:-2])

# 9.-Date Format
# Create a function that converts a date formatted as MM/DD/YYYY
# to YYYYDDMM
def format_date(date:str) -> str:
    """function that receives a date as 
    a string in the format MM/DD/YYYY, and returns 
    the date as a string in the format:  YYYYDDMM.

    Args:
        date (_type_): date as a string in the format MM/DD/YYYY
    """
    # convert a string to a list:
    a = date.rsplit("/")
    #revert the order of the list
    a.reverse()
    #join without space the elements of the list
    return "".join(a)
    
print(format_date("11/12/2019"))
# format_date("12/31/2019")
# format_date("01/15/2019")



