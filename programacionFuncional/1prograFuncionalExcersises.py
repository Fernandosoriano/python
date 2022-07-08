#1.- https://edabit.com/challenge/2hsyXkzDRewGSPpPE                
# Create a function that returns a base-2 (binary) representation of a base-10 (decimal) string number. 
# To convert is simple:((2) means base-2 and (10) means base-10) 010101001(2) = 1 + 8 + 32 + 128.		 
from sqlite3 import ProgrammingError


def binary(decimal):
        if decimal == 0: print ("0")
        dividendo = decimal
        elementosBinario = []
        while dividendo >= 1:
                elementosBinario.append(dividendo % 2)
                # print(dividendo % 2)
                dividendo = dividendo // 2
        elementosBinarioReverse = elementosBinario[::-1]
        numeroBinario = "".join([str(i) for i in elementosBinarioReverse])
        print(numeroBinario)
# binary(0)

#2.-Create a function that takes in a current mood and return a sentence in the following format:
#"Today, I am feeling {mood}". However, if no argument is passed, return "Today, I am feeling
# neutral".
# url: https://edabit.com/challenge/tgEWKRQD8hu5dD3pX
def mood_today(mood = "neutro"):
        moodLower = mood.lower()
        # message = "estoy {}".format(mood.lower()) if mood.lower() == "sad" or mood.lower() == "happy" else "estoy neutro"
        # message = f"Today, I am feeling {moodLower}" if mood.lower() == "sad" or mood.lower() == "happy" else "estoy neutro"
        if  mood.lower() == "sad" or mood.lower() == "happy":
                message = f"Today, I am feeling {moodLower}"
        elif mood == "neutro":
                message = "Today, I am feeling neutral"
        print(message)
# mood_today("happy")
# mood_today("sad")
# mood_today()

#3.-Create a function that takes a number num and returns its length.
# Notes
# The use of the len() function is prohibited.
# url:https://edabit.com/challenge/2zKetgAJp4WRFXiDT
# Examples:
# number_length(10) ➞ 2
# number_length(5000) ➞ 4
# number_length(0) ➞ 1
def number_length(numero):
        contador = 0
        numStr = str(numero)
        for i in numStr:
                contador = contador + 1
        print (contador)
# number_length(0)

#4.-eval performs the multiplication passed as argument
def pruebaEval (number1, operator, number2):
        if operator == "*":
                multplica = eval('number1 * number2')
                print(multplica)
        elif operator == "+":
                suma = eval('number1 + number2')
                print(suma)
# pruebaEval(2, "*", 2)
# pruebaEval(2, "+", 8)

#5.- Curzon Numbers
# In this challenge, establish if a given integer num is a Curzon number. If 1
# plus 2 elevated to num is exactly divisible by 1 plus 2 multiplied by num,
# then num is a Curzon number.
# URL:https://edabit.com/challenge/HYjQKDXFfeppcWmLX
def is_curzon(numero):
        if(numero<0): return print("no se aceptan números negativos")
        msg = "True" if (1 + 2**numero) % (1+ 2* numero) == 0 else "False"
        print (msg)
# is_curzon(5)
# is_curzon(10)
# is_curzon(14)

#6.-FizzBuzz Interview Question
# Create a function that takes a number as an argument and returns "Fizz", "Buzz" or "FizzBuzz".
# If the number is a multiple of 3 the output should be "Fizz".
# If the number given is a multiple of 5, the output should be "Buzz".
# If the number given is a multiple of both 3 and 5, the output should be "FizzBuzz".
# If the number is not a multiple of either 3 or 5, the number should be output on its own as shown in the examples below.
# The output should always be a string even if it is not a multiple of 3 or 5.
# Examples
def fizz_buzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Frizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return num
# print(fizz_buzz(3) )#➞ "Fizz"
# print(fizz_buzz(5) )#➞ "Buzz"
# print(fizz_buzz(15)) #➞ "FizzBuzz"
# print(fizz_buzz(4) )#➞ "4"

#7.-Serie de Fibo
def fibonacci (n):
   a = 0
   b = 1
   for i in range(n):
        print(a)
        a, b = b, a + b
        # c = a+b
        # a = b
        # b = c
#fibonacci (7)

# 8.- suma de gauss
def sumaGauss (n):
        suma = (n * (n+1)) / 2
        print(f'la suma usando la fórmula de Gauss es {int(suma)}')
# sumaGauss(4)

#9.-Factorial con while:
def factorialWhile(numero):
        factorial = 1
        while numero > 1:
                factorial = factorial * numero
                numero = numero - 1
        print(factorial)
# factorialWhile(0)

#10.-Factorial con for
# ahora me reto a hacerlo con un for:
def factorialFor(numero):
        factorial = 1
        for i in range(numero):
                factorial = factorial * numero
                numero = numero - 1
        print(factorial)
# factorialFor(6)

# NOTA: en la siguiente serie aparece en el primer ejercicio
# una forma más abreviada de calclar el factorial con Progra
# recursiva y uso de ternarios 

