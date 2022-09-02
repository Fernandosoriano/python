# 1.-
def invertirCadena (cadena):
    cadenaInvertida = cadena[::-1]
    print (cadenaInvertida)
# invertirCadena('estoy probando')

# 2.-
def esPalindromo(cadena):
    cadenaMinus = cadena.lower().replace(" ", "")
    cadenaInvertida = cadena[::-1]
    cadenaInvertidaMinus = cadenaInvertida.lower().replace(" ", "")
    # print(cadenaMinus, cadenaInvertidaMinus)
    if(cadenaMinus == cadenaInvertidaMinus):
        print(cadena + ' ' + 'es palindromo')
    else:
        print('no es palindromo')
# esPalindromo('A la GORDA drOgALa')

#3.-Formateo de cadenas
# name = input('Ingresa tu nombre por favor: ')
# edad = input('Ingresa tu edad por favor: ')
msg = '{name} tiene {edad} años'.format(name = "fer", edad = 23)
# print(msg)
msg2 = "la variable {} es un boleano, mientras que {} es de tipo number y {} es un string".format(True,4, 'fernando')
# print(msg2)

# 4.- Remove Repeated Letters
# Create a function that replaces all consecutively repeated letters
# in a word with single letters.
def remove_repeats(s):
   if len(s)<2:
       return s
   if s[0] != s[1]:
       return s[0]+remove_repeats(s[1:])
   return remove_repeats(s[1:])

# print(remove_repeats("aaabbbcccaaa"))
# print(remove_repeats("bookkeeper"))
# remove_repeats("geeksforgeeks")
# remove_repeats("aaabbbccc") => abc
# FUENTE: https://www.geeksforgeeks.org/remove-consecutive-duplicates-string/

### 5.-How Many Vowels?
# Create a function that takes a string and returns the number (count) of vowels
# contained within it.
def count_vowels(txt):
    l = ['a','e','i','o','u']
    suma = 0
    for letra in txt:
        if letra.lower() in l:
            suma = suma + 1
    return suma
# El más votado por la comunidad:
# def count_vowels(txt):
#   return sum([1 for x in txt.lower() if x in 'aeiou']) 

# Modifiqué el más votado por una fun lambda:
count_vowels_lam = lambda txt: sum([1 for x in txt.lower() if x in 'aeiou']) 

# FUENTE:https://edabit.com/challenge/p88k8yHRPTMPt4bBo
# print(count_vowels_lam("Prediction"))
