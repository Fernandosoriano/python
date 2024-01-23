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

### 4.-Return the Index of All Capital Letters
# Create a function that takes a single string as argument and returns
# an ordered list containing the indices of all capital letters in the string.
index_of_caps = lambda word: [word.index(i) for i in word if i.isupper()]
# FUENTE: https://edabit.com/challenge/rQkriLJBc9CbfRbJb

# print(index_of_caps("eDaBiT"))
# print(index_of_caps("eQuINoX"))
# print(index_of_caps("determine"))
# print(index_of_caps("STRIKE"))
# print(index_of_caps("sUn"))

### 5.-Repeating Letters
# Create a function that takes a string and returns a string in which each 
# character is repeated once.
double_char = lambda txt: ''.join([l*2 for l in txt])
# FUENTE: https://edabit.com/challenge/HpqLxNqqRvMQoz8ME
# print(double_char("String"))
# print(double_char("Hello World!")) 
# print(double_char("1234!_ "))


#6.-Burglary Series (03): Is It Gone?
# Your spouse is not concerned with the loss of material possessions but rather
# with his/her favorite pet. Is it gone?! Given a dictionary of the stolen 
# items and a string in lowercase representing the name of the pet (e.g. "rambo"),
# return:
# "Rambo is gone..." if the name is on the list.
# "Rambo is here!" if the name is not on the list.
# Note that the first letter of the name in the return statement is capitalized.
find_it = lambda items, name : f'{name.capitalize()} is gone...' if name in items else f'{name.capitalize()} is here!'
# FUENTE: https://edabit.com/challenge/2wQPKcSipXmK4idwD

# print(find_it({
#   "tv": 30,
#   "stereo": 50,
# 	"julius": 100,											 
# }, "julius"))

#8.-CMS Selector Based on a Given String
# Write a function that takes a list of strings and a pattern (string) and returns 
# the strings that contain the pattern in alphabetical order. If the pattern is an 
# empty string, return all the strings passed in the input list.

def cms_selector(lst, txt):
    # lw = [w.lower() for w in lst]
    return sorted([w for w in lst if txt in w ])

# print(cms_selector(["WordPress", "Joomla", "Drupal"], "w"))
# print(cms_selector(["WordPress", "Joomla", "Drupal", "Magento", "Shopify", "Blogger"], "er"))
# print(cms_selector(["WordPress", "Joomla", "Drupal", "Magento", "Shopify", "Blogger"], "o"))
# print(cms_selector(["WordPress", "Joomla", "Drupal", "Magento", "Shopify", "Blogger"], ""))
# print(cms_selector(["WordPress", "Joomla", "Drupal", "Magento", "Shopify", "Blogger"], "JO"))



