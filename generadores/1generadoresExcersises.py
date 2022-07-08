#1.-Ejemplo del uso de un generador, para generar una lista con todos los números
# pares anteriores a un número dado
def generaNumerosPares (n):
        for i in range (n):
                if i % 2 == 0:
                        yield i
# print(list(generaNumerosPares(10)))

#2.-Ejemplo sencillo de l asintaxis de un gnerador
def NumerosAnteriores (n):
        while n > 0 :
                yield n
                n = n - 1

#3.-Ejemplo para sumar todos los números anteriores a un número dado usando un generador
# print (sum(list(NumerosAnteriores(4))))
def sumarElementosList (n):
        def NumerosAnteriores (n):
                while n > 0 :
                        yield n
                        n = n - 1
        listaNumeros = list(NumerosAnteriores(n))
        suma = 0
        for i in listaNumeros:
                suma = suma + i
        print(suma)
# sumarElementosList(4)