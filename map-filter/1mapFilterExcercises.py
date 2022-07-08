#1.- How Many Vowels? Create a function that takes 
# a string and returns the number (count) of vowels contained within it.
# URL: https://edabit.com/challenge/p88k8yHRPTMPt4bBo
# Examples
# count_vowels("Celebration") ➞ 5
# count_vowels("Palm") ➞ 1
# count_vowels("Prediction") ➞ 4
def count_vowels(palabra):
        palabraArr = list(palabra)
        def identtificaVocal(letra):
                vocals = ["a","e","i","o","u"]  
                if letra.lower() in vocals:
                        return letra
        # listVowels = list(filter(lambda letra: letra.lower() in ["a","e","i","o","u"], palabraArr))
        listVowels = list(filter(identtificaVocal, palabraArr))
        print(len(listVowels))
# count_vowels("Palmm")
# count_vowels("PrEdiction")
# count_vowels("Celebration")

#2.- Ejercicio para probar los métodos map y filter en python
listaNumeros = [0,1,2,3,4,5,6,7,8,9,10,11]
def multiplica(value):
        return value*5
def multiplicarLista(func,lista):
        print(list(map(func,lista)))
# multiplicarLista(multiplica,listaNumeros)
# print(list(filter(lambda x: x % 2 == 0,listaNumeros)))