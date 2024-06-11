# 1.-Imaginary Coding Interview
# Create a function to check if a candidate is qualified in an imaginary
# coding interview of an imaginary tech startup.

# The criteria for a candidate to be qualified in the coding interview is:

# The candidate should have complete all the questions.
# The maximum time given to complete the interview is 120 minutes.
# The maximum time given for very easy questions is 5 minutes each.
# The maximum time given for easy questions is 10 minutes each.
# The maximum time given for medium questions is 15 minutes each.
# The maximum time given for hard questions is 20 minutes each.
def interview(lst:list, tot:int) -> str:
    """Function that receives a list, in which each element
    indicate th time that the candidate did for question, and if this
    time is the correct and also the total time, the candidate is 
    cualified, in another case, not

    Args:
        lst (_type_): List with the time that the candidate made per question
        tot (_type_): Total time that the candidate did during the test

    Returns:
        _type_: A string that indicates if the candidate is qualified or not
    """
    list_of_times = [5,5,10,10,15,15,20,20]
    l = [True for i, j in zip(lst, list_of_times) if i <= j]
    if len (lst) == 8 and len (l) == 8 and tot <= 120:
            return 'qualified'
    else:
        return 'disqualified'

# print(interview([5, 5, 10, 10, 15, 15, 20, 20], 120))
# print(interview([2, 3, 8, 6, 5, 12, 10, 18], 64))
# print(interview([5, 5, 10, 10, 25, 15, 20, 20], 120))
# print(interview([5, 5, 10, 10, 15, 15, 20], 120))
# print(interview([5, 5, 10, 10, 15, 15, 20, 20], 130))


#2.-Disarium Number
# A number is said to be Disarium if the sum of its digits raised
# to their respective positions is the number itself.

# Create a function that determines whether a number is a Disarium or not. 
# LINK = https://edabit.com/challenge/yvJbdkmKHvCNtcZy9

def is_disarium(n:int) -> bool:
    """Function that receives a number, and
    returns True if the number is a Disarium, in other case
    returns False

    Args:
        n (int): Number to check if is disarium

    Returns:
        bool: True if the number is disarium, False if not
    """
    list_of_nums:list = [int(num) for num in str(n)]
    return True if sum([i**(list_of_nums.index(i)+1) for i in list_of_nums]) == n \
    else False
# Tests:
# print(is_disarium(75))
# print(is_disarium(135))
# print(is_disarium(544))
# print(is_disarium(518))
# print(is_disarium(466))
# print(is_disarium(8))


# 3.-Combined Consecutive Sequence
def consecutive_combo(lst1:list, lst2:list) -> bool:
    """function that receives two lists
    and returns Trrue if the result of the
    concatenation of the two lists forms a consecutive
    sequence

    Args:
        lst1 (list): list one to be concatenated
        lst2 (list): list two to be concatenated

    Returns:
        bool: True if the resultating list has a consecutive
    sequence
    """
    combined_list:list = lst1+lst2
    return sorted(combined_list) == list(range(min(combined_list),\
        max(combined_list)+1))
# TESTS:
# print(consecutive_combo([1, 4, 5, 6], [2, 3, 7, 8, 10]))
# print(consecutive_combo([1, 4, 5, 6], [2, 7, 8, 9]))
# print(consecutive_combo([1, 4, 5, 6], [2, 3, 7, 8, 10]))


# 4.-Flipping Bits
# You will be given a list of 32-bit unsigned integers. Flip all
# the bits 1 -> 0 and 0 -> 1 and return the result as an unsigned integer.

def flipping_bits(n:int) -> int:
    """Function that receives an integer
    and converts this number to a binary of 32
    length, then this binary is flipped, changing
    0 to 1 and viceverse, and then the int of this
    binary changed is returned

    Args:
        n (int): integer to be changed

    Returns:
        int: integer of the  binary changed of the
        orginal number received
    """
    binary:str = bin(n)[2::]
    binary_filled:str = binary.zfill(32)
    l:list = ['1' if n=='0' else '0' for n in binary_filled]
    not_bin:int = int(''.join(l),2)
    return not_bin

# print(flipping_bits(4))