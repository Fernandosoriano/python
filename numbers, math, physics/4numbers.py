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

# print(row_sum(1000))




