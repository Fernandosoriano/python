### 1.-Find ASCII Charcode of Inverse Case Character
# Create a function that takes a single character as an argument and
# returns the char code of its lowercased / uppercased counterpart.
# FUENTE: https://edabit.com/challenge/QFXMcwaQZ8FTAuEtg
counterpartCharCode = lambda char:ord(char.swapcase())
# print(counterpartCharCode("a"))

### 2.-Correct Inequality Signs
# Create a function that returns True if a given inequality expression
# is correct and False otherwise.
# FUENTE:https://edabit.com/challenge/eA94BuKYjwMoNQSE2
correct_signs = lambda txt: eval(txt)
# print(correct_signs("3 < 7 < 11"))
# print(correct_signs("13 > 44 > 33 > 1"))
# print(correct_signs("1 < 2 < 6 < 9 > 3"))