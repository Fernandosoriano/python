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


# 5.-Tallest Skyscraper
# A city skyline can be represented as a 2-D list with 1s representing
# buildings. In the example below, the height of the tallest building
# is 4 (second-most right column).
# [[0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 1, 0],
# [0, 0, 1, 0, 1, 0],
# [0, 1, 1, 1, 1, 0],
# [1, 1, 1, 1, 1, 1]]
# Create a function that takes a skyline (2-D list of 0's and 1's)
# and returns the height of the tallest skyscraper.
# Link = https://edabit.com/challenge/76ibd8jZxvhAwDskb

def tallest_skyscraper(lst:list) -> int:
    """function that receives a lis of lists (matrix)
    and returns the max number resulted from the 
    sum of the n'th coolumn of the matrix

    Args:
        lst (list): list of lists

    Returns:
        int: max number, result of the sum of the n'th
        column of the list of lists (matrix)
    """
    suma:list = [sum(x) for x in zip(*lst)]
    return max(suma)
# TESTS:
# print(tallest_skyscraper([
# [0, 0, 0, 0],
# [0, 1, 0, 0],
# [0, 1, 1, 0],
# [1, 1, 1, 1]
# ]))
# print(tallest_skyscraper([
#   [0, 1, 0, 0],
#   [0, 1, 0, 0],
#   [0, 1, 1, 0],
#   [1, 1, 1, 1]
# ]))
# print(tallest_skyscraper([
#   [0, 0, 0, 0],
#   [0, 0, 0, 0],
#   [1, 1, 1, 0],
#   [1, 1, 1, 1]
# ]))


# 6.-Convert to Hex
# Create a function that takes a string's characters as ASCII
# and returns each character's hexadecimal value as a string.
# Link = https://edabit.com/challenge/g6yjSfTpDkX2STnSX

def convert_to_hex(txt:str) -> str:
    """Function that receives a string, then
    this string is converted to a list, in which each
    element is the equivalent of the letter of the original
    string to ASCII, and finally each element of this list is 
    converted to their equivalent in a hexadecimal system,
    returning it as a string

    Args:
        txt (str): string to be converted to a string of a 
        hexadecimal

    Returns:
        str: string with hexadecimal elements
    """
    l:list = [hex(ord(letter))[2::] for letter in txt]
    res = ' '.join(l)
    return res

# Notes:
#1.- ord receives a letter or symbol and returns their equivalent
# ValueErrorin ascii code

#2.- hex receives a decimal number, and returns thier equivalent
# in a hexadecimal system

# TESTS:
# print(convert_to_hex("hello world"))
# print(convert_to_hex("Big Boi"))
# print(convert_to_hex("Marty Poppinson"))


# 7.-Majority Vote
# Create a function that returns the majority vote in a list. A majority vote
# is an element thatoccurs > N/2 times in a list (where N is the length of the list).
# Link: https://edabit.com/challenge/pQavNkBbdmvSMmx5x
def majority_vote(lst:list) -> str | None:
    """Function that receives a list of letters,
    and returns the letter that appears more than
    the length of the list divided by two

    Args:
        lst (list): list with lettters to be analized

    Returns:
        _type_: the letter that appears more than the 
        length of the list divided by teo or None if 
        this doesn´t happen
    """
    lim:int = len(lst)/2
    counter_ls:list = [el if lst.count(el) > lim else 0 for el in lst]
    majority_vote_ls:list = list(filter(lambda x: x != 0,\
                                list(dict.fromkeys(counter_ls))))
    return majority_vote_ls[0] if len(majority_vote_ls) > 0 else None
# Tests:
# print(majority_vote(["A", "B", "B", "B", "A", "A"]))
# print(majority_vote(["B", "B", "B"]))
# print(majority_vote(["A", "B", "B"]))
# print(majority_vote(["A", "A", "B"]))
# print(majority_vote(["A", "A", "A", "B", "C", "A"]))
# print(majority_vote(["B", "A", "B", "B", "C", "A", "B", "B"]))
# print(majority_vote(["A", "B", "B", "A", "C", "C"]))
# print(majority_vote(["A", "B"]))
# print(majority_vote(["A"]))
# print(majority_vote([]))


