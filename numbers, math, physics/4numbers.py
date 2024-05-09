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
