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
V_DAC(0)
V_DAC(1023)
V_DAC(400)
        
