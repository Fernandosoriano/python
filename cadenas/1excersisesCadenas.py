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

### 6.-Default Mood
# Create a function that takes in a current mood and return a sentence in 
# the following format: "Today, I am feeling {mood}". However, if no argument 
# is passed, return "Today, I am feeling neutral".

def mood_today(mood = 'neutral'):
    if mood:
        return "Today, I am feeling" + " " + mood 
    return "Today, I am feeling neutral" 

# mood_today = lambda mood = 'neutral': f'Today, I am feeling {mood}' if mood else f"Today, I am feeling {mood}" 
# print(mood_today())

### 7.-Shuffle the Name
# Create a function that takes a string (will be a person's first and last name)
# and returns a string with the first and last name swapped.

# def name_shuffle(txt):
#     listName = txt.split()
#     return f"{listName[1]} {listName[0]}"
# def name_shuffle(txt):
#     # listName = txt.split()
#     return "{0} {1}".format(txt.split()[1], txt.split()[0])
# name_shuffle = lambda txt:
name_shuffle = lambda txt: "{0} {1}".format(txt.split()[1], txt.split()[0])
# FUENTE:https://edabit.com/challenge/pKSL3HtApPYAJ72CJ 
# Examples
# print(name_shuffle("Donald Trump"))
# print(name_shuffle("Rosie O'Donnell"))
# print(name_shuffle("Seymour Butts"))



### 8.-Hiding the Card Number
# Write a function that takes a credit card number and only displays the last four characters.
# The rest of the card number must be replaced by ************.

card_hide = lambda card: ''.join(['*' for i in card[:len(card)-4]]) + (card[-4:])
# print(card_hide("1234123456785678"))
# print(card_hide("8754456321113213"))
# print(card_hide("35123413355523"))

### 9.-The Reverser!
# The "Reverser" takes a string as input and returns that string in reverse order,
# with the opposite case.
reverse = lambda txt: txt[::-1].swapcase()
# print(reverse("Hello World"))

### 10.-Hamming Distance
# Hamming distance is the number of characters that differ between two strings.
# To illustrate:
# String1: "abcbba"
# String2: "abcbda"
# Hamming Distance: 1 - "b" vs. "d" is the only difference.
# hamming_distance("abcde", "bcdef")
def hamming_distance(txt1, txt2):
    lst = list(zip(txt1, txt2)) #DOCU for zip: https://docs.python.org/3/library/functions.html#zip
    return sum([1 for t in lst if t[0] != t[1] ])
# FUENTE: https://edabit.com/challenge/nfWirHJzNRBMAp9Df
# print(hamming_distance("abcde", "bcdef"))
# print(hamming_distance("abcde", "abcde"))
# print(hamming_distance("strong", "strung"))

# El más votado: 
# def hamming_distance(txt1, txt2):
# 	return sum(x!=y for (x,y) in zip(txt1,txt2))