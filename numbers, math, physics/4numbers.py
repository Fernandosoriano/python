#1.- Next Number Greater Than A and B and Divisible by B
# You are given two numbers a and b. Create
# a function that returns the next number greater than a and b and divisible by b.
def divisible_by_b(a:int, b:int) -> int:
    """function that takes two numbers (a,b)
    a>b and returns a number that's equal or
    greater than a, and is divisible by b

    Args:
        a (int): bigger number
        b (int): number in which the returned number has to be divisible

    Returns:
        int: number that is greater thn a and b, and is divisible by b
    """
    while a%b !=0:
            a += 1
    return a
# print(divisible_by_b(17, 8))
# divisible_by_b(98, 3)
# divisible_by_b(14, 11) 
# divisible_by_b(11, 8)
# divisible_by_b(450, 36)
# divisible_by_b(1019, 13)

# 2.-How Many Solutions Does This Quadratic Have?
# A quadratic equation a x² + b x + c = 0 has either 0, 1, or 2 distinct
# solutions for real values of x. Given a, b and c, you should return the
# number of solutions to the equation.
solutions = lambda a,b,c: 2 if b**2-4*a*c>0 else 1 if b**2-4*a*c==0 else 0
# print(solutions(1, 0, -1))
# print(solutions(1, 0, 0))
# print(solutions(1, 0, 1))
# print(solutions(200, 420, 800))
# print(solutions(200, 420, -800))
# print(solutions(1000, 1000, 0))
# print(solutions(10000, 400, 4))

# 3.-List of Multiples
# Create a function that takes two numbers as arguments (num, length) 
# and returns a list of multiples of num until the list length reaches length.
# LINK = https://edabit.com/challenge/BuwHwPvt92yw574zB

# def list_of_multiples(num, length):  
#     l = [num*(i+1) for i in range(length)]
#     return l
list_of_multiples = lambda num,length:[num*(i+1) for i in range(length)]
# print(list_of_multiples(7, 5))
# print(list_of_multiples(12, 10))
# print(list_of_multiples(17, 6))


# 4.-Quadratic Equation
# LINK = https://edabit.com/challenge/MDWFcHCTiJfHmwTFx
# Create a function to find only the root value of x in any
# quadratic equation ax^2 + bx + c. The function will take three arguments:
# def quadratic_equation(a, b, c):
#     # import math
#     root_1, root_2 = (-b+(b**2-4*a*c)**0.5)/2*a, (-b-(b**2-4*a*c)**0.5)/2*a
#     print(int(root_1), root_2)
quadratic_equation = lambda a,b,c: int((-b+(b**2-4*a*c)**0.5)/2*a)
# print(quadratic_equation(1, 2, -3))
# quadratic_equation(2, -7, 3)
# quadratic_equation(1, -12, -28)

#5.-Hex to Binary
# Create a function that will take a HEX number and returns the binary
# equivalent (as a string).
# LINK = https://edabit.com/challenge/BuCaGYh8keiWJGmcC
to_binary = lambda num: "{0:08b}".format(int(num, 16))

# print(type(to_binary('0xFF')))
# print(to_binary('0xAA'))
# print(to_binary('0xFA'))


#6.-The Snake — Area Filling
# This challenge is based on the classic videogame "Snake".
# Assume the game screen is an n * n square, and the snake 
# starts the game with length 1 (i.e. just the head) positioned
# on the top left corner.

# In this version of the game, the length of the snake doubles
# each time it eats food (e.g. if the length is 4, after eating it becomes 8).

# Create a function that takes the side n of the game screen
# and returns the number of times the snake can eat before it
# runs out of space in the game screen.

def snakefill(n:int) -> int:
    """function that receives a nummber n,
    that indicates the size of a grid of nxn, and
    returns a number n, that indicates number of times
    the snake can eat before it runs out of space in
    the grid.

    Args:
        n (_type_): number that indicates the size of a grid

    Returns:
        _type_:number of times
    the snake can eat before it runs out of space
    """
    area = n**2   
    for i in range (n):
        dif = area-(2**(i+1))
        # print('dif = ', dif, 'i+1=',i+1)
        if dif >= 0:
            number_of_times = i+1
        if dif < 0:  
            number_of_times = i+1-1      
            break
    return number_of_times 

# print(snakefill(900))


# 7.-Simple Row Sum
# Imagine this triangle:
# Create a function that takes a number n and
# returns the sum of all numbers in nth row.

# LINK = https://edabit.com/challenge/ysgbRFTPujx8v37yF

#     1
#    2 3
#   4 5 6
#  7 8 9 10
# ...

def row_sum(n:int) -> int: 
    """Function that receives a number, and returns the
    sum of the numbers that are in the level with this
    number in a pyramid like this:  
     1
    2 3
   4 5 6
  7 8 9 10
11 12 13 14 15

    Args:
        n (int): number of the row to calculate the
        sum

    Returns:
        int: the sum of the indicated row in the
        imaginary pyramid
    """
    l:list = [i for i in range(1,n+1)]
    l_2:list = [num for num in range (1,sum(l)+1)]
    return sum(l_2[len(l_2)-n::])

# print(row_sum(3))
# print(row_sum(1000))


# 8.-Add the Values of the Symbols in a Matrix
def check_score(simbols_matrix:list) -> int:
    """Function that receives a list of lists
    in which the element of each list is a simbol that is equivalent
    to a number, and this function do a cast, and returns
    the sum of all the equivalent number of the symbols, in case
    that the result is negative, this function returns 0

    Args:
        matrix_of_simbols (list): list of  lists of symbols to sum

    Returns:
        int: the result of the sum of all the numbers equivalent
        to one symbol
    """
    cast_dict:dict = {'#':5,
            'O':3,
            'X':1,
            '!':-1,
            '!!':-3,
            '!!!':-5}  
    res:int = sum([sum(list(map(lambda x: cast_dict[x], l_i))) for l_i in simbols_matrix])
    return res if res > 0 else 0


# TESTS  
# print(check_score([
# ["#", "!"],
# ["!!", "X"]
# ]) )
# print(check_score([
# ["!!!", "O", "!"], 
# ["X", "#", "!!!"],
# ["!!", "X", "O"]
# ]))
# print(check_score([
# ["#", "O", "#", "!!", "X", "!!", "#", "O", "O", "!!", "#", "X", "#", "O"],
# ["!!!", "!!!", "!!", "!!", "!", "!", "X", "!", "!!!", "O", "!", "!!!", "X", "#"],
# ["#", "X", "#", "!!!", "!", "!!", "#", "#", "!!", "X", "!!", "!!!", "X", "O"],
# ["!!", "X", "!!", "!!", "!!!", "#", "O", "O", "!!!", "#", "O", "O", "#", "!!"],
# ["O", "X", "#", "!", "!", "X", "!!!", "O", "!!!", "!!", "O", "!", "O", "X"],
# ["!!", "!!!", "X", "!!!", "!!", "!!", "!!!", "X", "O", "!", "#", "!!", "!!", "!!!"],
# ["!!", "!!", "#", "O", "!", "!!", "!", "!!!", "#", "O", "#", "!", "#", "!!"],
# ["X", "X", "O", "X", "!!!", "#", "!!!", "!!!", "X", "X", "X", "!", "#", "!!"],
# ["O", "!!!", "!", "O", "#", "!", "!", "#", "X", "X", "#", "O", "!!", "!"],
# ["X", "!", "!!", "#", "#", "X", "!!", "O", "!!", "X", "X", "!!", "#", "X"],
# ["!", "!!", "!!", "O", "!!", "!!", "#", "#", "!", "!!!", "O", "!", "#", "#"],
# ["!", "!!!", "!!", "X", "!!", "!!", "#", "!!!", "O", "!!", "!!!", "!", "!", "!"],
# ["!!!", "!!!", "!!", "O", "!", "!", "!!!", "!!!", "!!", "!!", "X", "!", "#", "#"],
# ["O", "O", "#", "O", "#", "!", "!!!", "X", "X", "O", "!", "!!!", "X", "O"]
# ]))
# print(check_score([['#', '!', 'O', '!!', '#', '!!', '!!', 'X', '!', 'X', '!!!',
# '!!!', 'X', '#'], ['!', '#', '!!', '!!!', 'X', 'X', '#', '!!', 'O', '!!!', '!',
# '!!!', '#', 'O'], ['O', 'X', '!!!', '#', '!!!', '!', '!', '!', '#', '!!', '!!!',
# 'X', '!', 'X'], ['#', '!!', '!!', '#', 'O', '!', 'X', 'X', '!!!', '#', '#', '!!!', 
# '#', '!'], ['#', 'O', 'X', 'X', '!!', '#', 'O', 'X', '#', '!', '!', '!', 'O', '#'],
# ['X', '!', 'X', 'O', '!', '!', '!!', '!!', '!!', '!!', '!!!', '!!!', '!', 'X'],
# ['!!!', '!', '!!', 'O', '!!!', 'X', '#', '#', 'X', 'X', '!', '!', 'X', '!'], 
# ['!!!', 'O', '!!!', '!!!', 'O', '#', '!!', '!!!', '!', '!!!', 'O', 'O', 'X', '!!!'],
# ['!!', 'X', 'O', '!!!', '!!', 'O', '#', 'X', 'O', 'X', '!!', 'X', '#', '!'], ['X', '#',
# '!!!', '!!!', '!!', '#', '!', '!!', 'O', '!', 'O', '#', '!!!', '#'], ['!', '#', '!',
# '!!!', '!!!', 'X', '!', 'X', '#', '!!', '!', '!!', 'X', '!!!'], ['!!!', '#', '#', '!!',
# 'O', '!!', '#', '!!!', '#', '#', '!!', '#', '!', 'O'], ['!!!', 'X', 'O', '!!', 'X', '!',
# 'O', 'X', 'O', '!!!', '#', '#', '#', '#'], ['X', 'X', '!!!', '!!', 'O', '#', 'O', '#', 'X'
# , 'X', 'X', '!!!', '!', '!!!']]))


# 9.-Powerful Numbers
# If the square of every item in p is also a factor of x, then x is 
# said to be a powerful number.
# Create a function that takes a number and returns True 
# if it's powerful, False if it's not.
# Link = https://edabit.com/challenge/aW8mz7Tky3gGiuQsX

def is_powerful(n:int) -> bool:
    """Function that recives a number and
    returns True if the number is  poewerful,
    and false in other case

    Args:
        n (int): number to evaluate

    Returns:
        bool: True if the number is poweful
    """
    prime_factors:list = []
    divisor:int = 2
    if n % divisor == 0:
        prime_factors.append(divisor)
        quotient:int = n//divisor
    else:
        quotient:float = n/divisor
        quotient:int = n
    while quotient != 1:
        if quotient % divisor != 0:
            divisor += 1
        elif quotient % divisor == 0:
            quotient = quotient/divisor
            prime_factors.append(divisor)
# The process since the code line 242 to 255 is to find the prime numbers
# of the received number as a parameter
    no_repeated_prime_factors:list = list(dict.fromkeys(prime_factors))
    bool_list:list = [True if n%i**2==0 else False for i in no_repeated_prime_factors]
    return True if all(bool_list) else False
# TESTS:
# print(is_powerful(36))
# print(is_powerful(27))
# print(is_powerful(674))
# print(is_powerful(32))
# print(is_powerful(320))

# 10.-Calculated Bonus
# A financial institution provides professional services to banks and claims charges 
# from the customers based on the number of man-days provided. Internally, it has
# set a scheme to motivate and reward staff to meet and exceed targeted billable
# utilization and revenues by paying a bonus for each day claimed from customers
# in excess of a threshold target.

# This quarterly scheme is calculated with a threshold target of 32 days
# per quarter, and the incentive payment for each billable day in excess of such
# threshold target is shown as follows:

# Days	                Bonus
# 0 to 32 days	        Zero
# 33 to 40 days	        SGD$325 per billable day
# 41 to 48 days	        SGD$550 per billable day
# Greater than 48 days	SGD$600 per billable day

# Please note that incentive payment is calculated progressively. 
# As an example, if an employee reached total billable days of 45 in a
# quarter, his/her incentive payment is computed as follows:
# 32*0 + 8*325 + 5*550 = 5350
# Link:https://edabit.com/challenge/ksiA6Q34iXgTcMeZF

def bonus(days:int) -> int:
    """function that receives the number of days that a worker worked,
    and according wit this number of days, the function calculates
    the total bonus that the worker has earned

    Args:
        days (int): number of  worked days

    Returns:
        int: the total amount of bonus
    """
    total_bonus:list = []
    if days < 32:
        return 0
    periods_list:list = [[0,32,0], [33,40,325],[41,48,550],[49,36500,600]]
    for period in periods_list:
        if periods_list.index(period) == 0:
            total_bonus.append(0)
        else:
            if days > period[1]:
                total_bonus.append(8*period[2])
            elif days-(min(period))>0: 
                total_bonus.append(period[2]*(days-(min(period))+1))
            else:
                total_bonus.append(0)
    return (sum(total_bonus))
# TESTS
# print(bonus(15))
# print(bonus(37))
# print(bonus(50))








