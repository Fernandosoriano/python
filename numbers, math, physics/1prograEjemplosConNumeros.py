### 1.-Curzon Numbers
# In this challenge, establish if a given integer num is a Curzon number. If 1 plus
# 2 elevated to num is exactly divisible by 1 plus 2 multiplied by num, then num
# is a Curzon number. Given a non-negative integer num, implement a function that
# returns True if num is a Curzon number, or False otherwise.
# FUENTE: https://edabit.com/challenge/HYjQKDXFfeppcWmLX
def is_curzon(num):
    potencia = (2**num) + 1
    multiplica =  (2*num) + 1 
    if potencia % multiplica == 0:
        return True
    return False
# print(is_curzon(5))
# print(is_curzon(10))
# print(is_curzon(14))

### 2.- Calculating Damage
# Create a function that takes damage and speed (attacks per second) and 
# returns the amount of damage after a given time.
# FUENTE:https://edabit.com/challenge/HSHHkdRYXfgfZSqri
def damage(damage, speed, time):
    if damage<0 or speed<0:
        return 'invalid'
    time_low = time.lower()
    if time_low == 'second':
        resulting_damage = damage * speed
        return resulting_damage
    elif time_low == 'minute':
        time_seconds = speed * 60
        resulting_damage = damage * time_seconds
        return resulting_damage
    time_seconds = speed*60*60
    resulting_damage = damage * time_seconds
    return resulting_damage
# print(damage(40, 5, "second"))
# print(damage(100, 1, "minute"))
# print(damage(2, 100, "hour"))
# print(damage(-2, 100, "hour"))

### 3.- Sum of Resistance in Series Circuits
# When resistors are connected together in series, the same current passes through
# each resistor in the chain and the total resistance, RT, of the circuit must be
# equal to the sum of all the individual resistors added together. That is:
# RT = R1 + R2 + R3 ...
# Create a function that takes an array of values resistance that are connected 
# in series, and calculates the total resistance of the circuit in ohms. The ohm
# is the standard unit of electrical resistance in the International System of 
# Units ( SI ).
def series_resistance(lst):
    suma = 0
    for resistencia in lst:
        suma = suma + resistencia
    if suma>1:
        return f'{suma} ohms'
    return f'{suma} ohm'         
# print(series_resistance([1, 5, 6, 3]))

### 4.-Radians to Degrees
# Create a function that takes an angle in radians and returns the corresponding 
# angle in degrees rounded to one decimal place.
# from math import pi
def radians_to_degrees(rad):
    from math import pi
    degrees = (360 * rad) / (2*pi)
    return round(degrees,1)
# print(radians_to_degrees(50))

### 5.-Return the Factorial
# Create a function that takes an integer and returns the factorial of that integer.
# That is, the integer multiplied by all positive lower integers.
# FUENTE: https://edabit.com/challenge/FF6kYPHdAcJnoosr5
def factorial(num):
    if num > 0:
        factorial = 1
        lista_factorial = []
        while num >= 1:
            lista_factorial.append(num)
            num = num - 1 
        for num in lista_factorial:
            factorial = factorial * num
        return factorial
# Versión con recursividad, vista en las soluciones del link :   
def factorial(num):
	return 1 if num < 2 else num * factorial(num - 1)

### 6.-War of Numbers
# There's a great war between the even and odd numbers. Many numbers already lost
# their lives in this war and it's your task to end this. You have to determine
# which group sums larger: the evens or the odds. The larger group wins.
# Create a function that takes a list of integers, sums the even and odd numbers
# separately, then returns the difference between the sums of the even and odd
# numbers.
# FUENTE: https://edabit.com/challenge/rMr8yRxS8TeF9pDyn

def war_of_numbers(lst):
    suma_par     = 0
    suma_inpar   = 0
    list_pares   = []
    list_inpares = []
    for num in lst:
        if num % 2 == 0:
            list_pares.append(num)
        elif num % 2 != 0:
            list_inpares.append(num)
    for num in list_pares:
        suma_par = suma_par + num
    for num in list_inpares:
        suma_inpar = suma_inpar + num
    if suma_par > suma_inpar:
        return suma_par - suma_inpar
    return suma_inpar - suma_par
# El más votado en el link fuente:
def war_of_numbers(lst):
  return abs(sum(n if n % 2 else -n for n in lst))
    
# print(war_of_numbers([5, 9, 45, 6, 2, 7, 34, 8, 6, 90, 5, 243]))

        
    



