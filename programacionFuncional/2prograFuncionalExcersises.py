# 1.-Factorial con recursividad y operador ternario
def factorialRecursivoTernario (numero):
        numero = numero if numero == 1 else numero * factorialRecursivoTernario(numero-1)
        return numero
        # if numero == 1:
        #         return numero
        # else:
        #      return numero * factorial(numero-1)
# print(factorialRecursivoTernario(1))

# 2.- A digital-to-analog converter 
#Fuente: https://edabit.com/challenge/AJGqpNL2yAyhbdpvB

def V_DAC(value):
        analog_voltage_measured  = (value * 5 ) / 1023
        print (round (analog_voltage_measured, 2))
# V_DAC(0)
# V_DAC(1023)
# V_DAC(400)

### 3.- Is it Time for Milk and Cookies?
# Christmas Eve is almost upon us, so naturally we need to prepare some milk
# and cookies for Santa! Create a function that accepts a Date object and 
# returns True if it's Christmas Eve (December 24th) and False otherwise.
import datetime
def time_for_milk_and_cookies(date):
        # if date.month == 12 and date.day == 24:
        #         return True
        # return False 
        True if  date.month == 12 and date.day == 24 else False    
# print(time_for_milk_and_cookies(datetime.date(2013, 12, 24)))
# print(time_for_milk_and_cookies(datetime.date(2013, 1, 23)))
# print(time_for_milk_and_cookies(datetime.date(3000, 12, 24)))