# 1.-Factorial con recursividad y operador ternario
def factorialRecursivoTernario (numero):
        numero = numero if numero == 1 else numero * factorialRecursivoTernario(numero-1)
        return numero
        # if numero == 1:
        #         return numero
        # else:
        #      return numero * factorial(numero-1)
# print(factorialRecursivoTernario(1))