#1.- Create a function which returns the number of True values there are in an array.
#example : countTrue([true, false, false, true, false]) ➞ 2
def countTrue(array = None):
    # nums = [11, 22, 33, 44, 55]
    # res = list(filter(lambda x: x%2==0, nums))
    # print(res)
    if type(array) != list:
        return print('Solo se aceptan listas como argumento, gracias')
    if array == None:
         return print ('por favor ingresa una lista')
    for i in array:
        if type(i) != bool:
            return print('sólo se aceptan listas con booleanos')
    listTrue = list(filter(lambda v:  v == True, array))

    print(f'el valor booleano true, aparece {len(listTrue)} veces')
    # print(listTrue)
# countTrue([True, False, False, True, False])

#2.- Stuttering Function: Write a function that stutters a word as if someone is struggling to read it.
#  The first two letters are repeated twice with an ellipsis ... 
# and space after each, and then the word is pronounced with a question mark ?.
# stutter("incredible") ➞ "in... in... incredible?
def stutter (word):
        firstTwo = word[:2]  #Recuerda que en los CORTES DE LISTA no se toma el último elemento
        # print(firstTwo + "..." + firstTwo + "..." + word+"?")
        print(f'{firstTwo}... {firstTwo}... {word}')
# stutter("increasing")

#3.- Programa una función que dado un arreglo de elementos, elimine los 
# // duplicados, pe. miFuncion(["x", 10, "x", 2, "10", 10, true, true]) devolverá ["x", 10, 2, "10", true]
def eliminaRepetidos(lista):
    listaSinRepetir = []
    for i in lista:
        if(not i in listaSinRepetir):
            listaSinRepetir.append(i)
    print(listaSinRepetir)
# eliminaRepetidos(["x", 10, "x", 2, "10", 10, True, True])

#4.-Programa una función que dado un arreglo de números obtenga el promedio,
# //  pe. promedio([9,8,7,6,5,4,3,2,1,0]) devolverá 4.5.
def promedio(lista):
    if (type(lista) != list):
    # if (not (isinstance(lista, list))):
         return print('sólo se aceptan listas como argumentos')    
    for i in lista:
        if (type(i) != int or type(i) != float ):
            return print('algún elemento de tu lista no es un número') 
    suma = 0 
    for i in lista:
        suma += i
    promedio = suma/len(lista)
    print(promedio)
# promedio([9,8,7,6,5,4,3,2,1,0])
# def imprimirType(lista):
#     print(type(lista))
# imprimirType([2,4,5,6])

#5.-Two Distinct Elements
# In each input list, every number repeats
# at least once, except for two. Write a function that returns the two unique numbers.
# Examples
# return_unique([1, 9, 8, 8, 7, 6, 1, 6]) ➞ [9, 7]
# return_unique([5, 5, 2, 4, 4, 4, 9, 9, 9, 1]) ➞ [2, 1]
# return_unique([9, 5, 6, 8, 7, 7, 1, 1, 1, 1, 1, 9, 8]) ➞ [5, 6]
# URL : https://edabit.com/challenge/yL5WmWTCNwwb4GnR7
def return_unique(listaInput):
    # la función count3, edecidí progrmarla, por curiosidad de ver cómo
    # se hacia sin usar la función count predefinida de python
    def count3(terminoAContar,lista):
        return len(list(filter(lambda elementList: elementList == terminoAContar,lista)))
    listaUnicos = []
    for i in listaInput:
        # if lista.count(i) == 1: descomentar esta línea si quieres usar count de python
        if count3(i,listaInput) == 1:
            listaUnicos.append(i)
    print(listaUnicos)
# return_unique([1, 9, 8, 8, 7, 6, 1, 6])
# return_unique([5, 5, 2, 4, 4, 4, 9, 9, 9, 1])
# return_unique([9, 5, 6, 8, 7, 7, 1, 1, 1, 1, 1, 9, 8])

#6.-La función max() del ejercicio 1 (primera parte) y la función max_de_tres() del ejercicio 2
#(primera parte), solo van a funcionar para 2 o 3 números. Supongamos que tenemos mas de 3 números
#o no sabemos cuantos números son. Escribir una función max_in_list() que tome una lista de números y
#devuelva el mas grande.
def max_in_list(lista):
    maximo = lista[len(lista)-1]
    for i in lista:
        if i > maximo:
            maximo = i
        else:
            maximo = maximo
    print(maximo)
# max_in_list([34,1,2,3,4])
def min_in_list (lista):
    minimo = lista[0]
    for i in lista:
        minimo = i if i < minimo else minimo
    print(minimo)
# min_in_list([1,0,2,-30,4,-1])
# ejemplo para entedner el operado rternario:
# es_bonito = True   
# estado = "Es bonito" if es_bonito else "No es bonito"
# print(estado)
# print(max([1,2,3,4]))

# 7.-Escribir una función mas_larga() que tome una lista de palabras y 
# devuelva la mas larga.
def mas_larga(lista):
    masLarga = lista[0]
    for i in lista:
        masLarga = i if len(i) >= len(masLarga) else masLarga 
    print(masLarga)        
        # print (len(i))
# mas_larga(["Fernando0000000000000000000", "fernandiosooooooooo", "Jocelynisca", "Naremi"])

### 7.-Fix the Error: Filtering out Empty Arrays
# I am trying to filter out empty arrays from an array. In other words, I want to
# transform something that looks like this: ["a", "b", [], [], [1, 2, 3]] to
# look like ["a", "b", [1, 2, 3]]. My code looks like this:
def remove_empty_arrays(arr):
		return [x for x in arr if x != [] ]
# FUENTE: https://edabit.com/challenge/raN9mCseAYJvoJQtQ
# print(remove_empty_arrays([1, 2, [], 4]))


### 8.-Find the Odd Integer
# Create a function that takes a list and finds the integer which appears
# an odd number of times.

def find_odd(lst):
    for numero in lst:
        if lst.count(numero) % 2 != 0:
            return numero
# FUENTE : https://edabit.com/challenge/9TcXrWEGH3DaCgPBs       

# print(find_odd([1, 1, 2, -2, 5, 2, 4, 4, -1, -2, 5]))
# print(find_odd([20, 1, 1, 2, 2, 3, 3, 5, 5, 4, 20, 4, 5]))
# print(find_odd([10]))