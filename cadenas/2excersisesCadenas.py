### 1.-Find ASCII Charcode of Inverse Case Character
# Create a function that takes a single character as an argument and
# returns the char code of its lowercased / uppercased counterpart.
# FUENTE: https://edabit.com/challenge/QFXMcwaQZ8FTAuEtg
counterpartCharCode = lambda char:ord(char.swapcase())
# print(counterpartCharCode("a"))

### 2.-Xs and Os, Nobody Knows
# Create a function that takes a string, checks if it has the same number of "x"s and "o"s 
# and returns either True or False.
# Return a boolean value (True or False).
# Return True if the amount of x's and o's are the same.
# Return False if they aren't the same amount.
# The string can contain any character.
# When "x" and "o" are not in the string, return True.
XO = lambda txt: True if txt.lower().count('x') == txt.lower().count('o') else False if txt.lower().count('x') != txt.lower().count('o') else True   
# FUENTE:https://edabit.com/challenge/JSJEuuWduBB5hEX6k
# la más votada:
#     def XO(text):
# ​
#   return text.lower().count('x')==text.lower().count('o')
# print(XO("ooxx"))

### 3.-Vowel Replacer
# Create a function that replaces all the vowels in a string with a
# specified character.
def replace_vowels(txt, ch):
    lst = []
    for l in txt.lower():
        if l in ('a','e','i','o','u'):
            l = ch 
        lst.append(l)        
    return(''.join(lst))
# La más votada:
# def replace_vowels(txt, ch):
#   return ''.join([i if i not in 'aeoui' else ch for i in txt])
# FUENTE:https://edabit.com/challenge/Ggq8GtYPeHJQg4v7q
# print(replace_vowels("thE aardvark","#"))
# print(replace_vowels("minnie mouse", "?"))
# print(replace_vowels("shakespeare", "*"))
