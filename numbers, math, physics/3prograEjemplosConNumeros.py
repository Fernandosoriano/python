### 1.-Cricket Balls to Overs!
# In cricket, an over consists of six deliveries a bowler bowls from one end.
# Create a function that takes the number of balls bowled by a bowler and calculates
# the number of overs and balls bowled by him/her. Return the value as a float,
# in the format overs.balls.
# FUENTE:https://edabit.com/challenge/guR6aa2zytfZvywMS
def total_overs(balls):
    t = divmod(balls, 6) #this method takes two numbers as arguments and returns their 
                         #quotient and remainder in a tuple
    return f'{t[0]}' if  t[1] == 0 else f'{t[0]}.{t[1]}'
# print(total_overs(2400))
# print(total_overs(164))
# print(total_overs(945))
# print(total_overs(5))

### 2.-Harshad Numbers
# A number n is a Harshad (also called Niven) number if it is divisible by 
# the sum of its digits. For example, 666 is divisible by 6 + 6 + 6, so it is
# a Harshad number.
# Write a function to determine whether the given number is a Harshad number.
def is_harshad(num):
    sNum = str (num)
    suma = 0
    for i in sNum:
        suma += int(i)
    return True if num % suma == 0 else False
# FUENTE: https://edabit.com/challenge/ZDDyfBFBWMotQSYin
# print(is_harshad(23) )  


### 3.-Number Split
# Given a number, return a list containing the two halves of the number.
# If the number is odd, make the rightmost number higher.
def number_split (n):
    import math 
    return [math.floor(n/2),math.ceil(n-math.floor(n/2))]
# print(number_split(11))
# FUENTE:https://edabit.com/challenge/9f3Mi6vHNcm8vRcSh 



### 5
def solve_for_exp(b,n):
    l = []
    e = n/b
    while e >= 1:
        l.append(e)
        n = e
        e = n/b
    return len(l)
# print(solve_for_exp(4,1024))
# print(solve_for_exp(2, 1024))
# print(solve_for_exp(9, 3486784401))

#### 6.-Cricket Balls to Overs!
# In cricket, an over consists of six deliveries a bowler
# bowls from one end. Create a function that takes the number of
# balls bowled by a bowler and calculates the number of overs
# and balls bowled by him/her. Return the value as a float, in the format overs.balls.

def total_overs(balls:int):
    return balls//6 if balls%6 == 0 else float(f'{balls//6}.{balls%6}')
# FUENTE: https://edabit.com/challenge/guR6aa2zytfZvywMS
# print(total_overs(0)


### 7.-A Circle and Two Squares
# Imagine a circle and two squares: a smaller and a bigger one. For the smaller one,
# the circle is a circumcircle and for the bigger one, an incircle.

# Create a function, that takes an integer (radius of the circle) and returns
# the difference of the areas of the two squares.

# Examples
# square_areas_difference(5) ➞ 50

# square_areas_difference(6) ➞ 72

# square_areas_difference(7) ➞ 98


def square_areas_difference (r:int) -> int|str : 
    """
    Doc: https://edabit.com/challenge/NNhkGocuPMcryW7GP
    
    Function that takes an integer (radius) and returns
    the difference between two squres, a smaller and a bigger one. For the
    smaller one, the circle is a circumcircle and for the bigger one, an incircle.
    Args:
        r (int): radius of the circle it must be positive
    """
    return  4*r**2 - 2*r**2 if r > 0 else 'Please enter a positive radius'

# print(square_areas_difference(-5))

f = lambda  r: 4*r**2 - 2*r**2 if r > 0 else 'Please enter a positive radius'
# print(f(5))

### 8.- 
# import math
# print (int(math.log(1024, 2)))



def solve_for_exp(b:int, n:int) -> int:
    """Function that resolves a logaritm
       for integers numbers

    Args:
        b (int): number that acts like the basis of a logaritm
        n (int): number of  what you want to obtain their logaritm

    Returns:
        logaritm of one number
    """
    e = n / b 
    l = []
    while e != 1:
        e = e / b
        l.append(e)
    return len(l)+1
        
# print(solve_for_exp(10, 100000000))


