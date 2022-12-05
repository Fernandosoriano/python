### 1.-FizzBuzz Interview Question ###
# Create a function that takes a number as an argument and returns "Fizz",
# "Buzz" or "FizzBuzz".

# If the number is a multiple of 3 the output should be "Fizz".
# If the number given is a multiple of 5, the output should be "Buzz".
# If the number given is a multiple of both 3 and 5, the output should be "FizzBuzz".
# If the number is not a multiple of either 3 or 5, the number should be output
# on its own as shown in the examples below.
# The output should always be a string even if it is not a multiple of 3 or 5.

# def fizz_buzz(num):
fizz_buzz = lambda num:"FizzBuzz" if num % 3 == 0 and num % 5 == 0 else 'Fizz' if num % 3 == 0 else "Buzz" if num % 5 == 0 else str(num)
# print(fizz_buzz(15))

### 2.-Count Ones in Binary Representation of Integer ###

# Count the amount of ones in the binary representation of an integer. For example,
# since 12 is 1100 in binary, the return value should be 2.
# FUENTE : https://edabit.com/challenge/GbyPdqNnp75Wci7Cn
# def count_ones(num):
#     num_binary = format(num, "b")
#     return num_binary.count('1')
count_ones = lambda num: format(num, "b").count('1')
# print(count_ones(999))

### 3.-Pythagorean Triplet ###
# Create a function that validates whether three given integers form a Pythagorean
# triplet. The sum of the squares of the two smallest integers must equal the
# square of the largest number to be validated.
def is_triplet(n1, n2, n3):
    l = [n1, n2, n3]
    hyp = max(l)
    catetos = list(filter(lambda n: n != hyp, l))
    return True if catetos[0]**2 + catetos[1]**2 == hyp**2 else False
# print(is_triplet(3, 4, 5))
# el más votado:
def is_triplet(*n): #observa que usa *args, bibliografia= https://www.programiz.com/python-programming/args-and-kwargs
    a, b, c = sorted(n) #y sorted, bibliografia = https://www.programiz.com/python-programming/methods/built-in/sorted
    return a*a + b*b == c*c
# FUENTE: https://edabit.com/challenge/Ns4Sjh7KK58ofAph8

### 4.-Flatten the Curve ###
# Given a list of integers, replace every number with the mean of all numbers.

def flatten_the_curve(lst = []):
    if lst:
        import statistics
        mean = round(statistics.mean(lst),1)
        return [mean for num in lst]
    return []

# print(flatten_the_curve([]))   
	
# import statistics
# data = [11, 21, 11, 19, 46, 21, 19, 29, 21, 18, 3, 11, 11]
# x = statistics.mean(data)
# print(round(x,1))

### 5.- Geometry 1: Length of Line Segment
# Write a function that takes coordinates of two points on a two-dimensional
# plane and returns the length of the line segment connecting those two points.

from cmath import sqrt
import math
line_length = lambda x,y: round(math.sqrt((y[0]-x[0])**2+ (y[1]-x[1])**2),2)
# print(line_length([15, 7], [22, 11]))

### 6.- Sum of Evenly Divisible Numbers from a Range ###
# Create a function that takes three arguments a, b, c and returns the
# sum of the numbers that are evenly divided by c from the range a, b inclusive.
def evenly_divisible(a,b,c):
    lst = []
    for num in range(a,b+1):
        if num % c == 0:
            lst.append(num)
    return sum(lst)
# FUENTE: https://edabit.com/challenge/nWtgKSNGQ3sB52rQ8
# el más votado:
#     def evenly_divisible(a, b, c):
#   return sum(i for i in range(a, b+1) if not i%c)
# print(evenly_divisible(1, 10, 20))
# print(evenly_divisible(1, 10, 2))
# print(evenly_divisible(1, 10, 3))

### 7.-Find the Discount ###
# Create a function that takes two arguments: the original price and the
# discount percentage as integers and returns the final price after the discount.
# def dis(price, discount):
dis = lambda price, discount: round(price - ((discount/100)*price),2)
# FUENTE:https://edabit.com/challenge/cXnkmRdxqJrwdsP4n 
# print(dis(1500, 50))
# print(dis(89, 20))
# print(dis(100, 75))

### 8.-Circle or Square ###
# Given the radius of a circle and the area of a square, return True if
# the circumference of the circle is greater than the square's perimeter and
# False if the square's perimeter is greater than the circumference of the circle

# def circle_or_square(rad, area):
circle_or_square = lambda rad, area: True if 2*3.14*rad > (area**0.5) * 4 else False
# print(circle_or_square(16, 625))
# print(circle_or_square(5, 100) )
# print(circle_or_square(8, 144))

### 9.-Basic Calculator ###
# Create a function that takes two numbers and a mathematical operator + - / * 
# and will perform a calculation with the given numbers.
calculator = lambda num1, operator, num2: "Can't divide by 0!" if num2 == 0 else eval('num1' + operator + 'num2') 
# FUENTE:https://edabit.com/challenge/ZdnwC3PsXPQTdTiKf
# print(calculator(2, '/', 2)) 

# Probabilities (Part 1)

### 10.-Probabilities (Part 1) ###
# Given a list of numbers and a value n, write a function that returns the probability
# of choosing a number greater than or equal to n from the list. The probability should
# be expressed as a percentage, rounded to one decimal place.
# FUENTE: https://edabit.com/challenge/LMjficQtWW36a3by3
probability = lambda lst, n : round((len([i for i in lst if i>= n])/ len(lst))*100,1)
# print(probability([5, 1, 8, 9], 6))
# print(probability([7, 4, 17, 14, 12, 3], 16))
# print(probability([4, 6, 2, 9, 15, 18, 8, 2, 10, 8], 6))

